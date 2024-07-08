# BMI (Body Mass Index) calculator
# It is mainly used to calculate fat in your body based on your height and weight.
# if Bmi(lessthan)<18.5 then you are Underweight
# if Bmi is in between 18.5 and 24.9  then you are Normal
# if Bmi (greater than )> 24.9 the you are Overweight
print("*******  This is BMI (Body Mass Index) calculator  *********")
print("********** WEIGHT(kILOGRAMS) **** HEIGHT(METERS) ********* " )
def Take_Data():
    Name=input("Enter your name:")
    Weight=float(input("Enter your Weight in Kilograms:"))
    Height=float(input("Enter your Height in meters:"))
    Height=round(Height*0.3048,2) 
    return Name,Weight,Height
def Bmi_cal(Weight,Height):
    if(Weight >0 and Height>0 ):
        Bmi=Weight/(Height**2)
        Bmi=round(Bmi,2)
        print(Bmi)
        return Bmi
    else:
        print("Incorrect Height and weight-Please Enter correct Weight and Height ")
def Display(Name,Bmi):
    if(Bmi>=0  and Bmi<=18.5):
        print("Hello",Name,"\nYou are Underweight")
        print("You have to take good food to be healthy (Normal)")
    elif(Bmi>18.5 and Bmi<=24.9):
        print("Hello",Name,"\nYou are Normal")
        print("You are healthy and fit")
    else:
        print("Hello",Name,"\nYou are Overweight")
        print("you are having more fat maintain your diet by taking less food")
Name,Weight,Height=Take_Data()
Bmi=Bmi_cal(Weight,Height)
Display(Name,Bmi)