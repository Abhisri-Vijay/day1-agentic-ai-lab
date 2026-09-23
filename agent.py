import json
from openai import OpenAI

from config import BASE_URL, API_KEY, MODEL, QUESTIONS
from tools import get_course_fee, calculate


client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee for a course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303"
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a simple arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression such as 12000 + 18000"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


def run_tool(name, arguments):
    if name == "get_course_fee":
        return get_course_fee(**arguments)

    if name == "calculate":
        return calculate(**arguments)

    raise ValueError(f"Unknown tool: {name}")


def ask_agent(question, max_steps=5):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful course-fee assistant. "
                "Use the available tools whenever you need exact course fees "
                "or calculations."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            return message.content

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"  [ACT] {name}({arguments})")

            result = run_tool(name, arguments)

            print(f"  [OBSERVE] {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

    return "Maximum agent steps reached."


for question in QUESTIONS:
    print("\nQ:", question)
    print("A:", ask_agent(question))