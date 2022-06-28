import speech_recognition as sr
from gtts import gTTS
from tkinter import *
import playsound
from googletrans import Translator
import googletrans
import time


def Chooselang():
    lang_code = {'albanian': 'sq', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'belarusian': 'be',
                 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'chinese (simplified)': 'zh-cn',
                 'chinese (traditional)': 'zh-tw', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl',
                 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi',
                 'french': 'fr', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu',
                 'haitian creole': 'ht', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hungarian': 'hu',
                 'icelandic': 'is', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
                 'javanese': 'jw', 'kannada': 'kn', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'lao': 'lo',
                 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk',
                 'malay': 'ms', 'malayalam': 'ml', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my',
                 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl',
                 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'scots gaelic': 'gd',
                 'serbian': 'sr', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'spanish': 'es',
                 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr',
                 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'yiddish': 'yi',
                 'zulu': 'zu'}
    # using googletrans (LANGCODES, LANGUAGES) to Find the language list
    for lang, code in lang_code.items():
        print(f"{lang} : {code}")


def langdetect(text):
    translator = Translator()  # creating a object of class translator
    lang1 = translator.detect(text)  # Using detect Method To Detect text Language
    return (lang1.lang)  # lang1 is a dictionary with 2 keys lang,confidence


def transapp(Sampletext, lang_dest):
    translator = Translator()  # creating a object of class translator
    try:
        translation = translator.translate(Sampletext, dest=lang_dest)  # using translate method of class translator
        return translation.text
    except Exception as e:
        print(e)
        exit(1)


def speech_text(lang_src):
    r = sr.Recognizer() # Creates a new Recognizer instance
    with sr.Microphone() as Mic:  # using mic as a audio source with instance of Microphone
        print("Speak Anything :")
        try:
            audio = r.listen(Mic, timeout=3, phrase_time_limit=15)  # recording audio with Mic as source
            text = r.recognize_google(audio, language=lang_src)  # convert audio file to text using google API
            return text
        except Exception as e:
            print(e)
            exit(1)


def text_speech(text, lang):
    language = lang
    try:
        output = gTTS(text=text, lang=language, slow=False)  # using GTTS API to Convert back text to audio
        output.save("output.mp3")  # Saving file in current Directory
        playsound.playsound('output.mp3')  # playing sound in Background
        print('...')
    except:
        print("Sorry, Language Not supported in Voice module !!!")


choice = 4

while (choice != 3):
    print("Choose Any one option : ")
    print("1)Text To Voice and Text ")
    print("2)Voice to Text and  Voice ")
    print("3)Exit The App")
    choice = int(input())

    if (choice == 1):
        textin = input("Enter Text in any Language : ")
        try:
            lang_src = langdetect(textin)
        except:
            print("Not Recognisable Language")
        print("Choose Language in which You want To Translate")
        time.sleep(2)  # It will pause the Program For 2 seconds
        Chooselang()  # Display a List of Languages and Codes
        lang_dest = input("Enter the language code : ")
        translated_text = transapp(textin, lang_dest)
        text_speech(translated_text, lang_dest)
        try:
            root = Tk()  # creating main(root) Window of the Tkinter class using tk widget
            root.title('Multilingual Translator')  # title
            root.iconbitmap('icons8-translate-app-48.ico')  #icon
            root.geometry('400x200')  # Width * height of main window
            label1 = Label(root, text='Original Text (' + googletrans.LANGUAGES.get(lang_src).capitalize() + ')',
                           padx=5,
                           pady=5).grid(row=0, column=0)
            label2 = Label(root, text='Translated Text(' + googletrans.LANGUAGES.get(lang_dest).capitalize() + ')',
                           padx=5,
                           pady=5).grid(row=0, column=1)
            label3 = Message(root, text=textin, padx=5, pady=5, aspect=200).grid(row=1, column=0)
            label4 = Message(root, text=translated_text.capitalize(), padx=5, pady=5, aspect=200).grid(row=1, column=1)
            root.attributes('-topmost', True)
            root.mainloop()  # This method will loop forever, waiting for events from the user, until the user exits the program
        except Exception as e:
            print(e)
    elif (choice == 2):
        print("Choose Language in which You will Speak and in which you want to Translate")
        time.sleep(2)  # It will pause the Program For 2 seconds
        Chooselang()  # Display a List of Languages and Codes
        lang_src = input("Enter the Lang code For Speaking: ")
        lang_dest = input("Enter the Lang code For Translation : ")
        try:
            textin = speech_text(lang_src)

        except Exception as e:
            print(e)
            exit(1)
        translated_text = transapp(textin, lang_dest)
        text_speech(translated_text, lang_dest)
        try:
            root = Tk()
            root.title('Multilingual Translator')
            root.iconbitmap('icons8-translate-app-48.ico')
            root.geometry('400x200')
            label1 = Label(root, text='Original Text (' + googletrans.LANGUAGES.get(lang_src).capitalize() + ')',
                           padx=5,
                           pady=5).grid(row=0, column=0)
            label2 = Label(root, text='Translated Text(' + googletrans.LANGUAGES.get(lang_dest).capitalize() + ')',
                           padx=5,
                           pady=5).grid(row=0, column=1)
            label3 = Message(root, text=textin, padx=5, pady=5, aspect=200).grid(row=1, column=0)
            label4 = Message(root, text=translated_text.capitalize(), padx=5, pady=5, aspect=200).grid(row=1, column=1)
            root.attributes('-topmost', True)
            root.mainloop()
        except Exception as e:
            print(e)
    else:
        print(print("Enter correct choice"))
