import uuid
import json
import os
#Build a simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.
# requirements : 
#Requirements
# add an expense with a description and amount
#Update an expense 
# delete an expense
# View all expenses
#View a summarry of all expenses
# view a summarry of expenses for a specific month.
# allow users to export expenxes to csv file
class Expense:
 def __init__(self,name,dsc,budgeted_amount,month):
    self.name = str(name)
    self.dsc = str(dsc)                         #initialization of class expense
    self.budget_amount = float(budgeted_amount)
    self.month = month
    #I quickly realize adding input to these guys wount assist in capturing the input


 def __str__(self):
      return f"{self.name} | {self.dsc} | {self.budget_amount} | {self.month} |"

#expenses block defining the logic or adding the first 

expense = {}
expense_f = "expense.json"    #file initialization
if os.path.exists(expense_f):
   with open(expense_f,"r") as f:      #checking file existence
      try :
         data = json.load(f)
         expenses =  deserialize(data)
      except json.JSONDecodeError:    #Loading the file if it exists{to memory}
         expenses = {}
else:
   expenses = {}                         #If it doesnt exist expenses is made then its made empty.




def add():
    expense_id = str(uuid.uuid4())
    name = input("Name: ")
    dsc = input("description : ")
    month = int(input("month : "))
    if 1 <= month <= 12 : 
      budgeted_amount = float(input("budgeted_amount"))
      new_expense = Expense(name,dsc,budgeted_amount,month)
      expenses[expense_id] = new_expense
      print("Expense added successfully.")
    else:
       print("Month is invalid : Please enter month ")

    

def view():
   if not expenses:
    print ("You dont have an expense stored.")
    return
   for expense_id, expense in expenses.items() :
     print (f"|Expense name : {expense.name} |")
     print (f"|Expense description : {expense.dsc}|")
     print (f"|Expense month : {expense.month}|")
     print (f"|Expense budget_amount : {expense.budget_amount}|")
     print("-"*20)



def delete():
   expense_d = input("Enter the name of the expense you want to delete")
   for expense_id, expense in expenses.items():
      if expense.name == expense_d:
         del expenses[expense_id]
         
         print("The expense was deleted gracefully and successfully")
      else:
         print("The expense was not found.")
      break

def update():
   expense_a = input("what is the name of your expense you wish to update")
   for expense_id,expense in expenses.items():
      if expense.name == expense_a:
         decision = input(" what do you want to change about your expense :name/desc/amount/month ")
         if decision.lower() == "name":
            new_name = input("please input your new name")
            expense.name = new_name
         elif decision.lower() == "dsc":
            new_dsc = input("What is the new description.")
            expense.dsc = new_dsc
         elif decision.lower() == "month":
            new_month = input ("What is the new month.")
            expense.month = new_month
         elif decision.lower() == "budget_amount":
            new_amount = input("What is the new buget_amount")
            expense.budget_amount = float( new_amount)
         else:
            print("Invalid Input")
         break
   else: 
         print("expense not found")
 


   with open(expense_f,"w") as f:
      json.dump(serialize(),f)
      return data

   


def summarize():
   decision =int(input( """Would you like a summary of a specific month
   if so enter the month."""))
   total = 0
   for expense_id,expense in expenses.items():
     
      if expense.month == decision:
         print("calculating...")
         total += expense.budget_amount
   print(f"Your total expenditure for {expense.month} is {total}ksh")

def summarize_all():
   decision = input("Would you like to get a summary or a reciept of your expenses.")
   if decision.lower() == "yes":
      print("summarizing..")
      total = 0
      #I want to print the month and total
      for expense_id,expense in expenses.items(): 
            total += expense.budget_amount
            print(f"{expense.month} : {expense.budget_amount}")
            print(f"Your total expenditure for {expense.month} is {total}  ")

def serialize():
   data = {}
   for expense_id,expense in expenses.items():
      data[expense_id] = {
         "name" : expense.name,
         "dsc" : expense.dsc,
         "budget_amount" : expense.budget_amount,
         "month" : expense.month,
      }

   
def deserialize():
   data = {}
   expenses = {}
   for expense_id, expense in data.items():
      expenses[expense_id] = Expense(
         expense["name"],
         expense["dsc"],
         expense["month"],
         expense["budgeted_amount"]
      )
      return expenses
      

while 1>0:
   do = input("""----------------------------------------------------------
              Welcome to expense tracker cli -----:
               If you want to view all expenses - press v
              If you want to update all expenses - press u
              if you want to summarrize all expenses - press s
              if you want to add an expense - press o
              If you want to quit the meny press q""")
   if do.lower() == "v":
       view()
   elif do.lower() == "u":
       update()
   elif do.lower() == "s":
       summarize()
   elif do.lower() == "o":
       add()
   elif do.lower() == "q":
       break
   else:
      print("Your input doesnt match my db  ")









