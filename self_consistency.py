from collections import Counter
from openai import OpenAI
from config import BASE_URL, API_KEY, MODEL
from cot_compare import QUESTIONS, COT_PROMPT


client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)


RUNS = 5
TEMPERATURE = 0

QUESTION = QUESTIONS[0]


def final_answer(text):
    for line in reversed(text.splitlines()):
        if "final answer" in line.lower():
            return line.split(":", 1)[-1].strip()

    return text.splitlines()[-1].strip() if text.strip() else "(empty)"


answers = []

for attempt in range(1, RUNS + 1):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": COT_PROMPT},
            {"role": "user", "content": QUESTION}
        ],
        temperature=TEMPERATURE
    )

    answer = final_answer(response.choices[0].message.content)

    print(f"run {attempt}: {answer}")
    answers.append(answer)


winner, count = Counter(answers).most_common(1)[0]

print(f"\nMajority answer ({count} of {len(answers)} runs): {winner}")