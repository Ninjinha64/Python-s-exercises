weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

IMC = weight / (height ** 2)
if IMC < 18.5:
    print("Underweight")
elif 18.5 <= IMC < 25:
    print("Normal weight")
elif  25 <= IMC < 30:
    print("Overweight")