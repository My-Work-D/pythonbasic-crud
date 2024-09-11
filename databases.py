

import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ijse@2001",
            database="user_data"
        )
        self.mycursor = self.mydb.cursor()
        self.create_table()

    def create_table(self):
        self.mycursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                password INT,
                email VARCHAR(255)
            )
        """)
        print("Table created (if not exists).")

    def insert_user(self, name, password, email):
        sql = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)"
        val = (name, password, email)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(f"{self.mycursor.rowcount} record inserted.")

    def get_all_users(self):
        self.mycursor.execute("SELECT * FROM users")
        return self.mycursor.fetchall()

    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()
        print("Database connection closed.")


class UserApp:
    def __init__(self, root):
        self.db = Database()

        self.root = root
        self.root.title("User Registration")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")  # Background color

        # Styling
        self.label_font = ("Arial", 12)
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        self.button_bg = "#4CAF50"  # Button color
        self.button_fg = "white"  # Button text color

        # Name label and entry
        self.name_label = tk.Label(root, text="Name:", font=self.label_font, bg="#f0f0f0")
        self.name_label.pack(pady=10)
        self.name_entry = tk.Entry(root, font=self.entry_font, width=30)
        self.name_entry.pack(pady=5)

        # Password label and entry
        self.password_label = tk.Label(root, text="Password:", font=self.label_font, bg="#f0f0f0")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(root, show="*", font=self.entry_font, width=30)
        self.password_entry.pack(pady=5)

        # Email label and entry
        self.email_label = tk.Label(root, text="Email:", font=self.label_font, bg="#f0f0f0")
        self.email_label.pack(pady=10)
        self.email_entry = tk.Entry(root, font=self.entry_font, width=30)
        self.email_entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_user, font=self.button_font, bg=self.button_bg, fg=self.button_fg)
        self.submit_button.pack(pady=20)

        # View Users button
        self.view_users_button = tk.Button(root, text="View Users", command=self.view_users, font=self.button_font, bg=self.button_bg, fg=self.button_fg)
        self.view_users_button.pack(pady=5)

    def submit_user(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        if name and password and email:
            self.db.insert_user(name, int(password), email)
            messagebox.showinfo("Success", "User added successfully!")
            self.clear_entries()  # Clear the entries after submission
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def view_users(self):
        users = self.db.get_all_users()
        if users:
            users_info = "\n".join([f"ID: {user[0]}, Name: {user[1]}, Email: {user[3]}" for user in users])
            messagebox.showinfo("Users", users_info)
        else:
            messagebox.showinfo("No Users", "No users found in the database.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def on_closing(self):
        self.db.close_connection()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
