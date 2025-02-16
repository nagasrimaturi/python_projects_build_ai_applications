from textblob import TextBlob
class ChatBot:
    def __init__(self):
        self.sentiment_analyzer=TextBlob("")
    def chat(self):
        print(f"chatbot:hi,how can i help you")
        while True:
            user_message = input("you: ").strip()

            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            if sentiment_score > 0:
                chatbot_message = f"cahtbot:thats greate to hear that \n sentimet scroe :{sentiment_score}\n"
            elif sentiment_score < 0:
                chatbot_message = f"cahtbot:sorry about that,how can i help with that \n sentimet scroe :{sentiment_score}\n"
            else:
                chatbot_message = f"chatbot:i see,tell me more about it \n sentimet scroe :{sentiment_score}\n"
              
            print(chatbot_message)


if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.chat()
     
               