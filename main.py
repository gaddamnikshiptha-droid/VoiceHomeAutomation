import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

light = False
fan = False
ac = False

r = sr.Recognizer()

while True:

    with sr.Microphone() as source:
        print("\nSay a command...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()

        print("You said:", command)

        if "light on" in command:
            light = True
            engine.say("Light turned on")

        elif "light off" in command:
            light = False
            engine.say("Light turned off")

        elif "fan on" in command:
            fan = True
            engine.say("Fan turned on")

        elif "fan off" in command:
            fan = False
            engine.say("Fan turned off")

        elif "ac on" in command:
            ac = True
            engine.say("Air conditioner turned on")

        elif "ac off" in command:
            ac = False
            engine.say("Air conditioner turned off")

        elif "status" in command:
            engine.say("Reporting status")

        elif "exit" in command:
            engine.say("Goodbye")
            engine.runAndWait()
            break

        print("💡 Light:", "ON" if light else "OFF")
        print("🌬 Fan :", "ON" if fan else "OFF")
        print("❄ AC   :", "ON" if ac else "OFF")

        engine.runAndWait()

    except:
        print("Could not understand")