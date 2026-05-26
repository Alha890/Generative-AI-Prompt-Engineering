#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install groq')

import time
from groq import Groq

client = Groq(
    api_key="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"
)

models = [
    "llama3-8b-8192",
    "llama3-70b-8192"
]

def compare_models(prompt, models):

    results = []

    print("\n" + "=" * 80)
    print("PROMPT")
    print("=" * 80)
    print(prompt)

    for model_name in models:

        start_time = time.time()

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=500
        )

        end_time = time.time()

        output = response.choices[0].message.content

        response_time = round(end_time - start_time, 2)

        output_length = len(output)

        results.append({
            "model": model_name,
            "time": response_time,
            "length": output_length,
            "output": output
        })

    print("\n" + "=" * 80)
    print("MODEL COMPARISON")
    print("=" * 80)

    for result in results:

        print(f"\nModel: {result['model']}")
        print(f"Response Time: {result['time']} seconds")
        print(f"Output Length: {result['length']} characters")

        print("\nOutput:\n")
        print(result["output"])

        print("\n" + "-" * 80)


complex_prompt = """
A farmer has 17 sheep.
All but 9 die.
How many sheep are left?
Explain your reasoning step by step.
"""

simple_prompt = "What is the capital of Japan?"

compare_models(complex_prompt, models)

compare_models(simple_prompt, models)

print("\n" + "=" * 80)
print("OBSERVATIONS")
print("=" * 80)

print("""
1. llama3-8b-8192 is faster and suitable for simple factual questions.

2. llama3-70b-8192 usually gives more detailed and accurate reasoning
   for complex problems.

3. The 70B model is worth using when:
   - solving difficult reasoning tasks
   - generating detailed explanations
   - handling coding/debugging tasks

4. The 8B model is better when:
   - speed is important
   - the task is simple
   - lower latency is preferred

5. For factual questions, the quality difference is usually small,
   so the faster 8B model is often enough.
""")


# In[ ]:




