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
                age INT,
                weight FLOAT
            )
        """)
        print("Table created (if not exists).")

    def insert_user(self, name, age, weight):
        sql = "INSERT INTO users (name, age, weight) VALUES (%s, %s, %s)"
        val = (name, age, weight)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(f"{self.mycursor.rowcount} record inserted.")

    def get_all_users(self):
        self.mycursor.execute("SELECT * FROM users")
        myresult = self.mycursor.fetchall()
        for row in myresult:
            print(row)

    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()
        print("Database connection closed.")
