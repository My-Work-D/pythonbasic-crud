import sys
sys.path.append('C:/Users/sachi/Downloads/MyTestProject/newtest/pythonbasic')
from databases import Database

class User:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.password = int(input("Enter your password: "))
        self.email = input("Enter your email: ")

    def __str__(self):
        return f"Name: {self.name}, Password: {self.password}, Email: {self.email}"

# Create a database object
db = Database()

# Get user input
user = User()
print(user)

# Insert user into the database
db.insert_user(user.name, user.password, user.email)

# Retrieve and display all users from the database
db.get_all_users()

# Close the database connection
db.close_connection()
