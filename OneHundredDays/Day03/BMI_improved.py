# This software objective is to calculate one's BMI

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"{bmi}, You are underweight")
elif bmi < 25:
    print(f"{bmi}, You are at the average weight")
elif bmi < 30:
    print(f"{bmi}, You are overweight")
elif bmi < 35:
    print(f"{bmi}, You are obese")
elif bmi >= 35:
    print(f"{bmi}, You are clinically obese")
else:
    print("Invalid weight")
