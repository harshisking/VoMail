import ollama
import json

def command_parser(command:str):
    sys_msg = """
You are a voice command interpreter for an email assistant app.
- If the user wants to send an email, return a JSON like:
  {
    "action": "send_email",
    "alias": "riya",
    "prompt": "apologize for delay in meeting"
  }
- If the command is not about sending email (like adding/removing a contact), return:
  {
    "action": "fallback",
    "command": "list contacts"
  }

Only return valid JSON. No explanation.
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

def email_gen(command:str):
    response = ollama.chat(
        model='mistral',
        messages=[
            {'role':'system', 'content':'Act a professional Email Writer. You have the knowledge of all types of Emails. Be precise about details and be short and professional'},
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