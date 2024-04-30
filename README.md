# Voice Run Command Py 🎙️
เป็นระบบเอาไว้ควบคุมการทำงานของคอมคุณด้วย เสียงสามารถปรับเเต่งเเละเเก้ไขได้อย่างอิสระ
รองรับภาษาไทยด้วยนะจ้ะะะะ

### ตัวอย่าง โค้ด 📜
main.py
```py
from libs.record import Speech_recognition

def main():
    sp_system = Speech_recognition()
    
    # voice recording
    text = sp_system.Recording()
    
    # basic data command
    data = ["ช่วยค้นหา", "ค้นหา", "ช่วย", "ขอวฺิธี", "วิธี"]
    
    for word in data:
        if word in text:
            text = text.replace(word, "")
            break
    
    text_res = "ได้คับนี่คือผลลัพของข้อมูลที่คุณตามหา"
    command = f"start www.google.com/search?q={text}"
    
    # add command to sp_system
    sp_system.AddSpeechData(data, text_res, command)
    
    # start
    sp_system.Start()
    
    # show response speech text
    print("Recognized Text:", text)
    
if __name__ == "__main__":
    main()
```
## About 🧐
ระบบนี้เป็นระบบที่ผมทำเอาไวรอระหว่างกำลังศึกษาเรื่อง python machine learning เพี่ยงเพราะอยากมี จาวิส เป็นของตัวเองงงงงงง 😭

## Install 💉
Staps 1 Install Python\
Staps 2 Clone my Project\
Steps 3 Click installer.bat\
Steps 4 python main.py\
enjoy

## Make With Love By 💖: ZEMONNUB
