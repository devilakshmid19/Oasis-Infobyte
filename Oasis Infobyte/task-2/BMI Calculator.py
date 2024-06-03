def bmi_calculate(weight, height):
    res = weight/(height** 2)
    return res

def bmi_arrange(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 25:
        print("Normal Weight")
    elif 25 <= bmi <= 30:
        print("Overweight") 
    else:
        print("Obese")

def main():
    weight = float(input("Enter your weight in kilograms:"))
    height = float(input("Enter your height in meters:"))
    if weight <= 0 or height <= 0:
        print("Error: weight and height must be positive numbers.")
        return
    bmi = bmi_calculate(weight,height)
    print("Your BMI is:",bmi)
    print("You are classified as:",bmi_arrange(bmi))

if __name__ == "__main__":
    main()