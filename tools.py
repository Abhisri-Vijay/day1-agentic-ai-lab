import ast
import operator as op

from config import COURSE_FEES


def get_course_fee(course_code: str) -> int:
    """Return the fee for a course code."""
    code = course_code.upper().strip()

    if code not in COURSE_FEES:
        raise ValueError(f"Unknown course code: {course_code}")

    return COURSE_FEES[code]


_ALLOWED = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}


def calculate(expression: str) -> float:
    """Safely evaluate simple arithmetic."""
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant) and isinstance(
            node.value, (int, float)
        ):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return _ALLOWED[type(node.op)](left, right)

        raise ValueError("Unsupported expression")

    return evaluate(tree)