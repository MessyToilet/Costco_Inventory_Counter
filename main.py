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

def handle_info_bar(name:str, entries:str, last_entery:str) -> None:
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

    left_text    =f"| Last Entry: {last_entery}   Last Entry Total: "
    middle_text = f""
    right_text  = f"Total Entries: {entries:<9} |"

    left_text_size    = len(left_text)
    middle_text_start = (terminal_width - len(middle_text)) // 2
    right_text_start  = terminal_width - len(right_text)

    print(f"{left_text}{' ' * (middle_text_start - left_text_size)}{middle_text}{' ' * (right_text_start - middle_text_start - len(middle_text))}{right_text}")
    print(f"└{'-' * (terminal_width - 2)}┘")
    return

def handle_print_menu(name:str, entries: str, last_entry:str, ) -> int:
    while True:
        try:
            clear_screen()
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
    clear_screen()
    print("Starting Costco Inventory Counter!")

    current_counter_name: str = str(input("Current Counter: ")).capitalize()
    current_entry_total:  int = 0
    total_entries:        int = 0
    last_entry:           str = ""
    last_entry_total:     int = 0

    while True:
        choice = handle_print_menu(current_counter_name, str(total_entries), last_entry)
        if choice == 1:
            while True: #Getting values
                try:
                    current_entry_total, last_entry = handle_input_and_calculation()
                    total_entries += 1
                    print(current_entry_total)
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
