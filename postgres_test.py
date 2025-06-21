import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="my_first_db",  # change to your database name
    user="postgres",     # change if your username is different
    password="Postgredb@sql"  # use the password you set during install
)

# Create a cursor to perform operations
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
""")
conn.commit()

def add_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    print(f"User {name} added successfully.")

def update_user_by_id():
    user_id = int(input("Enter the user ID to update: "))
    name = input("Enter the new name: ")
    age = int(input("Enter the new age: "))
    cur.execute("UPDATE students SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
    conn.commit()
    print(f"User ID {user_id} updated successfully.")

def view_all_users():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_user_by_name():
    name = input("Enter the name of the user to search: ")
    cur.execute("SELECT * FROM students WHERE name = %s", (name,))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No user found with that name.")

def delete_user_by_id():
    user_id = int(input("Enter the user ID to delete: "))
    cur.execute("DELETE FROM students WHERE id = %s", (user_id,))
    conn.commit()
    print(f"User ID {user_id} deleted successfully.")

def menu():
    while True:
        print("\nSelect an operation:")
        print("1. Add User")
        print("2. Update User by ID")
        print("3. View All Users")
        print("4. Search User by Name")
        print("5. Delete User by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()

# Clean up
cur.close()
conn.close()
