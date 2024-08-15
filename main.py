from datetime import datetime
import pandas as pd
import shutil
import os

def handle_info_bar(name:str, entries:str, last_entery:str) -> None:
    version: str = "1.0"
    credits: str = "Jacob C"
    title:   str = "COSTCO INVENTORY COUNTER"
    time:    str = datetime.now().strftime("%H:%M:%S")

    terminal_width = shutil.get_terminal_size().columns
    left_text      = f"| Current Counter: {name}"
    middle_text    = f"{title}"
    right_text     = f"By: {credits}   Release: {version}   {time}  |"

    left_text_size    = len(left_text)
    middle_text_start = (terminal_width - len(middle_text)) // 2
    right_text_start  = terminal_width - len(right_text)

    print(f"┌{'-' * (terminal_width - 2)}┐")
    print(f"{left_text}{' ' * (middle_text_start - left_text_size)}{middle_text}{' ' * (right_text_start - middle_text_start - len(middle_text))}{right_text}")
    print(f"├{'-' * (terminal_width - 2)}┤")

    left_text    =f"| Last Entry: {last_entery}"
    middle_text = f""
    right_text  = f"Total Entries: {entries:<8} |"

    left_text_size    = len(left_text)
    middle_text_start = (terminal_width - len(middle_text)) // 2
    right_text_start  = terminal_width - len(right_text)

    print(f"{left_text}{' ' * (middle_text_start - left_text_size)}{middle_text}{' ' * (right_text_start - middle_text_start - len(middle_text))}{right_text}")
    print(f"└{'-' * (terminal_width - 2)}┘")
    return

def handle_print_menu(name:str, entries: str, last_entry:str, ) -> int:
    while True:
        try:
            if os.name == "nt": os.system("cls")        #windows
            if os.name == "posix": os.system("clear")   #linux
            handle_info_bar(name, entries, last_entry)
            choice: int = int(input("\nO P T I O N S\n\t(1) Add Item\n\t(2) Edit Item\n\t(3) Delete Item\n\t(4) Veiw Inventory\n\t(5) Quit\n\n"))
            break
        except:
            print("Bad Type Given!")
    return choice

def handle_input_and_calculation() -> tuple[int, str]:
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
    return total, item

def main() -> None:
    print("Starting Costco Inventory Counter!")

    current_counter_name: str = str(input("Current Counter: ")).capitalize()
    total:       int = 0
    total_entry: int = 0
    last_entry:  str = ""

    while True:
        choice = handle_print_menu(current_counter_name, str(total_entry), last_entry)
        if choice == 1:
            while True: #Getting values
                try:
                    total, last_item = handle_input_and_calculation()
                    total_entry += 1
                    print(total)
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
            break

    return

if __name__ == '__main__':
    main()
    print("Terminating Session!")




#use dict to store?
#Double check correct entry?
#better graphics? total entrys/ credits/ version/ last entry + info
#   implement last entry total
#implement pandas with CSV?
#   handle save file saving when quiting?
#convert info bar data to json?
