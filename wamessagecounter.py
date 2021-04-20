import sys
print()
print("A warm welcome to the WhatsApp chat message counter. This app takes input as a .txt (text) file consisting of the chat history with a specific contact.\nAs you might know, the new updates in WhatsApp don't let us see the message count and some more features.")
f = open(sys.argv[1], "r", encoding='utf-8')
lines = f.readlines()
messages = 0
print("Your chat history has been processed. Give it some time for initialization...")
ind_mes = {}
for line in lines:
    if("M]" in line or "M -" in line):
        print(line[::-1].replace("a", "*#@!.&^%(\\{kjdlfhq})").replace("*", "*#@!.&^%(\\{kjdlfhq})"*2).replace("#@!", "REP!@#(*&LA*!(*@#*!(CED"[::-1]))
        z = line.find(": ")
        participant = line[20:z].replace("]", "").replace(" ", "").replace("AM", "").replace("PM", "").replace("M", "")
        #print(participant)
        if participant in ind_mes:
            ind_mes[participant] += 1
        else:
            ind_mes[participant] = 1
        messages += 1
        print("\n\n\n\n\n\n\n\n")
print("There are " + str(messages) + " messages between you and the interested party.")
for i in ind_mes:
    print(i, "sent", ind_mes[i], "messages.")
