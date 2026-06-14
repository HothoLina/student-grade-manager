# 🎓 Student Grade Manager System

A Python + MySQL backend project that manages students and their grades using a full CRUD system with reporting and database relationships.

---

## 🚀 Features

- Add new students
- View all students in a table format
- Search students by name
- Update student information
- Delete students (with cascade delete for grades)
- Add grades for students
- View grades per student
- Calculate average grade
- Generate full student performance report
- Input validation and error handling

---

## 🛠️ Tech Stack

- Python 3
- MySQL
- MySQL Connector
- Tabulate (for clean CLI tables)

---

## 🗄️ Database Structure

### Students Table
| Field | Type |
|------|------|
| id | INT (Primary Key) |
| name | VARCHAR |
| email | VARCHAR (Unique) |

### Grades Table
| Field | Type |
|------|------|
| id | INT (Primary Key) |
| student_id | INT (Foreign Key) |
| subject | VARCHAR |
| grade | FLOAT |

---

## 🔗 Relationship

- One student → Many grades
- Cascade delete enabled:
  - If a student is deleted → all their grades are automatically deleted

---

## 📊 Key SQL Concepts Used

- INSERT INTO
- SELECT
- UPDATE
- DELETE
- WHERE
- LIKE
- AVG()
- FOREIGN KEY
- ON DELETE CASCADE

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/student-grade-manager.git

2. Move into the project folder
cd student-grade-manager
3. Create virtual environment
python -m venv venv
4. Activate virtual environment
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux
5. Install dependencies
pip install -r requirements.txt
6. Create MySQL database
CREATE DATABASE student_management;
7. Run the project
python main.py
📌 Project Structure
student-grade-manager/
│
├── main.py
├── db.py
├── student.py
├── grade.py
├── requirements.txt
├── README.md
📈 Example Report Output
===== STUDENT REPORT =====

Name: Amira Ahmed
Email: amiraahmed@email.com

Subjects:
+----------+--------+
| Subject  | Grade  |
+----------+--------+
| Math     | 95     |
| science  | 83      |
| history  | 70      |
+----------+--------+

Average Grade: 82.67
Performance: Very Good


💡 What I Learned
Building a backend system from scratch
Connecting Python with MySQL
Designing relational databases
CRUD operations
Writing SQL queries
Handling errors in real applications
Structuring a full project like a developer
👨‍💻 Author

Built by HothoLina as part of a backend development learning journey.


---

