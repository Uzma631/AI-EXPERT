
import random

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Himalayas", "Swiss Alps"],
    "cities": ["Tokyo", "Paris"]}

jokes = [
    "Why do programmers hate nature? Too many bugs!",
    "Why did the computer get sick? It had a virus!"]

def recommend():
    choice = input("Beaches, mountains, or cities? ").lower()

    if choice in destinations:
        place = random.choice(destinations[choice])
        print("TravelBot: Visit", place)

        answer = input("Do you like it? (yes/no): ").lower()

        if answer == "yes":
            print("TravelBot: Have a great trip!")
        else:
            print("TravelBot: Maybe next time!")
    else:
        print("TravelBot: Sorry, I don't know that category.")

def packing():
    place = input("Where are you going? ")
    days = input("How many days? ")

    print("Packing tips for", days, "days in", place)
    print("- Pack clothes.")
    print("- Bring a charger.")
    print("- Check the weather.")

def chat():
    print("Hello! I am TravelBot.")
    print(" I can suggest travel spots (say 'recommend'), packing tips (say 'pack'), and even tell you a joke! (say 'joke')")


    while True:
        user = input("You: ").lower()
        
        if "recommend" in user or "suggest" in user:
            recommend()
        elif "pack" in user:
            packing()
        elif "joke" in user:
            print("TravelBot:", random.choice(jokes))
        elif "help" in user:
            print("Try: recommend, packing, joke, or bye")
        elif "bye" in user or "exit" in user:
            print("TravelBot: Safe travels!")
            break
        else:
            print("TravelBot: I don't understand.")

chat()
