height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = weight * 703 / height ** 2
bmi = round(bmi, 1)

# < 16.0    Severely Underweight 
# 16.0 - 18.4   Underweight
# 18.5 - 24.9   Normal
# 25.0 - 29.9   Overweight
# 30.0 - 34.9   Moderately Obese
# 35.0 - 39.9   Severely Obese
# > 39.9   Morbidly Obese

if bmi < 16.0:
    print(f"Your BMI of {bmi} makes you Severely Underweight")
elif bmi < 18.4:
    print(f"Your BMI of {bmi} makes you Underweight")
elif bmi < 24.9:
    print(f"Your BMI of {bmi} makes you Normal")
elif bmi <  29.9:
    print(f"Your BMI of {bmi} makes you Overweight")
elif bmi < 34.9:
    print(f"Your BMI of {bmi} makes you Moderately Obese")
elif bmi < 39.9:
    print(f"Your BMI of {bmi} makes you Severely Obese")
else:
    print(f"Your BMI of {bmi} makes you Morbidly Obese")