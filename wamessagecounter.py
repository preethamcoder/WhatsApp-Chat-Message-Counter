import sys
print()
print("""Hello, a warm welcome to the WhatsApp chat message counter. This app takes input as a .txt (text) file consisting of the chat history with a specific contact.\nAs you might know, the new updates in WhatsApp don't let us see the message count and some more features.""")
f = open(sys.argv[1], "r", encoding='utf-8')
lines = f.readlines()
messages = -1
print("Your chat history has been processed. Give it some time for initialization...")
for line in lines:
    if("M]" in line):
        messages += 1
print("There are " + str(messages) + " messages in this chat.")