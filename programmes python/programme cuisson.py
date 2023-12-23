import time
import platform
import winsound


print("---WELCOME TO THE FAST-FOOD CONNECTÉ---")
print()
print(f"Menu of the day")
print()
print("1- Boiled eggs: 3 minutes")
print("2- spaghetti bolognese: 6 minutes")
print("3- vegetarian burger: 9 minutes")
print()
choice = input("Make your choice : ")

if choice == "1":
    cooking_time = 3*60

elif choice == "2":
    cooking_time = 4*60

else:
    cooking_time = 5*60

while cooking_time > 0:
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.1)
        cooking_time -=1
    
    minute = cooking_time//60
    sec = cooking_time-minute*60
    print(f" remaining time : {minute} : {sec}", end="", flush=True)
    print()

if platform.system() == "Windows":
    frequency = 600
    duration = 500
    winsound.Beep(frequency, duration)
print()
print("cooking finished... enjoy your meal")