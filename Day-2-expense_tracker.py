expenses = {}

def add_expense():

    print("How many expenses you want to add :")
    num = int(input().strip())

    for _ in range(num):

        print("Category Name :")
        cat = input().strip()

        print("Expense made :")
        exp = int(input().strip())

        if cat in expenses:
            expenses[cat].append(exp)
        else:
            expenses[cat] = [exp]

def view_expense():

    if not expenses:
        print("no expenses recorded")
        return

    for key,values in expenses.items():
        print(f"{key} : {values}")

def view_expense_category():

    if not expenses:
        print("no expenses recorded")
        return
    else:
        print("Type Category : ")

        c = input().strip()

        if c not in expenses:
            print(f" {c} category not found")
        else:
            print(f"{c} : {expenses[c]}")

def total_expense():
    total_exp = 0 

    if not expenses:
        print("no expenses recorded")
        return
    else:
        for value in expenses.values():
            total_exp += sum(value)
    
    print(f"The total expenes is : {total_exp}")

def total_expense_category():

    if not expenses:
        print("no expenses recorded")
        return 
    else:
        print("Enter Category Name :")
        cate= input().strip()
        total = 0 
        if cate in expenses:
            total = sum(expenses[cate])
        print(f" The total of {cate} is {total}")
    
def max_expense():

   # max_exp = {}
   # for key,values in expenses.items():
   #     max_exp[key] = sum(values)
    max_category = max(expenses, key=lambda k: sum(expenses[k]))

    print(max_category)

            

def main():

    print("Add expense - 1")
    print("View expense - 2")
    print("view expense as pre category - 3")
    print("Total Expense - 4")
    print("Total as per category - 5")
    print("Max Expense - 6")
    print("Exit - 7 ")

    try:
        n = int(input().strip())
    except ValueError:
        print("Invalid input. Enter a number between 1 and 4.")
        return True 
    
    if n == 1:
        add_expense()
        return True
    
    elif n == 2:
        view_expense()
        return True
    
    elif n == 3:
        view_expense_category()
        return True
   
    elif n == 4:
        total_expense()
        return True
    
    elif n == 5:
        total_expense_category()
        return True
    
    elif n == 6:
        max_expense()
        return True   
    
    elif n == 7:
        print("-----EXiT-----")
        return False
    
    
if __name__ == "__main__":
    while True:
        if not main():

            break
