#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def estimate_context_usage(messages_list, model_limit=8192):
    total_tokens = 0

    for message in messages_list:
        content = message["content"]
        tokens = enc.encode(content)
        total_tokens += len(tokens)

    print(f"Total Tokens Used: {total_tokens}")
    print(f"Model Limit: {model_limit}")

    usage_percent = (total_tokens / model_limit) * 100
    print(f"Usage: {usage_percent:.2f}%")

    if usage_percent > 80:
        print("WARNING: Context usage exceeded 80% of the model limit!")

messages = []

large_text = "Artificial Intelligence is transforming industries. " * 300

for i in range(10):
    messages.append({
        "role": "user",
        "content": large_text
    })

estimate_context_usage(messages)


# In[ ]:




