import sys
import time

print("Please enter the number of lives.")
lives = int(input()) 
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input()) 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
delay_print("\n" "Health has been set.")
print("\n")

#Ask Piotr how to add space between the UNICODE!

print("Lives:", 	'\u2665' * lives)
print("Energy: ",	'\u25C6' * energy)
print("Shield: ",	'\u26E8'  * shield)

print("Lives:  {'♥' * lives}")
print("Energy: {'♦' * energy}")
print("Shield: {'♦' * shield}")