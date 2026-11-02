# 🕵️ SENTIMENT SPY
from textblob import TextBlob  

history = []   # a list to remember every sentence and its mood

name = input("What is your name, Agent? ").strip() or "Mystery Agent"
print(f"\nWelcome, Agent {name}! Type a sentence and I'll spy on its feeling")
print("Commands: 'history' = see past results, 'exit' = quit\n")


def get_mood(score):
    #Turn the polarity score into a mood
    if score > 0.25:
        return "Positive 😊"
    elif score < -0.25:
        return "Negative 😞"
    else:
        return "Neutral 😐"


while True:    
    text = input(">> ").strip()

    if text.lower() == "exit":
        print(f"Goodbye, Agent {name}! 👋")
        break

    if text.lower() == "history":
        if not history:
            print("Nothing yet!")
        for number, (sentence, mood) in enumerate(history, start=1):
            print(f"{number}. {sentence} → {mood}")
        continue   # go back and ask again

    if text == "":
        print("Please type something!")
        continue

    score = TextBlob(text).sentiment.polarity   # 🔍 the spy does its job here
    mood = get_mood(score)
    history.append((text, mood))
    print(f"{mood}  (score: {score:.2f})")

