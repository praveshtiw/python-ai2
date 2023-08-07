import speech_recognition as sr

# Create a speech recognition object
recognizer = sr.Recognizer()

# Open the microphone and start listening
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
    while True:
        try:
            audio_data = recognizer.listen(source, timeout=5)  # Listen for audio input with a timeout of 5 seconds

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)

            print("You said:", text)

        except sr.WaitTimeoutError:
            print("Listening timeout. Say something...")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Error occurred while calling the API: {e}")
