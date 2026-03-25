# BMI Calculator (Height in Feet)

height_feet = float(input("Enter your height (in feet): "))
weight = float(input("Enter your weight (in kg): "))

# Convert feet to meters
height_meters = height_feet * 0.3048

bmi = weight / (height_meters ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")