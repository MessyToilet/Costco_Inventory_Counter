
import pandas as pd
import os

print("Starting Costco Inventory Counter!")

print("Total = [ (L)ength * (W)idth * (H)eight ] + (E)xtra")

counter = str(input("Current Counter: "))
while True:
    total = 0
    item  = ""

    while True:
        try:
            if os.name == "nt": os.system("cls")        #windows
            if os.name == "posix": os.system("clear")   #linux
            choice = int(input("\nO P T I O N S\n\t(1) Add Item\n\t(2) Edit Item\n\t(3) Delete Item\n\t(4) Quit\n\n"))
            break
        except:
            print("Bad Type Given!")

    if choice == 1:
        while True: #Getting values
            try:
                item   = str(input("Item: "))
                length = int(input("L: "))
                width  = int(input("W: "))
                height = int(input("H: "))
                extra  = int(input("E: "))
                if length > 0 and width > 0 and height > 0 and extra >= 0:
                    total = (length * width * height) + extra
                else:
                    print("Warning n <= 0!")
                    pass
                print(f'\n{item}: {total}')
                break
            except:
                print("Bad Type Given!")
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Terminating Session!")
        break
#use dict to store?
#break into funcs?
