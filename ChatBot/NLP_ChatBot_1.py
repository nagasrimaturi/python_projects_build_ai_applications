from textblob import TextBlob

intents = {
    "wishes":{
        "keywords":["hey,hi,good morning,good evening"],
        "response":"hey,how can i help you"
        
    },
    "hours":{
        "keywords":["open","close","hours"],
        "response":"The store will from the 9am to 10pm,from monday to friday."
    },
    "return":{
        "keywords":["return","money back","refund","payment"],
        "response":"Iam happy to help with your return, Let me connect to the live agent."
    }
    
}
def get_response(message):
    message = message.lower()
    
    for intent_data in intents.values():
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]
        
        sentiment = TextBlob(message).sentiment.polarity
        
    return ("thats great to hear that" if sentiment > 0 else
             "i can help with your return, let me conncet to the live agent" if sentiment < 0 else
             "I see ,tell me about it more")
def chatbot():
    print(f"chatbot:Hi,how can help with you today")
    while (user_message := input("you: ").strip().lower()) not in ["quit","bye","exit"]:
        print(f"chatbot: {get_response(user_message)}")


    print("Thank you fro chatting ,Have a nice day")

if __name__ == "__main__":
    chatbot()