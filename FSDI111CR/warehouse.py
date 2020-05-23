"""
    Program: Warehouse management system
    Functionality:
        - Repeated menu
        - Register items to catalog
            - id(auto generated)
            - title
            - category
            - price
            - stock
        -Display Catalog
        -Display items with no stock (out of stock)
        
        -Saving / retrieving data to/from file
        
        -Update the stock of an item
         - show list of items
         - ask the user to choose an id
         - ask the user for the new stock value
         - find item with selected id
         - update the stock
         - save changes

        - Print the total value of the stock (sum(price * stock))
        
        - Remove an item from the catalog

        -Register a sale
            - show the list of items
            - ask user to choose an id
            - ask the user to provide the quantity
            - update the stock

        - Have a log of events
            - file name for the logs
            - a list for the log entries
            - add_log_event function
            - save_log
            - read_log
            - update existing fns to register log entries

        - Display log of events
        - Display different categories

"""

from menu import menu, clear, header
from item import Item
import datetime
import pickle

# global variabls
catalog = []
log = []
data_file = "warehouse.data"
last_id = 0
log_file = "log.data"

def save_log():
    global log_file
    writer = open(log_file, "wb")
    pickle.dump(log, writer)
    writer.close()
    print('** Log Saved! **')

def read_log():
    try:
        global log_file
        reader = open(log_file, "rb") #[R]ead [B]inary
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)

        how_many = len(log)
        print("** Loaded "+str(how_many)+ " log entries!")
    except:
        print("** Error loading log entries **")

# def display_log():
#     size = len(log)
#     header("Current Log has (" + str(size) + " Entries!)")

#     print("|" + "ID".rjust(2) 
#         + " | " + 'Title'.ljust(20)
#         + " | " + 'Category'.ljust(15)
#         + " | " + 'Price'.rjust(10)
#         + " | " + 'Stock'.rjust(5) +'|' )
#     print("_"*70)

#     for entry in log:
#         if(entry.update == '1'):
#             print(entry.title+" stock was updated to "+str(entry.stock))
#             print("_"*70)
#         elif(entery.update =='2'):
#             print(entry.title+" value was updated to "+str(entry.value))
#             print("_"*70)
#         elif(entery.update =='3'):
#             print(entry.title+" was registerd as a new item!")
#             print("_"*70)


def save_catalog():
    global data_file
    writer = open(data_file, "wb") #create file (overwrite), open it to [W]rite [B]inary
    pickle.dump(catalog, writer)
    writer.close()
    print("** Data Saved! **")

def read_catalog():
    try:
        global last_id
        global data_file
        reader = open(data_file, "rb") #[R]ead [B]inary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id
    except:
        print("** No data file found, db is empty **")

# functions


def delete_item():
    header("Delete an Item")
    display_catalog()
    select = int(input('Please select the item ID you would like to delete: '))
    found = False
    for item in catalog:
        if(item.id == select):
            found = True
            print('\n'+"**"+item.title+" has been removed!**"+'\n')
            add_log_event("Removed", "Removed item: "+ str(item.id))
            catalog.remove(item)
            save_catalog()
    if(not found):
        print("Error: Selected id does not exist, try again")

def register_item():
    header("Register New Item")
    global last_id
    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))
    

    new_item = Item() # <- create instances of a class (object)
    last_id += 1    #NO last_id++ :(
    new_item.id = last_id
    new_item.title = title
    new_item.category = cat
    new_item.price = price
    new_item.stock = stock      
    
    catalog.append(new_item)
    add_log_event("NewItem", "Added item: "+str(last_id))
    print("Item created!")

def display_catalog():
    size = len(catalog)
    header("Current Catalog(" + str(size) + " items)")

    print("|" + "ID".rjust(2) 
        + " | " + 'Title'.ljust(20)
        + " | " + 'Category'.ljust(15)
        + " | " + 'Price'.rjust(10)
        + " | " + 'Stock'.rjust(5) +'|' )
    print("_"*70)

    for item in catalog:
        print("|"+str(item.id).rjust(2) 
        + " | " + item.title.ljust(20)
        + " | " + item.category.ljust(15)
        + " | " + str(item.price).rjust(10)
        + " | " + str(item.stock).rjust(5)+"|")
        print("_"*70)

def display_out_of_stock():
    size = len(catalog)
    header("Currently Out of Stock(" + str(size) + " items)")

    
    print("|" + "ID".rjust(2) 
        + " | " + 'Title'.ljust(20)
        + " | " + 'Category'.ljust(15)
        + " | " + 'Price'.rjust(10)
        + " | " + 'Stock'.rjust(5) +'|' )
    print("_"*70)

    for item in catalog:
        if(item.stock == 0):
            print("|"+str(item.id).rjust(2) 
            + " | " + item.title.ljust(20)
            + " | " + item.category.ljust(15)
            + " | " + str(item.price).rjust(10)
            + " | " + str(item.stock).rjust(5)+"|")
            print("_"*70)
     
def update_stock(opc):
    header("Please select an item.")
    display_catalog() 
    Id = int(input('Please enter the product id...'))
   
    found = False
    for item in catalog:
        if(item.id == Id):
            found = True
            
            if(opc == 1):
                stock = int(input("New stock value: "))
                item.stock = stock
                print('**Stock Updated!**')
                add_log_event("Set Stock", "Updated Stock for item: "+ str(item.id))
            else:
                sold = int(input("Number of items to sale: "))
                item.stock -= sold # decrese the stock value by the number of sold items
                print('**Sale Updated!**')
                add_log_event("Sale", "Sold: "+ str(sold) + " item(s) of item: "+ str(item.id))

            

    if(not found):
        print("Error: Selected id does not exist, try again")

def total_investment():
    sum = 0.0
    for x in catalog:
        sum += x.stock * x.price

    header("Total Investment: $"+ str(sum))

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%b-%d, %Y %T")

def add_log_event(event_type,event_description):
    entry = "12:00" + " | " + event_type.ljust(10)  + " | " + event_description.ljust(30)
    log.append(entry)
    save_log()

def print_log():
    size = len(log)
    header("Currently (" + str(size) + " logged events!)")
    print("Date".rjust(5) 
        + " | " + 'Event'.ljust(10)
        + " | " + 'Description'.ljust(30))
    print("_"*70)

    for entry in log:       
        print(entry)
        print("_"*70)

def display_categories():
    header("List of Categories!")
    categories = []
    for item in catalog:
        categories.append(item.category)
    for category in categories:
        if categories.count(category) > 1:
            categories.remove(category)
        print(category)

    print("-"*70)
    
    

 


# instructions
# start menu


# first load
read_catalog()
read_log()
input("Press enter to continue")

opc = ""
while(opc!= 'x'):
    clear()
    menu()
    opc = input('Please select an option: ')
    print("\n")
    if(opc == 'x'):
        clear()
        break # break = finish loops

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()  
    elif(opc == '3'):  
        display_out_of_stock()
    elif(opc == '4'):
        update_stock(1) # update stock
        save_catalog()
    elif(opc == '5'):
        total_investment()
    elif(opc == '6'):
        delete_item()
    elif(opc == '7'):
        update_stock(2)# register a sale
        save_catalog()
    elif(opc == '8'):
        print_log()
    elif(opc == '9'):
        display_categories()

    input("Press enter to continue....")

