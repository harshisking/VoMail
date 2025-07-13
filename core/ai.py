import ollama
import json
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv("USERNAME")

def command_parser(command:str):
    print("Analyzing the command")
    sys_msg ="""
You are a voice command interpreter for an email assistant app.

If the user's command is about sending an email:
- Extract the recipient's alias or name (e.g., 'rahul', 'my client', 'dr. mehta').
- Extract the actual message they want to send.
- Respond with strictly valid JSON in this format (all lowercase keys):

{
  "action": "send_email",
  "alias": "rahul",
  "prompt": "i will be late for the meeting at 4 pm"
}

If the command is NOT about sending email (like adding, listing, deleting contacts, or getting a contact):
- Extract the alias (if available).
- Determine the intent from the phrase (e.g., add/remove/list/get contact).
- Respond with:

{
  "action": "fallback",
  "alias": "rahul",
  "command": "remove_contact"
}

Only respond with valid JSON. Do not explain anything. Do not include extra text.
"""


    response = ollama.chat(
        model='mistral',
        messages=[
            {'role':'system', 'content':sys_msg},
            {'role':'user','content':command}
        ]
    )
    try:
        parsed = json.loads(response['message']['content'])
        return parsed
    except json.JSONDecodeError:
        print("Please Try Again")
        return {'action':'fallback','command':command}

def email_gen(prompt:str, alias:str):
    print("Generating Email")
    sys_msg = f"""You are a professional email writer acting on behalf of the user.

- The user is an individual (not a company).
- Write a short, respectful, professional email based on the user's prompt.
- The recipient is: {alias}
- Do not assume anything not mentioned.
- Focus on clarity, correct tone, and brevity.
- The users name is {username}"""

    response = ollama.chat(
        model='mistral',
        messages=[
            {'role':'system', 'content':sys_msg},
            {'role':'user', 'content':prompt}
        ]
    )
    email_txt = response['message']['content']
    return email_txt


def main():
    prompt = input("INPUT: ")
    json_data = command_parser(prompt)
    print(json_data)


if __name__=="__main__":
    main()

__all__ = ['email_gen','command_parser']