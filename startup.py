import pyttsx3

friend = pyttsx3.init()
friend.setProperty("rate", 178)
friend.say("Welcome Sir, the system is ready and running. The room temperature is at 27 Degrees. Have a Good day")
friend.runAndWait()