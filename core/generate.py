import ollama

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
    print(email_gen(prompt))


if __name__=="__main__":
    main()

__all__ = ['email_gen']