import re
from config import COURSE_FEES, QUESTIONS


def answer(question):
    q = question.lower()

    # Q1: Single course fee
    match = re.search(r"(cs101|ai202|ds303)", q)
    if match and "fee" in q:
        code = match.group(1).upper()
        return f"Rs.{COURSE_FEES[code]:,}"

    # Q2: Two course total after scholarship
    if "total" in q and "scholarship" in q:
        codes = re.findall(r"(cs101|ai202|ds303)", q)
        if len(codes) >= 2:
            total = sum(COURSE_FEES[c.upper()] for c in codes[:2])
            return f"Rs.{total * 0.9:,.0f}"

    # Q3: Compare two courses
    if "more expensive" in q:
        codes = re.findall(r"(cs101|ai202|ds303)", q)
        if len(codes) >= 2:
            a = COURSE_FEES[codes[0].upper()]
            b = COURSE_FEES[codes[1].upper()]
            if a > b:
                return f"Yes, by Rs.{a-b:,}"
            else:
                return f"No, by Rs.{b-a:,}"

    # Q4
    if "welcome" in q:
        return "Welcome to the course!\nWishing you a great learning journey."

    return "I don't understand the question."


for question in QUESTIONS:
    print("\nQ:", question)
    print("A:", answer(question))