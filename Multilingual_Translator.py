from tkinter import *
from gtts import gTTS
import playsound
import os
from googletrans import Translator
import speech_recognition as sr

text6 = "albanian : sq ,arabic: ar, armenian: hy, azerbaijani: az, belarusian: be, bengali: bn, bosnian: bs, bulgarian: bg," \
        "catalan: ca ,chinese(simplified): zh - cn ,chinese(traditional): zh - tw ,croatian: hr ,czech: cs, danish: da," \
        "dutch: nl, english: en, esperanto: eoestonian: et ,filipino: tl, finnish: fi ,french: fr ,georgian: ka ,german: de," \
        "greek: el, gujarati: gu ,creole: ht ,hawaiian: haw ,hebrew: he ,hindi: hi ,hungarian: hu ,icelandic: is ,indonesian: " \
        "id ,irish: ga ,italian: it ,japanese: ja ,javanese: jw ,kannada: kn ,korean: ko ,kurdish(kurmanji): ku ,lao: lo ," \
        "latin: la ,latvian: lv ,lithuanian: lt ,luxembourgish: lb ,macedonian: mk ,malay: ms ,malayalam: ml ,marathi: mr ," \
        "mongolian: mn ,myanmar(burmese): my ,nepali: ne ,norwegian: no ,odia: or ,pashto: ps ,persian: fa, polish: pl ," \
        "portuguese: pt, punjabi: pa, romanian: ro ,russian: ru ,gaelic: gd ,serbian: sr ,shona: sn ,sindhi: sd, sinhala: si ," \
        "slovak: sk ,spanish: es ,swedish: sv ,tajik: tg ,tamil: ta ,telugu: te ,thai: th ,turkish: tr ,ukrainian: uk ," \
        "urdu: ur ,uzbek: uz ,vietnamese: vi ,welsh: cy ,yiddish: yi ,zulu: zu  "


# using googletrans (LANGCODES, LANGUAGES) to Find the language list


def transapp(Sampletext, lang_dest):
    translator = Translator()  # creating a object of class translator
    try:
        translation = translator.translate(Sampletext, dest=lang_dest)  # using translate method of class translator
        return translation.text
    except Exception as e:
        print(e)
        exit(1)


def speech_text():
    r = sr.Recognizer()  # Creates a new Recognizer instance
    with sr.Microphone() as Mic:  # using mic as a audio source with instance of Microphone
        print("Speak Anything :")
        try:
            audio = r.listen(Mic, timeout=3, phrase_time_limit=15)  # recording audio with Mic as source
            text = r.recognize_google(audio, language=speak_lang.get())  # convert audio file to text using google API
            text2 = transapp(text, lang_translate.get())
            label4 = Message(root, text=text2, padx=10, pady=10, aspect=200).grid(row=2, column=1)
            text_speech(text2, lang_translate.get())  # calling text to speech
        except Exception as e:
            print(e)
            exit(1)


def text_speech(text, lang):
    language = lang
    try:
        output = gTTS(text=text, lang=language, slow=False)  # using GTTS API to Convert back text to audio
        output.save("output.mp3")  # Saving file in current Directory
        playsound.playsound('output.mp3')  # playing sound in Background
        os.remove("output.mp3")
    except:
        print("Sorry, Language Not supported in Voice module !!!")


def TextTranslate():
    textin = input_text.get()
    lang_dest = lang_translate.get()
    try:
        translator = Translator()
        lang1 = translator.detect(textin)  # Using detect Method To Detect text Language
    except Exception as e:
        print("Not Recognisable Language")
    translated_text = transapp(textin, lang_dest)
    label2 = Message(root, text=translated_text, padx=10, pady=10, aspect=200, font=10).grid(row=2, column=1)
    text_speech(translated_text, lang_dest)  # calling text to speech


def langchooser():
    top = Toplevel()  # Creating a New Window Popup
    top.title('Choose Language in which You want To Translate')
    #top.iconbitmap('icons8-translate-app-48.ico')
    top.geometry('680x400')
    langlabel = Message(top, text=text6, padx=5, pady=5, aspect=200, font=(15)).grid(row=0, column=0)


root = Tk()  # creating main(root) Window of the Tkinter class using tk widget
root.title('Multilingual Translator')  # title
#root.iconbitmap('icons8-translate-app-48.ico')  # icon
root.geometry('512x360')  # Width * height of main window
input_text = StringVar()  # creating a instance of class StringVar
input_text.set("")
lang_translate = StringVar()  # creating a instance of class StringVar
lang_translate.set("")
speak_lang = StringVar()  # creating a instance of class StringVar
speak_lang.set("")
label1 = Label(root, text="Enter Text in any Language : ", pady=10).grid(row=1, column=0)  # label widget (static text)
textin = Entry(root, textvar=input_text, width=50, bd=2).grid(row=2, column=0)  # input widget
button2 = Button(root, text="Language Codes", command=langchooser).grid(row=10, column=0, pady=5)  # Button widget
label5 = Label(root, text="Enter the language code to Translate : ", padx=5, pady=10).grid(row=4, column=0)
lang_dest = Entry(root, textvar=lang_translate, width=5, bd=2).grid(row=5, column=0)
button1 = Button(root, text="Text Translate", command=TextTranslate).grid(row=6, column=0, pady=5)
label6 = Label(root, text="Enter the language code To Speak in  : ", padx=5, pady=10).grid(row=7, column=0)
ls = Entry(root, textvar=speak_lang, width=5, bd=2).grid(row=8, column=0)
label3 = Label(root, text="Translated Text", padx=10, pady=10).grid(row=1, column=1)
button3 = Button(root, text="Voice Translate", command=speech_text).grid(row=9, column=0, pady=5)
root.mainloop()  # This method will loop forever, waiting for events from the user, until the user exits the program
