# write a script that checks if someone is elifible to vote
age=int(input("Enter age : " ))

if age>= 18:
    print("You are eligible to vote")
else:
    print("You are not viable to vote .  underage.....")

# Write a scrpt to check whether if a number is odd or even

number=int(input("Enter number :"))

if number % 2 == 0:
    print(f"{number} is Even number")
else :
    print(f"{number} is Odd number")

    # Write a script that checks ("python123") is valid else wrong password 

password="python123"
password= input("Enter password:")
if password == "python123":
    print("Password valid")
else :
    print("Invalid password")
 
# write a script that checks the largest number of three

num1=int(input("Enter the first number :"))
num2=int(input("Enter the first number :"))
num3=int(input("Enter the first number :"))

if num1>num2 and num1>num3 :
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3 :
    print(f"{num2}is the largest number")
elif num3>num1 and  num3>num2 : 
    print(f"{num3} is the largest number ")
else :
    print("They are equal")