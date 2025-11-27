"""This program compares the sales of apples and bananas"""

apples = int(input("Enter the number of apples: "))

bananas = int(input("Enter the number of bananas: "))

"""Compare the sales of apples and bananas and print the result."""

if apples > bananas:
    print("The apples has sold more than bananas.")
elif bananas > apples:
    print("The bananas has sold more than apples.")
else:
    print("The apples and bananas have sold the same amount.")