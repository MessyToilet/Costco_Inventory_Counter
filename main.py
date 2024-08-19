from datetime import datetime
import pandas as pd
import shutil
import os

def clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")        #windows
    elif os.name == "posix":
        os.system("clear")   #linux
    else:
        print("Unkown CLI!")
    return

def handle_info_bar(name:str, entries:str, last_entery:str, last_entry_total: str) -> None:
    version: str = "1.0"
    credits: str = "Snow Desert Solutions"
    title:   str = "COSTCO INVENTORY COUNTER"
    time:    str = datetime.now().strftime("%H:%M:%S")

    terminal_width = shutil.get_terminal_size().columns
    left_text      = f"| Current Counter: {name}"
    middle_text    = f"{title}"
    right_text     = f"{credits}   Release: {version}   {time}  |"

    left_text_size    = len(left_text)
    middle_text_start = (terminal_width - len(middle_text)) // 2
    right_text_start  = terminal_width - len(right_text)

    print(f"┌{'-' * (terminal_width - 2)}┐")
    print(f"{left_text}{' ' * (middle_text_start - left_text_size)}{middle_text}{' ' * (right_text_start - middle_text_start - len(middle_text))}{right_text}")
    print(f"├{'-' * (terminal_width - 2)}┤")

    left_text    =f"| Last Entry: {last_entery}   Last Entry Total: {last_entry_total}"
    middle_text = f""
    right_text  = f"Total Entries: {entries:<9} |"

    left_text_size    = len(left_text)
    middle_text_start = (terminal_width - len(middle_text)) // 2
    right_text_start  = terminal_width - len(right_text)

    print(f"{left_text}{' ' * (middle_text_start - left_text_size)}{middle_text}{' ' * (right_text_start - middle_text_start - len(middle_text))}{right_text}")
    print(f"└{'-' * (terminal_width - 2)}┘")
    return

def handle_print_menu(name:str, entries: str, last_entry:str, last_entry_total:str ) -> int:
    while True:
        try:
            clear_screen()
            handle_info_bar(name, entries, last_entry, last_entry_total)
            choice: int = int(input("\nO P T I O N S\n\t(1) Add Item\n\t(2) Edit Item\n\t(3) Delete Item\n\t(4) Veiw Inventory\n\t(5) Quit\n\n"))
            break
        except:
            print("Bad Type Given!")
    return choice

def handle_input_and_calculation() -> tuple[int, str]:
    total       = 0
    item:   str = str(input("Item: "))
    length: int = int(input("L: "))
    width:  int = int(input("W: "))
    height: int = int(input("H: "))
    extra:  int = int(input("E: "))
    if length > 0 and width > 0 and height > 0 and extra >= 0:
        total = (length * width * height) + extra
    else:
        print("Warning n <= 0!")
    return total, item

def choice_1() -> tuple[str, int]:
    while True: #Getting values
        try:
            current_entry_total, currnet_entry = handle_input_and_calculation()

            #check if item is non-empty
            if currnet_entry in inventory:
                inventory[currnet_entry] += current_entry_total
            else:
                inventory[currnet_entry] = current_entry_total

            last_entry       = currnet_entry
            last_entry_total = inventory[last_entry]

            break
        except:
            print("Bad Type Given!")
    return last_entry, last_entry_total

def handle_edit():
    return

def handle_delete():
    return

def print_inventory_sorted() -> None:
    inventory_sorted = {key: value for key, value in sorted(inventory.items())}
    for key in inventory_sorted:
        print(f"{key}{' ' * (10 - len(key))} {inventory_sorted[key]}")
    return

def choice_4() -> None:
    clear_screen()
    print(f"Item{' ' * (10 - len('Item'))} Amount")
    print_inventory_sorted()
    for i in range(100):
        print(i)
    input("Press Any Key To Contiune...")
    return

def choice_5() -> None:
    print_inventory_sorted()
    return

def main() -> None:
    clear_screen()
    print("Starting Costco Inventory Counter!")

    global inventory
    inventory = {}

    current_counter_name: str = str(input("Current Counter: ")).capitalize()
    last_entry:           str = ""
    last_entry_total:     int = 0


    while True:
        choice = handle_print_menu(current_counter_name, str(len(inventory)), last_entry, str(last_entry_total))
        if choice == 1: #add
            last_entry, last_entry_total = choice_1()

        elif choice == 2: #edit

            pass
        elif choice == 3: #delete

            pass
        elif choice == 4: #veiw
            choice_4()
            pass
        elif choice == 5: #quit
            choice_5()
            break

    return

if __name__ == '__main__':
    main()
    print("Terminating Session!")



#break choices into funcs
#use dict to store?
#   check if inv is non-empty
#   add/ remove/ edit key+val
#Double check correct entry?
#better graphics? total entrys/ credits/ version/ last entry + info
#   implement last entry total
#implement pandas with CSV?
#   handle save file saving when quiting?
#convert info bar data to json?
#Edit Choice:
#   edit total for item
#   rename item
#   merge two items
