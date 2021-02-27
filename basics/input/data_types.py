import sys
import time

# Ask user to enter their name 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("What is your name friend?")
name = str(input("\t"))
# Ask user to enter their age 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print("How old are you (in years)?")
age = int(input("\t"))
# Ask user to enter their Height 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print("How tall are you (in meters)?")
height = float(input("\t"))
# Ask user to enter their weight 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print("How much do you weight (in kilograms)?")
weight = float(input("\t"))

bmi = weight / height**2

# Answer the user

# Ask Piotr how can we delay_print with more variables 

print(name, "you are", age ,"years old and your bmi is", bmi)
