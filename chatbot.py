from openai import OpenAI
from config import BASE_URL, API_KEY, MODEL, QUESTIONS

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

for question in QUESTIONS:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("\nQ:", question)
    print("A:", response.choices[0].message.content)