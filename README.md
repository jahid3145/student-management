# 🎓 Student Management System (Python)

A **console-based Student Management System** developed using Python.  
This project demonstrates **CRUD operations (Create, Read, Update, Delete)** using **file handling**, making it an excellent beginner-to-intermediate Python mini project.

---

## 🚀 Features

- ➕ Add new student records
- 👀 View all students
- ✏️ Update existing student details
- ❌ Delete student records
- 💾 Data stored persistently using a text file
- 📋 Menu-driven console interface

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Core Concepts:**
  - File Handling (`read`, `write`, `append`)
  - Functions
  - Conditional Statements
  - Loops
  - String Manipulation
  - Exception Handling

---

## 📂 Project Structure

Student_Management_System/
│
├── student_management_system.py
├── students.txt
└── README.md

yaml
Copy code

- `students.txt` → Stores student records persistently

---

## ▶️ How to Run the Project

### Prerequisites
- Python **3.x** installed

### Steps
1. Clone or download the repository
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the program:

```bash
python student_management_system.py
📋 Menu Options
pgsql
Copy code
==== Student Management System ====
1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Exit
📝 Student Data Format (File Storage)
Each student record is stored in students.txt as:

pgsql
Copy code
StudentID,Name,Age,Course
Example:
Copy code
101,John,20,Computer Science
🧠 How It Works
Student data is stored in a text file (students.txt)

Each operation reads from or writes to the file

Update and delete operations rewrite the file after modification

Program runs continuously until the user exits

⚠️ Limitations
No input validation for duplicate IDs

Uses plain text file (no database)

Console-based only

No authentication system

🔮 Future Enhancements
Add input validation

Prevent duplicate student IDs

Use CSV or database (SQLite/MySQL)

Add search functionality

Add GUI using Tkinter

Add student result/marks management

👨‍💻 Author
Name: Jahid

Course: BTech CSE (AI Specialization)

Purpose: Python mini project to practice file handling and CRUD operations

⭐ Support
If you found this project useful:

⭐ Star the repository

🍴 Fork it

📢 Share it with others

Happy Coding! 🚀
