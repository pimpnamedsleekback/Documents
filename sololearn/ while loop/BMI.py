weight=int(input("enter weight in kgs :"))
height=float(input("enter height in meters :"))
BMI=(int(weight/height**2))
if 0<BMI<18.5:
     print(BMI,"\nYou are Underweight")
elif 18.5<=BMI<=25:
    print(BMI,"You are Normal")
elif 25<=BMI<=30:
    print(BMI,"You are Overweight")
elif BMI==30:
    print(BMI,"you are Obese")
else:
    print("Oh hell No!you need to watch you weight dude")

