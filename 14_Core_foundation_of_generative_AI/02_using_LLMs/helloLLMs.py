# This file will hold all the knowledge about zero-shot prompting technique, one-shot prompting technique and few shot prompting technique.
# This file is more focused on COT prompting technique.
# manual COT for appending the history to the model...

from google import genai

client = genai.Client(
    api_key="AIzaSyCKq5Xz50-MRen6CtfmsKwXdyo7K1mngwA"
)

SYSTEM_PROMPT = """

You are an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow given JSON output format.
- Only run one step at a time.
- The sequence of step is START - (where the user gives an input), PLAN - (that can be a multiple times) and finally OUTPUT which is going to be displayed to the user.

OUTPUT JSON Format:
{'step': 'START' | 'PLAN' | 'OUTPUT', 'content': "string" }

Example:
START : Hey, can you solve 2 + 3 * 5 / 10
PLAN : {'step':"PLAN", "content":"Seems like user is interested in math problem"} 
PLAN : {'step':"PLAN", "content":"looking at the problem, we should we should solve it using BODMAS Rule"} 
PLAN : {'step':"PLAN", "content":"Yes, BODMAS is the correct rule to solve this problem"} 
PLAN : {'step':"PLAN", "content":"First we must multiply 3*5 which is 15"} 
PLAN : {'step':"PLAN", "content":"Now the new equation is 2+15/10"} 
PLAN : {'step':"PLAN", "content":"Now the new equation is 15/10 = 1.5"} 
PLAN : {'step':"PLAN", "content":"Now the new equation is 2 + 1.5"} 
PLAN : {'step':"PLAN", "content":"Now lets finally add the numbers"} 
PLAN : {'step':"PLAN", "content":"Great! we have solved and finally the answer is : 3.5"} 
PLAN : {'step':"OUTPUT", "content":"3.5"} 


"""

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Hey, write a code in JS to add n"
)

print(response.text)
