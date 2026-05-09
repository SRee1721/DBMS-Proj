import tkinter as tk
from tkinter import messagebox
import mysql.connector


def connect_to_database():
    try:
        # Replace 'your_database', 'your_username', and 'your_password' with your actual MySQL credentials
        db_connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        messagebox.showinfo("Success", "Connected to the database!")
        return db_connection
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None
