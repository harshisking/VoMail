import core.contacts as conts
import core.speech as sp
import core.ai as gen
import core.send as sen

def main():
    while True:
        command = sp.get_command()
        json_data = gen.command_parser("send an email to vomail, my client saying that my flight is 2 hours late")        
        if json_data['action'] == 'send_email':
            # recievers_email = conts.get_contact(json_data['alias'])[2]
            draft = gen.email_gen(json_data['prompt'], json_data['alias'])
            print(draft)
            pause()




def pause():
    _ = input("press any key to go forth: ")


if __name__=="__main__":
    main()