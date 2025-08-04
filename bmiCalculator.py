name = input("Enter your name: ")
weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))

BMI = weight / ((height/100)**2)

if BMI < 18.5:
    i = "underweight"
elif 18.5 <= BMI < 24.9:
    i = "normal weight"
elif 25 <= BMI < 29.9:
    i = "overweight"
elif 30 <= BMI < 34.9:
    i = "obesity class 1"
elif 35 <= BMI < 39.9:
    i = "obesity class 2"
elif BMI >= 40:
    i = "obesity class 3"

print(f"{name}, your BMI is {BMI:.1f} and you are classified as {i}.")
