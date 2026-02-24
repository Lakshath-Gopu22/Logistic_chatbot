from app.chatbot import ChatBot

bot = ChatBot()
print("Chatbot running...\n")

while True:
    msg = input("You: ")
    print("Bot:", bot.handle_message(msg))
