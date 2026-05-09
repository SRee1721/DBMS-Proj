import tkinter as tk

import cx_Oracle
import random
import string
import re
from tkinter import ttk, messagebox

# Function to authenticate the user
# Function to authenticate the user


def authenticate(username, password, is_admin=False):
    table_name = "Admin" if is_admin else "Passenger"
    cursor.execute(f'''
        SELECT * FROM {table_name}
        WHERE user_name = :username AND password = :password
    ''', {'username': username, 'password': password})
    result = cursor.fetchone()
    print("Authentication Result:", result)
    return result is not None


# Function to handle login button click
def login_clicked(is_admin=False):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    user_exists = username_exists(entered_username, is_admin)

    if user_exists and authenticate(entered_username, entered_password, is_admin):
        if is_admin:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            open_admin_window()
        else:
            messagebox.showinfo("Login Successful",
                                "Welcome, " + entered_username + "!")
            open_booking_window()
    elif user_exists:
        messagebox.showerror(
            "Login Failed", "Incorrect password for the provided username.")
    else:
        messagebox.showerror(
            "Login Failed", "Username does not exist. Click the Register button.")

# Function to check if a username exists in the database


def username_exists(username, is_admin=False):
    table_name = "Admin" if is_admin else "Passenger"
    cursor.execute(f'''
        SELECT * FROM {table_name}
        WHERE user_name = :username
    ''', {'username': username})
    return cursor.fetchone() is not None

# Function to handle register button click


def register_clicked(is_admin=False):
    register_window = tk.Toplevel(root)
    register_window.title("Registration Page")

    reg_username_label = tk.Label(register_window, text="Username:")
    reg_username_label.pack(pady=5)

    reg_username_entry = tk.Entry(register_window)
    reg_username_entry.pack(pady=5)

    reg_password_label = tk.Label(register_window, text="Password:")
    reg_password_label.pack(pady=5)

    reg_password_entry = tk.Entry(register_window, show="*")
    reg_password_entry.pack(pady=5)

    phone_number_label = tk.Label(register_window, text="Phone Number:")
    phone_number_label.pack(pady=5)

    phone_number_entry = tk.Entry(register_window)
    phone_number_entry.pack(pady=5)

    address_label = tk.Label(register_window, text="Address:")
    address_label.pack(pady=5)

    address_entry = tk.Entry(register_window)
    address_entry.pack(pady=5)

    register_button = tk.Button(register_window, text="Register", command=lambda: register(
        register_window, reg_username_entry.get(), reg_password_entry.get(), phone_number_entry.get(), address_entry.get(), is_admin))
    register_button.pack(pady=10)

# Function to register a new user


def register(register_window, username, password, phone_number, address, is_admin=False):
    if username_exists(username, is_admin):
        messagebox.showerror("Registration Failed", "Username already exists.")
        return

    # Validate password
    if not validate_password(password):
        messagebox.showerror(
            "Registration Failed", "Password must be at least 8 characters long and include at least 1 lowercase, 1 uppercase, 1 numeric, and 1 special character.")
        return

    # Validate phone number
    if not validate_phone_number(phone_number):
        messagebox.showerror(
            "Registration Failed", "Invalid phone number. Please enter a 10-digit number.")
        return

    cursor.execute(f'''
        INSERT INTO {"Admin" if is_admin else "Passenger"} (user_name, password, phone_number, address)
        VALUES (:username, :password, :phone_number, :address)
    ''', {'username': username, 'password': password, 'phone_number': phone_number, 'address': address})

    connection.commit()
    messagebox.showinfo("Registration Successful",
                        "User registered successfully!")
    register_window.destroy()

# Function to validate password


def validate_password(password):
    # Minimum length of 8 characters
    if len(password) < 8:
        return False

    # At least 1 lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # At least 1 uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # At least 1 numeric digit
    if not re.search(r'\d', password):
        return False

    # At least 1 special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all conditions are met, the password is valid
    return True

# Function to validate phone number


def validate_phone_number(phone_number):
    # Include your phone number validation logic here
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to open the admin window after successful login


def open_admin_window():
    admin_window = tk.Toplevel(root)
    admin_window.title("ADMIN PAGE")

    add_train_button = tk.Button(
        admin_window, text="Add Train", command=add_train)
    add_train_button.pack(pady=10)

    delete_train_button = tk.Button(
        admin_window, text="Delete Train", command=delete_train)
    delete_train_button.pack(pady=10)

    change_routes_button = tk.Button(
        admin_window, text="Change Routes", command=change_routes)
    change_routes_button.pack(pady=10)

# Function to handle add train button click


def add_train():
    add_train_window = tk.Toplevel(root)
    add_train_window.title("Add Train")

    train_name_label = tk.Label(add_train_window, text='Train Name:')
    train_name_label.pack(pady=5)

    train_name_entry = tk.Entry(add_train_window)
    train_name_entry.pack(pady=5)

    train_id_label = tk.Label(add_train_window, text='Train ID:')
    train_id_label.pack(pady=5)

    train_id_entry = tk.Entry(add_train_window)
    train_id_entry.pack(pady=5)

    add_train_button = tk.Button(add_train_window, text="Add Train", command=lambda: insert_train(
        train_name_entry.get(), train_id_entry.get(), add_train_window))
    add_train_button.pack(pady=10)


def insert_train(train_name, train_id, add_train_window):
    try:
        cursor.execute('''
            INSERT INTO Train (Train_id, Train_name)
            VALUES (:train_id, :train_name)
        ''', {'train_id': train_id, 'train_name': train_name})
        connection.commit()
        messagebox.showinfo("Train Added", "Train added successfully!")
        add_train_window.destroy()
    except cx_Oracle.Error as e:
        messagebox.showerror("Error", f"Error adding train: {e}")


def delete_train():
    delete_train_window = tk.Toplevel(root)
    delete_train_window.title("Delete Train")

    train_name_label = tk.Label(delete_train_window, text='Train Name:')
    train_name_label.pack(pady=5)

    train_name_entry = tk.Entry(delete_train_window)
    train_name_entry.pack(pady=5)

    train_id_label = tk.Label(delete_train_window, text='Train ID:')
    train_id_label.pack(pady=5)

    train_id_entry = tk.Entry(delete_train_window)
    train_id_entry.pack(pady=5)

    delete_train_button = tk.Button(delete_train_window, text="Delete Train", command=lambda: remove_train(
        train_name_entry.get(), train_id_entry.get(), delete_train_window))
    delete_train_button.pack(pady=10)


def remove_train(train_name, train_id, delete_train_window):
    try:
        # Include logic to delete a train and its related data from the Train, Schedule, Ticket, and Cost tables
        # ...
        cursor.execute('''
            DELETE FROM Train
            WHERE Train_id = :train_id AND Train_name = :train_name
        ''', {'train_id': train_id, 'train_name': train_name})
        connection.commit()
        messagebox.showinfo("Train Deleted", "Train deleted successfully!")
        delete_train_window.destroy()
    except cx_Oracle.Error as e:
        messagebox.showerror("Error", f"Error deleting train: {e}")


# Function to handle change routes button click
def change_routes():
    # Include logic to change routes in the Schedule and Ticket tables
    pass

# Function to open the booking window after successful login


def open_booking_window():
    global booking_window  # Declare booking_window as global
    booking_window = tk.Toplevel(root)
    booking_window.title("Booking Window")

    try:
        cursor.execute('''
            SELECT DISTINCT s.Station_id, t.Train_id, s.Station_name, t.Train_name, sc.Schedule_id, sc.Time_arrival, sc.Time_departure
            FROM Schedule sc
            JOIN Train t ON sc.Train_id = t.Train_id
            JOIN Station s ON s.Station_id = sc.Station_id
        ''')
        stations = cursor.fetchall()

        if not stations:
            messagebox.showinfo("No Stations", "No stations available.")
            return

        # Create Treeview widget
        tree = ttk.Treeview(booking_window)
        tree["columns"] = ("Station ID", "Train ID", "Station Name",
                           "Train Name", "Schedule ID", "Time Arrival", "Time Departure")

        # Define Treeview columns
        tree.column("#0", width=0, stretch=tk.NO)  # Empty column
        tree.column("Station ID", anchor=tk.W, width=80)
        tree.column("Train ID", anchor=tk.W, width=80)
        tree.column("Station Name", anchor=tk.W, width=120)
        tree.column("Train Name", anchor=tk.W, width=120)
        tree.column("Schedule ID", anchor=tk.W, width=80)
        tree.column("Time Arrival", anchor=tk.W, width=120)
        tree.column("Time Departure", anchor=tk.W, width=120)

        # Define Treeview headings
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Station ID", text="Station ID", anchor=tk.W)
        tree.heading("Train ID", text="Train ID", anchor=tk.W)
        tree.heading("Station Name", text="Station Name", anchor=tk.W)
        tree.heading("Train Name", text="Train Name", anchor=tk.W)
        tree.heading("Schedule ID", text="Schedule ID", anchor=tk.W)
        tree.heading("Time Arrival", text="Time Arrival", anchor=tk.W)
        tree.heading("Time Departure", text="Time Departure", anchor=tk.W)

        # Insert data into Treeview
        for station in stations:
            tree.insert("", "end", values=station)

        # Pack the Treeview
        tree.pack(expand=True, fill="both")

        source_label = tk.Label(booking_window, text="Source Station:")
        source_label.pack(pady=5)

        source_entry = tk.Entry(booking_window)
        source_entry.pack(pady=5)

        destination_label = tk.Label(
            booking_window, text="Destination Station:")
        destination_label.pack(pady=5)

        destination_entry = tk.Entry(booking_window)
        destination_entry.pack(pady=5)

        search_button = tk.Button(
            booking_window, text="Search Train(s)", command=lambda: search_trains(
                source_entry.get(), destination_entry.get()))
        search_button.pack(pady=10)
    except cx_Oracle.Error as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")


def search_trains(source_station, destination_station):
    try:
        cursor.execute('''
            SELECT DISTINCT t.Train_id, t.Train_name, c.Ticket_id, c.cost,c.Board_station,c.Arrival_station,ti.NO_OF_TICKETS
            FROM Cost c
            JOIN Station s1 ON c.Board_station = s1.Station_id
            JOIN Station s2 ON c.Arrival_station = s2.Station_id
            JOIN TICKET ti ON c.Ticket_id=ti.Ticket_id
            JOIN Train t ON c.Train_id = t.Train_id
            WHERE s1.Station_name = :source_station AND s2.Station_name = :destination_station
        ''', {'source_station': source_station, 'destination_station': destination_station})

        results = cursor.fetchall()
        print(results)

        if not results:
            messagebox.showinfo(
                "No Trains", "No trains available for the given route.")
        else:
            for result in results:
                train_info_label = tk.Label(
                    booking_window, text=f"Train: {result[1]}, Cost: {result[3]},TICKETS AVALIABLE:{result[6]}")
                train_info_label.pack()

                book_button = tk.Button(
                    booking_window, text="Book", command=lambda train_id=result[0], ticket_id=result[2], train_name=result[1], cost=result[3]: book_ticket(
                        train_id, result[4], result[5], train_name, cost, ticket_id))

                book_button.pack()

    except cx_Oracle.Error as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")


def book_ticket(train_id, board_station, arrival_station, train_name, cost, ticket_id):
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)

        c = random.randint(0, 9)
        d = random.randint(0, 9)
        e = random.randint(0, 9)
        f = random.randint(0, 9)
        current_passenger_id = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
        # Update the number of tickets in the Ticket table
        # Insert into the Reservation table
    # Check availability of the selected ticket
        cursor.execute('''
            SELECT NO_OF_TICKETS
            FROM Ticket
            WHERE Ticket_id = :ticket_id
        ''', {'ticket_id': ticket_id})

        ticket_availability = cursor.fetchone()

        if ticket_availability and ticket_availability[0] > 0:
            # Insert into the Reservation table
            ticket_id_fin = str(ticket_id)+current_passenger_id
            cursor.execute('''
    INSERT INTO Reservation (Passenger_id, TKT_id)
    VALUES (:passenger_id, :ticket_id_fin)
''', {'passenger_id': current_passenger_id, 'ticket_id_fin': ticket_id_fin})

            # Update the availability in the Ticket table
            cursor.execute('''
                UPDATE Ticket
                SET NO_OF_TICKETS = NO_OF_TICKETS - 1
                WHERE Ticket_id = :ticket_id
            ''', {'ticket_id': ticket_id})

            connection.commit()
            messagebox.showinfo("Booking Successful", f"Ticket booked for Train {
                                train_name}. Cost: {cost}")
        else:
            messagebox.showinfo(
                "Booking Failed", "Selected ticket not available.")

    except cx_Oracle.Error as e:
        print(e)
        messagebox.showerror("Error", f"Error booking ticket: {e}")


# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place login widgets
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

user_login_button = tk.Button(
    root, text="Login as User", command=lambda: login_clicked(is_admin=False))
user_login_button.pack(pady=10)

admin_login_button = tk.Button(
    root, text="Login as Admin", command=lambda: login_clicked(is_admin=True))
admin_login_button.pack(pady=10)

register_button = tk.Button(root, text="Register",
                            command=lambda: register_clicked(is_admin=False))
register_button.pack(pady=10)


# Connect to Oracle database and create necessary tables
# Replace the following placeholder values with your actual Oracle database server details
username = "system"
password = "system"
connection = cx_Oracle.connect(f"{username}/{password}@XE")
cursor = connection.cursor()

# Global variable to store the current passenger ID
current_passenger_id = None

# Start the main event loop
root.mainloop()

# Close the database connection
cursor.close()
connection.close()
