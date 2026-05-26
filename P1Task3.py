#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install groq')


# In[13]:


from groq import Groq

client = Groq(api_key="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")

question = "What is Artificial Intelligence?"

temperatures = [0.1, 0.7, 1.5]

for temp in temperatures:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=temp
    )

    print("=" * 60)
    print(f"Temperature: {temp}")
    print(response.choices[0].message.content)
    print()

print("Comment:")
print("At temperature 0.1, the response is more focused and consistent.")
print("At temperature 0.7, the response becomes more natural and creative.")
print("At temperature 1.5, the response is highly creative and diverse.")


# In[ ]:




