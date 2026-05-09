import string
import random
from tkinter import messagebox
import cx_Oracle


def connect_to_oracle():
    try:
        connection = cx_Oracle.connect('system/Srinivas17@XE')
        print("Connected to Oracle Database")
        return connection
    except cx_Oracle.Error as e:
        print(f"Error:{e}")


def create_tables(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
                    create Table Train
                    (
                    Train_id varchar(10),
                    Train_name varchar(10),
                    Train_type varchar(10),
                    Primary Key(Train_id)
                    )
                    """)
        cursor.execute("""
                        create Table Reservation
                    (
                    Passenger_id varchar(10),
                    Ticket_id varchar(10),
                    phone_number int,
                    address varchar(20),
                    Primary Key(Passenger_id),
                    Foreign Key (Ticket_id) references Ticket(Ticket_id),
                    
                    )
                    """)
        cursor.execute("""
                        create table Station
                    (
                    Station_id varchar(10),
                    Train_id varchar(10),
                    Station_name varchar(20),
                    Primary Key(Station_id),
                    Foreign Key (Train_id) References Train(Train_id)
                    )
                    """)
        cursor.execute("""
                        create Table Schedule
                    (Schedule_id varchar(10),
                        Train_id varchar(10),
                        Station_id  varchar(10),
                        Time_arrival varchar(10),
                        Time_Departure varchar(10),
                    Primary Key(Schedule_id),
                    Foreign Key (Train_id) references Train(Train_id),
                    Foreign Key (Station_id) references Station(Station_id)
                    )
                    """)
        cursor.execute("""
                        create table ticket
                    ( 
                    Ticket_id varchar(10),
                    Train_id varchar(10),
                    Schedule_id varchar(10),
                    Board_station varchar(10),
                    Arrival_station varchar(10),
                    NO_OF_Tickets int,
                    Primary Key(Ticket_id),
                    Foreign Key (Train_id) references Train(Train_id),
                    Foreign Key (Schedule_id) references Schedule(Schedule_id),
                    Foreign Key (Board_station) references Station(Station_id),
                    Foreign Key (Arrival_station) references Station(Station_id)
                        )
                        """)
        cursor.execute("""
                        create table Cost
                    (
                    Ticket_id varchar(10),
                    Train_id varchar(10),
                    Board_station varchar(10),
                    Arrival_station varchar(10),
                    cost int,
                    Foreign Key (Train_id) references Train(Train_id),
                    Foreign Key (Board_station) references Station(Station_id),
                    Foreign Key (Arrival_station) references Station(Station_id),
                    Foreign Key (Ticket_id) references Ticket(Ticket_id)
                    )
                    """)
        print("TABLES CREATED SUCCESSFULLY : ")
        cursor.close()
    except cx_Oracle.Error as e:
        print(f"Error: {e}")


def insert_values(connection, Train_id, Train_id1, Train_name, Train_type, Station_id, Station_1, Station_name, Schedule_id, Time_Arrival, Time_Departure, Board_station, Arrival_station, Ticket_id, NO_OF_Tickets, cost):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Train VALUES (:Train_id, :Train_name, :Train_type)",
                       {'Train_id': Train_id, 'Train_name': Train_name, 'Train_type': Train_type})
        cursor.execute("INSERT INTO Station Values(:Station_id,:Train_id,:Station_name)",
                       {'Station_id': Station_id, 'Train_id': Train_id, 'Station_name': Station_name})
        cursor.execute("INSERT INTO Station Values(:Station_id,:Train_id,:Station_name)",
                       {'Station_id': Station_1, 'Train_id': Train_id1, 'Station_name': Station_name})
        cursor.execute("INSERT INTO Schedule VALUES(:Schedule_id,:Train_id,:Station_id,:Time_Arrival,:Time_Departure)",
                       {'Schedule_id': Schedule_id, 'Train_id': Train_id, 'Station_id': Station_id, 'Time_Arrival': Time_Arrival, 'Time_Departure': Time_Departure})

        cursor.execute("INSERT INTO Ticket VALUES(:Ticket_id,:Train_id,:Schedule_id,:Board_station,:Arrival_station,:NO_OF_Tickets)",
                       {'Ticket_id': Ticket_id, 'Train_id': Train_id, 'Schedule_id': Schedule_id, 'Board_station': Board_station, 'Arrival_station': Arrival_station, 'NO_OF_Tickets': NO_OF_Tickets})
        cursor.execute("INSERT INTO COST VALUES(:Ticket_id,:Train_id,:Board_station,:Arrival_station,:cost)",
                       {'Ticket_id': Ticket_id, 'Train_id': Train_id, 'Board_station': Board_station, 'Arrival_station': Arrival_station, 'cost': cost})

        print("VALUES INSERTED SUCCESSFULLY ! ")
        cursor.close()
        connection.commit()
    except cx_Oracle.Error as e:
        print(f"Error :{e}")


oracle_connection = connect_to_oracle()
if oracle_connection:
    ''' create_tables(oracle_connection)'''
    cursor = oracle_connection.cursor()
    cursor.execute('''
        SELECT DISTINCT s.Station_id, t.Train_id, s.Station_name, t.Train_name
        FROM Station s
        JOIN Train t ON s.Train_id = t.Train_id''')
    stations = cursor.fetchall()
    if not stations:
        print("No Stations", "No stations available.")
    else:
        print("Available Stations and Trains:")
        for station in stations:
            print(f"{station[0]} - {station[2]} - Train: {station[3]}")
    insert_values(oracle_connection, 'T100', 'T200', 'VAIGAI', 'EXPRESS', 'S100', 'S200',
                  'MADURAI', 'SC300', '00:00:00', '6:40 am', 'TK200', 'S100', 'S200', 3, 500)

    # front end
    import tkinter as tk

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
    # Check if the username already exists
    if username_exists(username):
        # If the username exists, generate a unique username by adding a random suffix
        username = username + generate_username_suffix()

    # Insert the new user into the database
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
    booking_window = tk.Toplevel(root)
    booking_window.title("Booking Window")

    # Display all available stations and their associated trains
    import tkinter as tk


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
    # Check if the username already exists
    if username_exists(username):
        # If the username exists, generate a unique username by adding a random suffix
        username = username + generate_username_suffix()

    # Insert the new user into the database
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
    booking_window = tk.Toplevel(root)
    booking_window.title("Booking Window")

    # Display all available stations and their associated trains
    try:
        cursor.execute('''
            SELECT DISTINCT s.Station_id,t.Train_id, s.Station_name, t.Train_name,sc.Schedule_id,sc.TIme_arrival,sc.Time_departure
        FROM Schedule sc
        JOIN Train t ON sc.Train_id = t.Train_id
        Join Station s ON s.Station_id=sc.Station_id
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
                booking_window, text=f"STATION_ID : {station[0]} - TRAIN_ID{station[1]} - STATION_NAME : {station[2]}- TRAIN_NAME {station[3]}- SCHEDULE_ID {station[4]}- TIME_ARRIVAL {station[5]}- TIME_DEPARTURE {station[6]}")
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
            booking_window, text="Search Trains", command=lambda: search_trains(
                source_entry.get(), destination_entry.get()))
        search_button.pack(pady=10)
    except cx_Oracle.Error as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")


def search_trains(source_station, destination_station):
    cursor.execute('''
        SELECT DISTINCT t.Train_id, t.Train_name, c.cost
        FROM Cost c
        JOIN Station s1 ON c.Board_station = s1.Station_id
        JOIN Station s2 ON c.Arrival_station = s2.Station_id
        JOIN Train t ON c.Train_id = t.Train_id
        WHERE s1.Station_name = :source_station AND s2.Station_name = :destination_station
    ''', {'source_station': source_station, 'destination_station': destination_station})

    results = cursor.fetchall()

    if not results:
        messagebox.showinfo(
            "No Trains", "No trains available for the given route.")
    else:
        messagebox.showinfo(
            "Trains Found", "Trains available for the given route:\n" + "\n".join(map(str, results)))


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

# Start the main event loop
root.mainloop()

# Close the database connection
cursor.close()
connection.close()


def search_trains(source_station, destination_station):
    cursor.execute('''
        SELECT DISTINCT t.Train_id, t.Train_name, c.Ticket_id,c.cost
        FROM Cost c
        JOIN Station s1 ON c.Board_station = s1.Station_id
        JOIN Station s2 ON c.Arrival_station = s2.Station_id
        JOIN Train t ON c.Train_id = t.Train_id
        WHERE s1.Station_name = :source_station AND s2.Station_name = :destination_station
    ''', {'source_station': source_station, 'destination_station': destination_station})

    results = cursor.fetchall()

    if not results:
        messagebox.showinfo(
            "No Trains", "No trains available for the given route.")
    else:
        messagebox.showinfo(
            "Trains Found", "Trains available for the given route:\n" + "\n".join(map(str, results)))


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

# Start the main event loop
root.mainloop()
