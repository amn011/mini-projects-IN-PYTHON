print("________Welcome to Body-Mass Index calculator______________")
print("-----------------------------------------------------------")

height=float(input("enter your height in metres : "))
weight=float(input("enter your weight in kilograms :"))
bmi=(weight/(height*height))
print("Your BMI is :", +bmi)
if(bmi<18.5):
    print("nyou are under-weight, you should get in touch with a doctor")
elif(bmi>18.5 and bmi<24.9):
    print("You are normal, keep it regular ALL THE BEST")
else:
    print("You are over-weight, control your diet and consult a doctor")

