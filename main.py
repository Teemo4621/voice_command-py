from libs.record import Speech_recognition

def main():
    sp_system = Speech_recognition()
    
    # voice recording
    text = sp_system.Recording()
    
    # basic data commandP
    data = ["ช่วยค้นหา", "ค้นหา", "ช่วย", "ขอวฺิธี", "วิธี"]
    
    for word in data:
        if word in text:
            text = text.replace(word, "")
            break
    
    text_res = "ได้คับนี่คือผลลัพของข้อมูลที่คุณตามหา"
    command = f"start www.google.com/search?q={text}"

    sp_system.AddSpeechData(data, text_res, command)
    
    # start
    sp_system.Start()
    
    # show response speech text
    print("Recognized Text:", text)
    
if __name__ == "__main__":
    main()
