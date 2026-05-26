#!/usr/bin/env python
# coding: utf-8

# In[2]:


from groq import Groq
import time

client = Groq(api_key="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")

print("Generating poem with typing effect...\n")

start_time = time.time()

tokens = []

stream = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Write a short 4-line poem about the moon."
        }
    ],
    temperature=0.7,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        token = chunk.choices[0].delta.content

        print(token, end="", flush=True)

        tokens.append(token)

        time.sleep(0.02)

end_time = time.time()

print("\n")

full_response = "".join(tokens)

generation_time = end_time - start_time

total_tokens = len(tokens)

tokens_per_second = total_tokens / generation_time

print("=" * 60)
print("Full Response:\n")
print(full_response)

print("\nGeneration Time:", round(generation_time, 2), "seconds")
print("Total Tokens Received:", total_tokens)
print("Tokens Per Second:", round(tokens_per_second, 2))


# In[ ]:




