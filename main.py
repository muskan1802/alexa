# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes
#
# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# # engine.say("I am your Alexa")
# # engine.say("What can i do for you")
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
#
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("listening....")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 command=command.replace('alexa','')
#                 print(command)
#     except:
#         pass
#     return command
#
# def run_alexa():
#     command = take_command()
#     print(command)
#     if 'play' in command:
#         song = command.replace('play','')
#         talk('playing'+song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         talk('Current time is' + time)
#         print(time)
#     elif 'who' in command:
#         wiki = command.replace('who is','')
#         info = wikipedia.summary(wiki,1)
#         print(info)
#         talk(info)
#     elif 'joke' in command:
#         j = talk(pyjokes.get_joke())
#     else:
#         talk('I dont understand that can you please repeat')
#
# while True:
#     run_alexa()
#
#
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.say("I am your Alexa")
# engine.say("What can i do for you")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")

    assname = ("Jarvis 1 point o")
    talk("I am your Assistant")
    talk(assname)

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#
#     # Enable low security in gmail
#     server.login('your email id', 'your email password')
#     server.sendmail('your email id', to, content)
#     server.close()
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
        talk("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    # elif 'email to gaurav' in command:
    #     try:
    #         talk("What should I say?")
    #         content = take_command()
    #         to = "Receiver email address"
    #         sendEmail(to, content)
    #         talk("Email has been sent !")
    #     except Exception as e:
    #         print(e)
    #         talk("I am not able to send this email")
    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")

    elif 'fine' in command or "good" in command:
        talk("It's good to know that your fine")

    elif "change my name to" in command:
        query = command.replace("change my name to", "")
        assname = query

    elif "change name" in command:
        talk("What would you like to call me, Sir ")
        assname = take_command()
        talk("Thanks for naming me")

    elif "what's your name" in command or "What is your name" in command:
        talk("My friends call me")
        talk("Jarvis 1 point o")
        print("My friends call me", "Jarvis 1 point o")

    elif 'exit' in command or 'bye' in command:
        talk("Thanks for giving me your time")
        exit()

    elif "who made you" in command or "who created you" in command:
        talk("I have been created by Muskan.")
    else:
        talk('Please say the command again.')

wishMe()
while True:
    run_alexa()