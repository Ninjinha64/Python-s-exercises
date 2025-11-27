distance = float(input("Enter the distance of your trip in km: "))
if distance <= 100:
    print("The ticket price is R$10,00.")
elif 100 < distance <= 200:
    print("The ticket price is R$20,00.")
else:
    print("The ticket price is R$30,00.")
