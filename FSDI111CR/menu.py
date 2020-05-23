import os

def menu():
    print("\n\n")
    print("-"*30)
    print("  Warehouse Control")
    print("-"*30)

    print(" [1] Register Items")
    print(" [2] Display Catalog")
    print(" [3] Display Out of Stock")
    print(" [4] Update Item Stock")
    print(" [5] Show total investment")
    print(" [6] Delete an Item")
    print(" [7] Register a Sale")
    print(" [8] Display Log")
    print(" [9] Display Categories")

    print(" [x] Exit")

def header(title):
    clear()
    print("-" *70)
    print(" "+title)
    print("-" *70)

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')