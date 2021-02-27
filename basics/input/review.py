import asyncio
import time

#Talk with the user
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

delay_print("Salutare, numele meu este BEEP.")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(".")     
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(".") 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(".")   

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print("Te uiti putin confuz la mine, sa activam translatorul universal?") 

translator = input("Doresti sau nu doresti?").lower()
  if translator == Yes:
    print ("Activez translatorul universal")

  elif: translator = No:
    print("Esti sigur?")

  else: 
    print("Activez oricum translatorul universal")  

  Join = input('Would you like to join me?').lower()
if Join.startswith('y'):   # etc.