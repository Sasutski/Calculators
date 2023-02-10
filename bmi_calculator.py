print("BMI CALC© by Sasutski")
conversion = input("Pounds or Kilograms?:\n")
if conversion  == ("Kilograms"):
    weight = float(input("Weight in Kg: \n"))
    height = float(input("Height in meters: \n"))
    # if user inputs centimeters
    if height > 3:
        newheight = height/100
    else:
        newheight = height
    bmi = (weight/(newheight ** 2))
else:
    weight = float(input("Weight in Pounds: \n"))
    height = float(input("Height in Inches: \n"))
    bmi = (weight/(height ** 2)) * 703
print(bmi)
if bmi < 18.5:
    print("Underweight: Possible nutritional deficiency and osteoporosis.")
elif bmi <= 22.9:
    print("Healthy Range")
elif bmi <= 27.4:
    print("Mild to moderate overweight: Moderate risk of developing heart disease, high blood pressure, stroke, diabetes mellitus.")
else:
    print("Very Overweight to obese: High risk of developing heart disease, high blood pressure, stroke, diabetes mellitus. Metabolic Syndrome.")