#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install groq')


# In[5]:


from groq import Groq

client = Groq(api_key="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")

messages = [
    {
        "role": "system",
        "content": "You are a helpful Python doubt-solver chatbot."
    }
]

turn = 0

while turn < 4:
    user_input = input("You: ")

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    print("\nBot:", assistant_reply)
    print()

    turn += 1

print("=" * 60)
print("Full Conversation History:\n")

for msg in messages:
    print(msg)


# In[ ]:




