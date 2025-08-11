# find the body mass of the persor using weight and heigtht
# BMI Calculator
# Formula: BMI = weight (kg) / (height (m) * height (m))
weight = float(input("Enter your height in meters: "))
height = float(input("Enter your weight in kilograms: "))
body_mass  = weight / (height * height)

print(f"Your body mass index is: {body_mass:.2f}")
