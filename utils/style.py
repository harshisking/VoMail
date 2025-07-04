import colorama
import os
import core.contacts as conts
colorama.init(autoreset=True)


def banner():
    os.system("clear" if os.name == 'posix' else "cls")
    print(colorama.Fore.CYAN + '='*46)
    print("🎤",colorama.Fore.GREEN + "VoMail: Voice Mail".center(40),"🎤")
    print(colorama.Fore.CYAN + '='*46)


def show_contact(alias:str):
    contact = conts.get_contact(alias)
    print(contact)

def main():
    banner()
    show_contact("vomail")

if __name__=="__main__":
    main()


__all__ = ['banner','show_contact']