import datetime

# 🎯 Decorator to log mood detection
def mood_logger(func):
    def wrapper(*args, **kwargs):
        print(f"\n[{datetime.datetime.now()}] Detecting mood...")
        result = func(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Done.\n")
        return result
    return wrapper

# 😊 Closure that returns a mood-response function
def mood_response_generator():
    moods = {
        "happy": "Great! Keep smiling 😄 and spread joy.",
        "sad": "Take a walk 🌳, talk to a friend, or listen to music 🎵.",
        "angry": "Breathe deeply 🧘‍♀️. Try journaling your feelings ✍️.",
        "tired": "Rest well 😴 and drink water 💧.",
        "excited": "Channel that energy into something creative! 🎨"
    }

    def get_response(mood):
        return moods.get(mood.lower(), "Hmm, not sure. Just be kind to yourself ❤️.")
    
    return get_response

# 🧠 Function that uses closure & decorator
@mood_logger
def detect_mood(response_func, name, mood):
    print(f"\n{name}, here's something for you:")
    print(response_func(mood))

# 🚀 Main interactive function
if __name__ == "__main__":
    print("💬 Welcome to Mood Detector!")
    name = input("👤 Enter your name: ")
    while True:
        mood = input(f"🧠 Hi {name}, how are you feeling today? (Type 'exit' to quit): ")
        if mood.lower() == 'exit':
            print("👋 Thank you for using Mood Detector. Take care!")
            break
        mood_func = mood_response_generator()
        detect_mood(mood_func, name, mood)
