import sys
import time
#Ask for the desired number of lives
print("Please enter the number of lives.")
lives = int(input()) 

#Ask for the desired number of energy
print("Please enter the energy level.")
energy = int(input())

#Ask for the desired number of shield
print("Please enter the shield level.")
shield = int(input()) 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
delay_print("\n" "Health has been set.")
print("\n")

#Print the user desired settings

print("Lives:", 	'\u2665' * lives)
print("Energy: ",	'\u25C6' * energy)
print("Shield: ",	' \u26E8'  * shield)
