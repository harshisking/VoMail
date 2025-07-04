import speech_recognition as sr
import os


os.environ["PYTHONWARNINGS"] = "ignore"

recognizer = sr.Recognizer()

def get_command():
    try:
        # source as microphone
        with sr.Microphone() as source:
            os.system("clear" if os.name == 'posix' else "cls")
            print("Listening.....")
            recognizer.adjust_for_ambient_noise(source, duration=1) # reducing ambient noises

            #getting the command and converting it to text using google free API
            audio = recognizer.listen(source,timeout=5,phrase_time_limit=10)  # creating time limit if getting ideal
            command = recognizer.recognize_google(audio)
            
            # returning simple string with no extra spaces
            return command.lower().strip()
        

    except sr.UnknownValueError as e:
        print("Error:", e)
        return None
    
    except sr.RequestError as e:
        print("Error:", e)
        return None

    except Exception as e:
        print("Error:",e)
        return None
    
def main():
    command = get_command()
    print(command)


if __name__=="__main__":
    main()

__all__ = ["get_command"]