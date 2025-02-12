import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox


#Display option menu
print("please type a number from the given option:")
print("1-expence")
print("2- income")
print("3- exit")
print("4-view")
print("5-delete")
print("6-update")
print("7-save")
print("8-load")
print("9-summary")
print("10- GUI ")
#Initial amount
amount= 0
#list to store the transaction
list=[]
list.append({0:[],1:[],2:[],3:[],4:[],5:[]})


#Function to check if input is a valid catagory
def get_valid_catagory():
    print("Please select a valid category\n 0.Salary\n 1.Education\n 2.Groceries\n 3.Rent\n 4.Clothing\n 5.Other")
    while True:
        try:
            category = int(input("Enter a Category: "))
            if category >= 0 and category <= 5:
                return category
            else:
                print("Invalid category. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        

#Function to add a transaction
def add_transaction(amount,transaction_type):
    print("",transaction_type)
    category1=get_valid_catagory()
    Date=get_valid_date()
    print("Valid date enterded:",Date)
    user_amount = float(getValidAmount());
    description=get_valid_description()
    print("Valid description entered:", description)
    if transaction_type=="expence":
        amount = amount-user_amount
        print("your amount is:",amount)
        #list.append([amount,description,"expence",Date])
        list[0][category1].append({"amount":user_amount,"description":description,"type":"expence","Date":Date})
    else:
        amount=amount+user_amount
        print("yor amount is:",amount)
        #list.append([amount,description,"income",Date])
        list[0][category1].append({"amount":user_amount,"description":description,"type":"income","Date":Date})
    return (amount)
#function to view transaction

def view_transaction():
    for x in range(len(list)):
        print(list[x])

transaction_list = []  # Define transaction_list as an empty list
#Function to delete a transaction
def delete_transaction():
    if not list:
        print("Transaction list is empty.")
        return
   
    categoryToDelete = get_valid_catagory()
    selectDescription = input("Enter description to delete: ")

    myList = list[0].get(categoryToDelete, [])
    if not myList:
        print("No transactions found for the selected category.")
        return

    print("Before deletion:", myList)  # Print myList before deletion

    found = False
    for data in myList:
        if data.get("description") == selectDescription:
            found = True
            myList.remove(data)
            print("Transaction deleted successfully.")
            break

    print("After deletion:", myList)  # Print myList after deletion

    if not found:
        print("Transaction not found.")




#Function to update a transaction
def update_transaction():
  user_input_to_update=input("enter user input to update :")
  print(user_input_to_update)
  for x in range(len(list)):
      print(list[x])
      
  if(list[x][1]==user_input_to_update):
        
        print("found and item to update")#
        amount_update=int(input("Enter the amount of the update item :"))
        list[x][0]= amount_update
#Function to save transaction
def save_transaction():
  print("save transaction function working")
  with open("file.json",'w') as f:
      json.dump(list,f,indent=2)
#Function to load transactions from a file

def load_transaction():
    print("Load transaction function is working")
    file_path = 'file.json'

    with open(file_path, 'r') as file:
        data = json.load(file)

    data_list = data[0]
    result_list = []  # Start an empty list to store values
   
    result_list.append({0:[],1:[],2:[],3:[],4:[],5:[]})

   
    for key, value in data_list.items():
        #print(f"Key: {int(key)}, Value: {value}")
        result_list[0][key]=value
        # Append value to the list
        print(value)
       
    
    return result_list

#Function to display summary
def display_summary():
    total_income = 0
    total_expense = 0
    for category_data in list[0].values():
        for transaction in category_data:
            if transaction["type"] == "income":
                total_income += transaction["amount"]
            elif transaction["type"] == "expense":
                total_expense += transaction["amount"]

    net_income = total_income - total_expense
    from datetime import date
    today = date.today()

    current_date = today.strftime("%Y/%m/%d ")

    print("Summary:")
    print("Total Income:", total_income)
    print("Total Expenses:", total_expense)
    print("Net Income:", net_income)
    print("current date:", current_date)

#Function to check if input is a valid number
def is_valid_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

#Function to get a valid amount from the user    
def getValidAmount():
    is_valid=True
    while is_valid:
        custom_input=input("enter custom input :")
        print(custom_input)
        is_valid=is_valid_number(custom_input)
        if not is_valid:
            return custom_input
        

# Function to check if date input is valid 
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
# Function to get a valid  date  from user   
def get_valid_date():
    while True:
        date_input = input("Enter a date in YYYY-MM-DD format:")
        if is_valid_date(date_input):
            return date_input
        else:
            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
# Function to get a valid description from user
def get_valid_description():
    while True:
        description = input("Enter a description (at least 5 characters): ")
        if len(description) >= 5:
            valid_description = description  # Description must have  least five characters
            return valid_description
        else:
            print("Description must be at least 5 characters long.")
# creat GUI using tkinter to display transaction
def GUI(data_list):
    def search():
        search_text = entry.get().lower()

        for item in tree.get_children():
            tree.delete(item)

        found = False
        for key, value in data_list[0].items():
            for item in value:

                if search_text in item['description'].lower() or search_text in item['Date'].lower():# Check if keyword matches transaction description or date
                    # insert date,description,date and type to tabel
                    tree.insert("", tk.END, values=(key, item['Date'], item['description'], item['amount'], item['type']))
                    
                    item_id = tree.get_children()[-1]

                    tree.item(item_id, tags=('highlight',))
                    
                else:
                    # rows are inseert to data without highlighting
                    tree.insert("", tk.END, values=(key, item['Date'], item['description'], item['amount'], item['type']))
                    
# create main window
    root = tk.Tk()
    root.title("Personal Finance Tracker")
# create the label for search
    search_label = tk.Label(root, text="Search:")
    search_label.grid(row=0, column=0)
# create the entry filed for search
    entry = ttk.Entry(root)
    entry.grid(row=0, column=2)
# create the button for search
    button = ttk.Button(root, text="Search", command=search)  # Add command to call the search function
    button.grid(row=0, column=3)
# 
    def category(input):
            if input=="0":
                return "Salary"
            elif input=="1":
                return "Education"
            elif input=="2":
                return"Groceries"
            elif input=="3":
                return"Rent"
            elif input=="4":
                return"Clothing"
            elif input=="5":
                return"Other"
            else:
                return"Category is not found"
    # Table view
    tree = ttk.Treeview(root, columns=("Category", "Date", "Description", "Amount", "Type"), show="headings")
    tree.heading("Category", text="Category")
    tree.heading("Date", text="Date")
    tree.heading("Description", text="Description")
    tree.heading("Amount", text="Amount")
    tree.heading("Type", text="Type")
    tree.grid(row=11, column=0, columnspan=4)

# define tag for the highlighted rows
    tree.tag_configure('highlight', background='red')

#fii data into tabel
    for key, value in data_list[0].items():
        for item in value:

            tree.insert("", tk.END, values=(category(key), item['Date'], item['description'], item['amount'], item['type']))

    root.mainloop()




#Main loop
while True:
    user_input=input("Enter a user input : ")
    if user_input =="1":
        amount=add_transaction(amount,"expence")
        print(amount)
    elif user_input== "2":
        amount=add_transaction(amount,"income")
        print(amount)
    elif user_input=="3":
        print("exit")
        break
    elif user_input=='4':
        view_transaction()
    elif user_input=='5':
        delete_transaction()
    elif user_input=='6':
      update_transaction()
    elif user_input=='7':
      save_transaction()
    elif user_input=='8':
      list=load_transaction()
    elif user_input=='9':
      display_summary()
    elif user_input=='10':
        data_list = load_transaction()  
        GUI(data_list)
    else:
      print("try again")

