#password generator
import string
import random

print("***************************************** Password Generator ******************************************************")
print("In order to Create Strong password,You need to include Special characters,Numbers while creating Password")

def Input_Data():
    length=int(input("Enter the length of the password:"))
    print("Please answer above conditions to generate password")

    spchar=input("Do you want any special characters in the password(yes/no):").strip().lower()  
    
    letters=input("Do you want letters in your password(yes/no):").strip().lower()   
    
    numbers=input("Do you want numbers in your password(yes/no):").strip().lower()
    
    Characters=''
    
    if spchar=='yes':
        Characters=Characters+string.punctuation  #Contains special characters(#,@,>,<..... so on)
    if letters=='yes':  
        Characters=Characters+string.ascii_letters  #Contains Uppercase and Lowercase Alphabets 
    if numbers=='yes':
        Characters=Characters+string.digits   #Contains digits(0-9)
    return length,Characters

def Pass_Gen(length,Characters):
    if not Characters:
        print("please select any one criteria in order to generate password")
        return None    
    else:
        password=''
        for _ in range(length):
           password=password+random.choice(Characters)
        return password   

length,Characters=Input_Data()

Generate_password=Pass_Gen(length,Characters)

if Generate_password:
    print("Generated Password according to your Specification is",Generate_password)




