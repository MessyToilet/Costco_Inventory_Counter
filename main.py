
import pandas as pd
import os

def handle_print_menu() -> int:
    while True:
        try:
            if os.name == "nt": os.system("cls")        #windows
            if os.name == "posix": os.system("clear")   #linux
            choice: int = int(input("\nO P T I O N S\n\t(1) Add Item\n\t(2) Edit Item\n\t(3) Delete Item\n\t(4) Veiw Inventory\n\t(5) Quit\n\n"))
            break
        except:
            print("Bad Type Given!")
    return choice

def handle_input_and_calculation() -> int:
    total       = 0
    item        = str(input("Item: "))
    length: int = int(input("L: "))
    width:  int = int(input("W: "))
    height: int = int(input("H: "))
    extra:  int = int(input("E: "))
    if length > 0 and width > 0 and height > 0 and extra >= 0:
        total = (length * width * height) + extra
    else:
        print("Warning n <= 0!")
    return total

def main() -> None:
    print("Starting Costco Inventory Counter!")
    print("Total = [ (L)ength * (W)idth * (H)eight ] + (E)xtra")

    counter: str = str(input("Current Counter: "))

    while True:
        total: int = 0
        item:  str = ""

        if choice := handle_print_menu() == 1:
            while True: #Getting values
                try:
                    total = handle_input_and_calculation()
                    print(f'\n{item}: {total}')
                    break
                except:
                    print("Bad Type Given!")
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Terminating Session!")
            break

    return

if __name__ == '__main__':
    main()





#use dict to store?
#Double check correct entry?
#better graphics? total entrys/ credits/ version/ last entry + info
#implement pandas with CSV?
