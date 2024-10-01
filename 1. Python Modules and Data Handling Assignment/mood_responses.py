# mood responses module
def mood_response(mood):
    mood = mood.lower()
    mood = mood.strip()
    if mood == "happy":
        return "Great!"
    elif mood == "frustrated" or mood == "mad" or mood == "angry":
        return "Sorry."
    elif mood == "scared" or mood == "afraid" or mood == "stressed" or mood == "nervous" or mood == "anxious":
        return "Take a deep breath."
    elif mood == "horny":
        return "BONK"
    elif mood == "depressed" or mood == "sad":
        return "Eat some ice cream!"
    elif mood == "tired" or mood == "sleepy" or mood == "exhausted":
        return "Go for a walk?"
    elif mood == "bored":
        return "My brother made a really cool game at hue-man.app, you can play it if you want."
    elif mood == "excited":
        return "If only I could ask you what you're excited for..."
    elif mood == "calm":
        return "Nice."
    elif mood == "guilty":
        return "Objection!"
    elif mood == "hungry":
        return "Get a healthy snack!"
    else:
        return "I don't have a response for that one. Sorry."