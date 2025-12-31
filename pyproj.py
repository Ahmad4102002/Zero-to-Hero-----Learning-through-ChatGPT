Marks_Studs = {}

def add_students():
    print("enter student name :")
    student_name = input().strip()
    
    Marks_Studs[student_name] = []

def add_marks():
    if not Marks_Studs:
        return None
    
    print("enter student name :")
    student_name = input().strip()

    for key,values in Marks_Studs.items():
        if student_name != key:
            print(f"student with name {student_name} not found")
        elif student_name == key:
            print("enter marks for chemistry :")
            chem = int(input().strip())
            print("enter marks for physics :")
            phys = int(input().strip())
            print("enter marks for maths :")
            maths = int(input().strip())

            Marks_Studs[student_name] = [chem,phys,maths]

def check_marks():
    for key,values in Marks_Studs.items():
        print(key,values)
        

def main():

    print("Add Student - 1 ")
    print("Add Marks - 2 ")
    print("Check Marks - 3 ")

    user = int(input().strip())
    
    if user == 1:
        add_students() 
    
   
    if  user == 2:
        add_marks()
        if add_marks is None:
            print("Student not found") 

    
    if user == 3:
        check_marks()

if __name__ == "__main__":
    while True:
        main()