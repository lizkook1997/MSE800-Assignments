import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="my_first_db", 
    user="postgres",     
    password="Postgredb@sql"  
)

# Create a cursor to perform database operations
cur = conn.cursor()

# Create 'students' table
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
""")

# Create 'course' table
cur.execute("""
    CREATE TABLE IF NOT EXISTS course (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        unit INTEGER
    )
""")

conn.commit()

# --- Function Definitions ---

def add_user():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    print(f"Student {name} added successfully.")

def update_user_by_id():
    user_id = int(input("Enter the student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    cur.execute("UPDATE students SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
    conn.commit()
    print(f"Student ID {user_id} updated successfully.")

def view_all_users():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_user_by_name():
    name = input("Enter the name to search: ")
    cur.execute("SELECT * FROM students WHERE name = %s", (name,))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No student found with that name.")

def delete_user_by_id():
    user_id = int(input("Enter the student ID to delete: "))
    cur.execute("DELETE FROM students WHERE id = %s", (user_id,))
    conn.commit()
    print(f"Student ID {user_id} deleted successfully.")

def insert_course():
    name = input("Enter course name: ")
    unit = int(input("Enter course unit: "))
    cur.execute("INSERT INTO course (name, unit) VALUES (%s, %s)", (name, unit))
    conn.commit()
    print(f"Course '{name}' added successfully.")

def search_course():
    print("Search course by:\n1. Course ID\n2. Student Name")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        course_id = input("Enter Course ID: ")
        cur.execute("SELECT * FROM course WHERE id = %s", (course_id,))
        result = cur.fetchone()
        if result:
            print("Course Found:", result)
        else:
            print("No course found with that ID.")

    elif choice == '2':
        student_name = input("Enter Student Name: ")
        cur.execute("SELECT * FROM students WHERE name = %s", (student_name,))
        student = cur.fetchone()
        if student:
            print(f"Student Found: ID={student[0]}, Name={student[1]}, Age={student[2]}")
        else:
            print("No student found with that name.")
    else:
        print("Invalid option.")

# --- Menu Loop ---
def menu():
    while True:
        print("\nSelect an operation:")
        print("1. Add User")
        print("2. Update User by ID")
        print("3. View All Users")
        print("4. Search User by Name")
        print("5. Delete User by ID")
        print("6. Insert Course")
        print("7. Search Course by ID or Student Name")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_user_by_id()
        elif choice == '3':
            view_all_users()
        elif choice == '4':
            search_user_by_name()
        elif choice == '5':
            delete_user_by_id()
        elif choice == '6':
            insert_course()
        elif choice == '7':
            search_course()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()

# Cleanup
cur.close()
conn.close()
