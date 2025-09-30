from openai import OpenAI
import json

# this project will give you an error about the json loads and stuff sometimes, so better try to use the openAI's models.

client = OpenAI(
    # keep in mind to add an API key here!...
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)



SYSTEM_PROMPT = """

You are an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also make use of tool if required from the set of available tool.
For every tool call wait for the Observe step which is the output from the called tool.

Rules:
- Strictly follow given JSON output format.
- Only run one step at a time.
- The sequence of step is START - (where the user gives an input), PLAN - (that can be a multiple times) and finally OUTPUT which is going to be displayed to the user.

OUTPUT JSON Format:
{'step': 'START' | 'PLAN' | 'OUTPUT' | 'TOOL', 'content': "string", "input":"string" }

Available Tools:
- get_weather(city:string): Takes city name as an input string and returns the weather information about the city

Example 1:
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



message_history = [{"role":"system", "content":SYSTEM_PROMPT}]


user_query = input("👤: ")
message_history.append({"role":"user","content":user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role":"assistant", "content":raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥",parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "PLAN":
        print("🧠",parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break


  