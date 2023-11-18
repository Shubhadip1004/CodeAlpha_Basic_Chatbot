# Import Dependancies
import nltk
from nltk.chat.util import Chat, reflections

# Run this command for first run
# nltk.download('punkt')

# Define the chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello ! How can I help you?",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"(.*)how are you ?",
        ["I'm doing well, thank you!", "I'm just a computer program, so I don't have feelings, but I'm here to help.",]
    ],
    [
        r"(.*) your name?",
        ["You can call me ChatBOT.",]
    ],
    [
        r"(.*) your age?",
        ["I am just a chatbot\n\t I have no age :)",]
    ],
    [
        r"(.*) do for me?",
        ["I can provide information, answer questions, or just have a chat with you.",]
    ],
    [
        r"(.*) (love|like) you", 
        ["I appreciate that!", "Thank you!", "You are kind."]
    ],
    [
        r"(.*) (love|like|watch|enjoy) sports?", 
        ["I %2 Football and Cricket!"]
    ],
    [
        r"(.*) you live?", 
        ["I live in your Computer ;)"]
    ],
    [
        r"(.*) weather in (.*)?",
        ["Weather in %2 is awesome like always", "Pleasant weather here in %2", "Its really Hot here in %2",
         "Its really Cold here in %2", "Its rainy here in %2", "Never even heard about %2 :( "]
    ],
    [
        r"(.*) favourite (sportsperson|player)?", 
        ["I like Cristiano Ronaldo", "I like Virat Kohli!","I like MS Dhoni!",
         "I like Lionel Messi!","I like Sunil Chhetri!", "I like Neymar Jr.!",
         "I like Sachin Tendulkar!","I like Mbappe!", "I like Haaland.!",]
    ],
    [
        r"(.*) (help|assist)(.*)", 
        ["How can I help you?", "I am here to assist you."]
    ],
    [
        r"(.*)", 
        ["I'm sorry, I did not understand that.", "Can you please rephrase that?", "Can you ask me a different Question?", 
         "I prefer not to answer this ", "I not sure what are you talking about ", "I'm not comfortable answering this question"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Define the conversation loop
def chat():
    print("Hello! I'm your friendly chatbot")
    print("Type 'quit' to exit.")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("\nGoodbye! Have a great day.")
            break
        response = chatbot.respond(user_input)
        print("\nChatBOT: ", response)
        print()

# Start the conversation
if __name__ == "__main__":
    chat()
