'''
Student Management System (Python) 

Developed a console-based application using Python 

Implemented CRUD operations using file handling

Applied functions and conditional logic for data processing

'''

FILE_NAME ='students.txt'

# -------------------------------
# CREATE: Add a new student
# -------------------------------

def add_student():
    with open(FILE_NAME, "a") as file:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Age : "))
        course = input("Enter Course :")
        
        file.write(f"{student_id}  ,{name}  ,{age}  ,{course}\n")
        print(" Student Added Successfully!\n")

# -------------------------------
# READ: View all students
# -------------------------------

def view_student():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- Student Records ---")
            for line in file:
                line = line.strip()

                # Skip empty or invalid lines
                if not line or "," not in line:
                    continue

                student_id, name, age, course = line.split(",")
                print(f"ID: {student_id}, Name: {name}, Age: {age}, Course: {course}")
            print()
    except FileNotFoundError:
        print(" No student records found.\n")

# -------------------------------
# UPDATE: Modify student details
# -------------------------------

        
def update_student():
    student_id = input("Enter student ID to Update:")
    updated = False
    
    with open(FILE_NAME,"r") as file:
        lines = file.readlines()
        
    with open(FILE_NAME,"w") as file:
        for line in lines:
            data = line.strip().split(",")
            
            if data[0] == student_id:
                name = input("Enter New Name :")
                age = int(input("Enter New Age   : "))
                course =input("Enter new Course : ")
                file.write(f"{ student_id}  ,{name}  ,{age}  ,{course}\n")
                updated = True
            else:
                file.write(line)
    if updated:
        print("Student records updated Successfully!\n")
    else:
        print(" Student not found.\n")
        
# -------------------------------
# DELETE: Remove a student
# -------------------------------
        
        
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    deleted = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if line.startswith(student_id + ","):
                deleted = True
            else:
                file.write(line)

    if deleted:
        print(" Student deleted successfully!\n")
    else:
        print(" Student not found.\n")


# -------------------------------
# MAIN MENU
# -------------------------------

def student_Management_system():
    while True:
        print("====Student Management System===")
        print("1.Add Student")
        print("2.View Student")
        print("3.Update Student")
        print("4.Delete Student")
        print("5.Exit")
        
        choice = input("Enter Your choice(1-5): ")
        
        if choice == "1" :
            add_student()
        elif choice =="2":
            view_student()
        elif choice =="3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice =="5":
            print(" Exiting System. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")
student_Management_system()
            
        
        
    