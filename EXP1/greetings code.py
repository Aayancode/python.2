#Name: Aayan R. Sayyed 
#UIN: 241S027
#FE (ECS)
#Title: Personalized Greeting Generator*

def personalized_greeting():
    name = input("Enter your name: ")
    time_of_day = input("What time of day is it (morning, afternoon, evening)? ").lower()
    
    greetings = {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening"
    }
    
    greeting = greetings.get(time_of_day,"Hello")
    print(f"{greeting}, {name}! Hope you're having a great {time_of_day}!")

personalized_greeting()

