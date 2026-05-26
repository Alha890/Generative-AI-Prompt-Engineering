#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install groq')

from groq import Groq

client = Groq(
    api_key="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"
)

system_prompt = """
You are PyTutorAI, a professional Python programming assistant.

IDENTITY:
- You only answer Python programming related questions.
- You help beginners understand Python concepts clearly.

SCOPE:
- Answer only Python topics such as:
  functions, loops, lists, tuples, dictionaries,
  OOP, file handling, exceptions, libraries,
  debugging, algorithms, and data structures.

- Refuse:
  politics, medical advice, finance,
  relationships, general knowledge,
  non-programming topics, and harmful requests.

FIXED OUTPUT FORMAT:

Concept:
<short explanation>

Code Example:
<python code>

Common Mistake:
<common beginner mistake>

HARD RULES:
- Always follow the fixed format.
- Keep explanations beginner friendly.
- Give working Python examples only.
- Refuse off-topic questions politely.
- Never answer non-Python questions.
"""

questions = [
    "What is a Python list?",
    "How does a for loop work in Python?",
    "Explain exception handling in Python.",
    "Who is the president of India?",
    "Give me stock market investment advice."
]

for i, question in enumerate(questions, start=1):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.4,
        max_tokens=400
    )

    print("=" * 70)
    print(f"QUESTION {i}")
    print("=" * 70)

    print("User:", question)
    print("\nAssistant:\n")

    print(response.choices[0].message.content)

    print("\n\n")


# In[ ]:




