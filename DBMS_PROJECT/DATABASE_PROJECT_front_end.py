import tkinter as tk
from tkinter import messagebox
import cx_Oracle
import random
import string
import random

# Function to authenticate the user


def authenticate(username, password):
    cursor.execute('''
        SELECT * FROM Passenger
        WHERE user_name = :username AND password = :password
    ''', {'username': username, 'password': password})
    return cursor.fetchone() is not None

# Function to handle login button click


def login_clicked():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    user_exists = username_exists(entered_username)

    if user_exists and authenticate(entered_username, entered_password):
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


def username_exists(username):
    cursor.execute('''
        SELECT * FROM Passenger
        WHERE user_name = :username
    ''', {'username': username})
    return cursor.fetchone() is not None

# Function to handle register button click


def admin():
    admin_window = tk.Toplevel()
    admin_window.title("ADMIN PAGE")

    pass


def register_clicked():
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
        register_window, reg_username_entry.get(), reg_password_entry.get(), phone_number_entry.get(), address_entry.get()))
    register_button.pack(pady=10)

# Function to register a new user


def register(register_window, username, password, phone_number, address):
    if username_exists(username):
        username = username + generate_username_suffix()

    cursor.execute('''
        INSERT INTO Passenger (user_name, password, phone_number, address)
        VALUES (:username, :password, :phone_number, :address)
    ''', {'username': username, 'password': password, 'phone_number': phone_number, 'address': address})

    connection.commit()
    messagebox.showinfo("Registration Successful",
                        "User registered successfully!")
    register_window.destroy()

# Function to generate a random username suffix


def generate_username_suffix():
    return ''.join(random.choices(string.digits + string.ascii_letters, k=4))

# Function to open the booking window after successful login


def open_booking_window():
    global booking_window  # Declare booking_window as global
    booking_window = tk.Toplevel(root)
    booking_window.title("Booking Window")

    try:
        cursor.execute('''
            SELECT DISTINCT s.Station_id, t.Train_id, s.Station_name, t.Train_name, sc.Schedule_id, sc.TIme_arrival, sc.Time_departure
            FROM Schedule sc
            JOIN Train t ON sc.Train_id = t.Train_id
            JOIN Station s ON s.Station_id = sc.Station_id
        ''')
        stations = cursor.fetchall()

        if not stations:
            messagebox.showinfo("No Stations", "No stations available.")
            return

        station_label = tk.Label(
            booking_window, text="Available Stations and Trains:")
        station_label.pack(pady=5)

        for station in stations:
            station_info_label = tk.Label(
                booking_window, text=f"STATION_ID : {station[0]} - TRAIN_ID: {station[1]} - STATION_NAME : {station[2]}- TRAIN_NAME: {station[3]}- SCHEDULE_ID: {station[4]}- TIME_ARRIVAL: {station[5]}- TIME_DEPARTURE: {station[6]}")
            station_info_label.pack()

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

login_button = tk.Button(root, text="Login", command=login_clicked)
login_button.pack(pady=10)

register_button = tk.Button(root, text="Register", command=register_clicked)
register_button.pack(pady=10)

# Connect to Oracle database without specifying host, port, and service name
# Replace the following placeholder values with your actual Oracle database server details
username = "system"
password = "Srinivas17"

# Connection string directly using SID (XE)
connection = cx_Oracle.connect(f"{username}/{password}@XE")
cursor = connection.cursor()

# Global variable to store the current passenger ID

current_passenger_id = None
print(current_passenger_id)

# Start the main event loop
root.mainloop()

# Close the database connection
cursor.close()
connection.close()
