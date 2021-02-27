import sys
import time

# Ask user to enter their name 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

delay_print("\t What is your name friend?")
print()
print()
name = input("\t") 
print()
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

delay_print("\t It is nice to meet you, "+ name + "!")