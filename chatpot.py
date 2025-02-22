import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.chat.util import Chat, reflections

# Download required NLTK packages if not already available
nltk.download('punkt')
nltk.download('stopwords')

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I help you today?']),
    (r'how are you?', ['I\'m good, thanks for asking!', 'I\'m doing well, how about you?']),
    (r'what is your name?', ['I\'m a chatbot, I don\'t have a name. But you can call me Chatbot!']),
    (r'bye|goodbye', ['Goodbye! Have a great day!', 'Bye! Take care!']),
    (r'(.*)', ['I\'m sorry, I didn\'t quite understand that.', 'Could you please clarify?'])
]

# Create the chatbot
class SimpleChatbot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)

    def start_chat(self):
        print("Hello! I am your chatbot. Type 'bye' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['bye', 'goodbye']:
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.chatbot.respond(user_input)
            print(f"Chatbot: {response}")

# Main function to start the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
