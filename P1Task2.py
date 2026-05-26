#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tiktoken
import pandas as pd

enc = tiktoken.get_encoding("cl100k_base")

def token_cost(text, price_per_million=0.10):
    tokens = enc.encode(text)
    token_count = len(tokens)
    cost = (token_count / 1_000_000) * price_per_million
    return token_count, cost

paragraph = "Artificial Intelligence is transforming industries and improving efficiency. " * 50

python_script = "\n".join([f"print('Line {i}')" for i in range(1, 51)])

conversation = """
User: Hello, how are you?
Assistant: I am doing well. How can I help you today?
User: Explain machine learning in simple terms.
"""

results = []

samples = {
    "300-word Paragraph": paragraph,
    "50-line Python Script": python_script,
    "3-turn Conversation": conversation
}

for name, text in samples.items():
    token_count, cost = token_cost(text)
    results.append([name, token_count, f"${cost:.8f}"])

df = pd.DataFrame(results, columns=["Input Type", "Token Count", "Estimated Cost"])

print(df.to_string(index=False))


# In[ ]:




