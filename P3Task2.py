#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install groq tiktoken pandas')

from groq import Groq
import tiktoken
import pandas as pd
import time

client = Groq(
    api_key="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"
)

encoding = tiktoken.get_encoding("cl100k_base")

python_code = """
def student_grade_report(students):

    total_marks = 0

    for student in students:

        marks = sum(student["marks"])
        average = marks / len(student["marks"])

        if average >= 90:
            grade = "A"

        elif average >= 75:
            grade = "B"

        elif average >= 50:
            grade = "C"

        else:
            grade = "Fail"

        print(f"Name: {student['name']}")
        print(f"Total Marks: {marks}")
        print(f"Average: {average}")
        print(f"Grade: {grade}")
        print("-" * 30)

        total_marks += average

    class_average = total_marks / len(students)

    print(f"Class Average: {class_average}")
"""

zero_shot_prompt = f"""
Review the following Python code and suggest improvements:

{python_code}
"""

few_shot_prompt = f"""
Example:

Code:
def add(a,b):
 return a+b

Review:
- Add spaces after commas.
- Add proper formatting.
- Use a docstring.

Now review this code:

{python_code}
"""

cot_prompt = f"""
Review the following Python code step-by-step.

1. Check for bugs.
2. Check readability and style.
3. Check security or robustness issues.
4. Suggest improvements.

Code:

{python_code}
"""

prompts = {
    "Zero-Shot": zero_shot_prompt,
    "Few-Shot": few_shot_prompt,
    "Chain-of-Thought": cot_prompt
}

results = []

for prompt_type, prompt_text in prompts.items():

    input_tokens = len(encoding.encode(prompt_text))

    start_time = time.time()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        temperature=0.5,
        max_tokens=500
    )

    end_time = time.time()

    output_text = response.choices[0].message.content

    response_time = end_time - start_time

    output_length = len(output_text)

    results.append({
        "prompt_type": prompt_type,
        "input_tokens": input_tokens,
        "response_time": round(response_time, 2),
        "output_length": output_length
    })

df = pd.DataFrame(results)

print("\nPROMPT COMPARISON TABLE\n")
print(df.to_string(index=False))

