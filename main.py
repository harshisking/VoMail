import core.contacts as conts
import core.speech as sp
import core.ai as gen
import core.send as sen

def main():
    while True:
        command = sp.get_command() # Getting the command
        json_data = gen.command_parser(command) # Parsing the command        
        
        if json_data['action'] == 'send_email':  # if send mail then send mail
            recievers_email = conts.get_contact(json_data['alias'])[2]
            draft = gen.email_gen(json_data['prompt'], json_data['alias'])
            print(draft)
            print(recievers_email)
            
            
            # Checking whether the user likes it or not
            if confirm():
                sen.sender(recievers_email,draft, json_data['prompt'])
            else:
                pass

        elif json_data['action'] == 'fallback':
            
            if json_data['command'] == "add_contact":
                alias = input('Alias: ')
                email = input('Email: ')
                conts.add_contact(alias, email)
                pause()

            elif json_data['command'] == 'list_contacts':
                lis = conts.list_contacts()
                print(lis)
                pause()

            elif json_data['command']=='delete_contact' or json_data['command'] == 'remove contact':
                conts.remove_contact(json_data['alias'])
                pause()

            elif json_data['command']=='get_contact':
                contact = conts.get_contact(json_data['alias'])
                print(contact)
                pause()



def confirm():
    _ = input("yes or no: ")
    if _ == 'yes':
        return True
    else:
        return False


def pause():
    input("Press any key")


if __name__=="__main__":
    main()
