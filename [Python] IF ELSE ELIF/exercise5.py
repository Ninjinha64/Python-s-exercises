limit = 3000.0
Money = float(input("Type your outgoing money of the mounth: "))

if Money > limit:
    print("You have exceeded your budget limit!")
else:
    print("You are within your budget limit.")
    