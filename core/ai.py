import ollama
import json

def command_parser(command:str):
    sys_msg ="""
You are a voice command interpreter for an email assistant app.

If the command is about sending an email:
- Extract the recipient’s name or alias (e.g., 'Rahul', 'my client', 'Dr. Mehta').
- Extract the message the user wants to send.
- Return valid JSON like this (all lowercase keys):

{
  "action": "send_email",
  "alias": "rahul",
  "prompt": "i will be late for the meeting at 4 pm"
}

If the command is **not** about sending an email (e.g., add/remove/list contact), return:

{
  "action": "fallback",
  "command": "the full original command"
}

Strictly output only valid JSON. No extra text. No explanations.
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

def email_gen(command:str, alias:str):
    sys_msg = f"""You are a professional email writer acting on behalf of the user.

- The user is an individual (not a company).
- Write a short, respectful, professional email based on the user's prompt.
- The recipient is: {alias}
- Do not assume anything not mentioned.
- Focus on clarity, correct tone, and brevity."""

    response = ollama.chat(
        model='mistral',
        messages=[
            {'role':'system', 'content':sys_msg},
            {'role':'user', 'content':command}
        ]
    )
    email_txt = response['message']['content']
    return email_txt


def main():
    prompt = input("INPUT: ")
    print(command_parser(prompt))


if __name__=="__main__":
    main()

__all__ = ['email_gen','command_parser']