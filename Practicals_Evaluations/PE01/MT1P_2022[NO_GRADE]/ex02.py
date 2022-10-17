"""
The Body-mass index (BMI) of an individual is a measure of weight (in Kg) 
relation to height (in meters) and is computed as BMI = weight / height**2. 
This measure can be used to classify an individual:

Underweight     	< 17.0
Mild Underweight	[17.0, 18.5[
Normal	            [18.5, 25.0[
Overweight	        [25.0, 30.0[
Obese              	≥ 30.0

Write a function classify(weight, height) that computes the BMI for an individual 
given the weight and height and returns a string 'underweight', 'mild_underweight',
'normal', 'overweight' or 'obese'.
"""

def classify(weight, height):
    bmi_str = ""
    bmi = weight / height**2
    if (bmi < 17.0):
        bmi_str = "underweight"
    elif (bmi >= 17.0 and bmi < 18.5):
        bmi_str = "mild_underweight"
    elif (bmi >= 18.5 and bmi < 25.0):
        bmi_str = "normal"
    elif (bmi >= 25.0 and bmi < 30.0):
        bmi_str = "overweight"
    else:
        bmi_str = "obese"
    return bmi_str

"""
print("classify(75, 1.75)")
print(classify(75, 1.75))
print("classify(78, 1.65)")
print(classify(78, 1.65))
print("classify(50, 1.65)")
print(classify(50, 1.65))
print("classify(90, 1.65)")
print(classify(90, 1.65))
"""