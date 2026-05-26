#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install tiktoken')


# In[5]:


import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

samples = {
    "English Sentence": "Artificial Intelligence is changing the world.",

    "Python Function": """
def add(a, b):
    return a + b
""",

    "Native Language Sentence": "എനിക്ക് പ്രോഗ്രാമിംഗ് വളരെ ഇഷ്ടമാണ്",

    "Number": "1234567",

    "Email Address": "example123@gmail.com",

    "Math Notation": "f(x) = x^2 + 3x - 5"
}

for title, text in samples.items():
    tokens = enc.encode(text)
    token_strings = [enc.decode([token]) for token in tokens]

    print("=" * 50)
    print(title)
    print("Input:", text)
    print("Tokens:", token_strings)
    print("Token Count:", len(tokens))
    print()

print("Explanation:")
print("1. Numbers like 1234567 are grouped into larger chunks instead of single digits.")
print("2. Malayalam text produces more tokens because the tokenizer splits many characters separately.")


# In[ ]:




