import speech_recognition as sr #for human speak and interaction
import time   #to get time
from win32com.client import Dispatch #to make computer speak
import os   #to find files
from playsound import playsound  #to play audio files
import vlc  #to play video files
import webbrowser  #to explore web


say=Dispatch("SAPI.SpVoice")
r1=sr.Recognizer()
r2=sr.Recognizer()



while True:
        say.Speak(f"hey  imran  what   are    you    looking    for")
        with sr.Microphone() as source:
            print("speak now: \ntime \nexit \nmovies \npaint \nnotepad \nplay \ngoogle")
            audio=r1.listen(source)
        

        try:
                print(r1.recognize_google(audio))
                text=r1.recognize_google(audio).split(" ")
                for i in text:
                    if i=="time":
                        local=time.ctime()
                        say.speak(f"well today is {local}")
                        print(f"well today is {local}")
                    elif i=="exit":
                        say.speak("nice to meet you see you soon bye ")
                        print("nice to meet you see you soon bye ")
                        exit()
                        
                    elif i=="movies":
                        say.speak("there is a list of movie available in your laptop \ndecide it within 30 seconds")
                        for index in os.listdir("E:/download"):
                            print(index)
                        time.sleep(3)
                        say.speak("so which movie you want to watch?")
                        with sr.Microphone() as source:
                                print("say now:")
                                audio2=r2.listen(source)
                        print(r2.recognize_google(audio2))
                        text2=r2.recognize_google(audio2).split(" ")
                        for j in text2:
                                if j=="underwater":
                                        say.speak("playing underwater for you")
                                        media=vlc.MediaPlayer(r"E:\download\Underwater (2020) [720p] [BluRay] [YTS.MX]\Underwater.2020.720p.BluRay.x264.AAC-[YTS.MX].mp4")
                                        media.set_fullscreen(1200)
                                        media.play()
                                elif j=="Jumanji":
                                        say.speak("playing jumanji the next level  for you")
                                        media=vlc.MediaPlayer(r"E:\download\Jumanji The Next Level (2019) [720p] [WEBRip] [YTS.MX]\Jumanji.The.Next.Level.2019.720p.WEBRip.x264.AAC-[YTS.MX].mp4")
                                        media.set_fullscreen(1200)
                                        media.play()
                                        
                        
                    elif i=="play":
                        playsound("Machayenge - Emiway Bantai 128 Kbps.mp3")
                        
                    elif i=="Notepad":
                        say.speak("opening notepad for you")
                        os.system("notepad")
                        
                    elif i=="Paint":
                        say.speak("opening paint for you")
                        os.system("mspaint")
                        
                    elif i=="Google":
                        say.speak("operning google for you")
                        webbrowser.open("www.google.com")
                        say.speak("Search anything goodbye")
                    elif i=="today":
                            say.speak("Today is an auspicios day of Eed, wishing you and your family eed mubarak")

        except:
                print("Error")
                say.speak("sorry couldn't recognize your voice")


                        
