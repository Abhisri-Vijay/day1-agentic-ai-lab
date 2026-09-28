from agent import ask_agent

QUESTION = """
Compare these two options:

1. Take CS101 and AI202 with a 10% scholarship.
2. Take CS101, AI202, and DS303 with a 25% scholarship.

Which option is cheaper, and by how much?
"""

answer = ask_agent(QUESTION, max_steps=8)

print("\nFINAL ANSWER:")
print(answer)