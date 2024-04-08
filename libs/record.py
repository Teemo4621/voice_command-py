from io import BytesIO
import gtts
import keyboard
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import subprocess

class Speech_recognition:
    def __init__(self, prefix: str = None, keybind: str = None ,language: str = "th-TH"):
        self.prefix = prefix
        self.keybind = keybind
        self.language = language
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.audio = None
        self.sp_text = None
        self.qury = None
        self.speech_data = []
    
    def AddSpeechData(self, data: object, text: str, command: str):
        self.speech_data.append({"data": data, "text": text, "command": command})

    def Recording(self):
        print("listening...")
        try:
            with self.mic as mic:
                self.audio = self.recognizer.listen(mic)
            sp_text = str(self.recognizer.recognize_google(self.audio, language=self.language))
            if self.prefix is not None or self.keybind is not None:
                if not self.keybind:
                    if not self.prefix in sp_text:
                        return ValueError("Prefix not found")
                    else: self.qury = sp_text.split(self.prefix)[1].replace(" ", "") if self.prefix else sp_text.replace(" ", "")
                else:
                    keyboard.wait(self.keybind)
                    self.qury = sp_text.split(self.prefix)[1].replace(" ", "") if self.prefix else sp_text.replace(" ", "")
            else:
                self.qury = sp_text.split(self.prefix)[1].replace(" ", "") if self.prefix else sp_text.replace(" ", "")
            return str(self.qury)
        except: return str("")

    def __runCommand__(self):
        try:
            if self.speech_data:
                for get_data in self.speech_data:
                    for text in get_data["data"]:
                        if text in self.qury:
                            self.sp_text = get_data["text"]
                            subprocess.call(get_data["command"], shell=True)
                            return
                    else:
                        self.sp_text = "ฉันไม่รู้ต้องทำอะไร จากคำถามของคุณ prefix จะมีดังนี้ " + ",".join([i for i in get_data['data']])
                        print(get_data['data'])
            else:
                self.sp_text = "ฉันไม่รู้ต้องทำอะไร จากคำถามของคุณ กรุณาเพิ่มคำสั่งลงไปใน AddSpeechData"
        except Exception as err:
            print("An error occurred while running the command:", err)
            self.sp_text = ""
    
    def Start(self):
        self.__runCommand__()
        try:
            mp3_fp = BytesIO()
            tts = gtts.gTTS(self.sp_text, lang="th")
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            
            audio_segment = AudioSegment.from_mp3(mp3_fp)
            play(audio_segment)
            return self.sp_text
        except Exception as err:
            return err