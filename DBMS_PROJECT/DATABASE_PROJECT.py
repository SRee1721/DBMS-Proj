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
            CREATE TABLE Train (
                Train_id VARCHAR(10),
                Train_name VARCHAR(10),
                Train_type VARCHAR(10),
                PRIMARY KEY (Train_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE Station (
                Station_id VARCHAR(10),
                Station_name VARCHAR(20),
                PRIMARY KEY (Station_id)
                
            )
        """)
        cursor.execute("""
            CREATE TABLE Schedule (
                Schedule_id VARCHAR(10),
                Train_id VARCHAR(10),
                Station_id VARCHAR(10),
                Time_Departure VARCHAR(10),
                Time_arrival VARCHAR(10),
                PRIMARY KEY (Schedule_id),
                FOREIGN KEY  (Train_id) REFERENCES Train(Train_id) ON DELETE CASCADE,
                FOREIGN KEY  (Station_id) REFERENCES Station(Station_id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE Ticket (
                Ticket_id VARCHAR(10),
                Train_id VARCHAR(10),
                Schedule_id VARCHAR(10),
                Board_station VARCHAR(10),
                Arrival_station VARCHAR(10),
                NO_OF_TICKETS INT,
                PRIMARY KEY (Ticket_id),
                FOREIGN KEY  (Train_id) REFERENCES Train(Train_id) ON DELETE CASCADE,
                FOREIGN KEY  (Schedule_id) REFERENCES Schedule(Schedule_id) ON DELETE CASCADE,
                FOREIGN KEY  (Board_station) REFERENCES Station(Station_id) ON DELETE CASCADE,
                FOREIGN KEY  (Arrival_station) REFERENCES Station(Station_id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
           CREATE TABLE Reservation (
                                Passenger_id VARCHAR(10),
                                TKT_id VARCHAR(100),
                                
                                FOREIGN KEY (Passenger_id)REFERENCES PASSENGER (PASSENGER_ID)
                                
                                    )""")
        cursor.execute("""
            CREATE TABLE Cost (
                Ticket_id VARCHAR(10),
                Train_id VARCHAR(10),
                Board_station VARCHAR(10),
                Arrival_station VARCHAR(10),
                cost INT,
                FOREIGN KEY  (Train_id) REFERENCES Train(Train_id) ON DELETE CASCADE,
                FOREIGN KEY  (Board_station) REFERENCES Station(Station_id) ON DELETE CASCADE,
                FOREIGN KEY  (Arrival_station) REFERENCES Station(Station_id) ON DELETE CASCADE,
                FOREIGN KEY  (Ticket_id) REFERENCES Ticket(Ticket_id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""Create Table Admin(
            user_name varchar(20),
            password varchar(20),
            Admin_id Number,
            PRIMARY KEY(Admin_id))""")

        print("TABLES CREATED SUCCESSFULLY : ")
        cursor.close()
    except cx_Oracle.Error as e:
        print(f"Error: {e}")


'''def insert_values(connection, Train_id, Train_id1, Train_name, Train_type, Station_id, Station_1, Station_name, Schedule_id, Time_Arrival, Time_Departure, Board_station, Arrival_station, Ticket_id, NO_OF_Tickets, cost):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Train VALUES (:Train_id, :Train_name, :Train_type)",
                       {'Train_id': Train_id, 'Train_name': Train_name, 'Train_type': Train_type})
        cursor.execute("INSERT INTO Station VALUES(:Station_id,:Train_id,:Station_name)",
                       {'Station_id': Station_id, 'Train_id': Train_id, 'Station_name': Station_name})
        cursor.execute("INSERT INTO Station VALUES(:Station_id,:Train_id,:Station_name)",
                       {'Station_id': Station_1, 'Train_id': Train_id1, 'Station_name': Station_name})
        cursor.execute("INSERT INTO Schedule VALUES(:Schedule_id,:Train_id,:Station_id,:Time_Arrival,:Time_Departure)",
                       {'Schedule_id': Schedule_id, 'Train_id': Train_id, 'Station_id': Station_id, 'Time_Arrival': Time_Arrival, 'Time_Departure': Time_Departure})

        cursor.execute("INSERT INTO Ticket VALUES(:Ticket_id,:Train_id,:Schedule_id,:Board_station,:Arrival_station,:NO_OF_Tickets)",
                       {'Ticket_id': Ticket_id, 'Train_id': Train_id, 'Schedule_id': Schedule_id, 'Board_station': Board_station, 'Arrival_station': Arrival_station, 'NO_OF_Tickets': NO_OF_Tickets})
        cursor.execute("INSERT INTO Cost VALUES(:Ticket_id,:Train_id,:Board_station,:Arrival_station,:cost)",
                       {'Ticket_id': Ticket_id, 'Train_id': Train_id, 'Board_station': Board_station, 'Arrival_station': Arrival_station, 'cost': cost})

        print("VALUES INSERTED SUCCESSFULLY ! ")
        cursor.close()
        connection.commit()
    except cx_Oracle.Error as e:
        print(f"Error :{e}")'''


oracle_connection = connect_to_oracle()
if oracle_connection:
    create_tables(oracle_connection)
    '''insert_values(oracle_connection, 'T100', 'T200', 'VAIGAI', 'EXPRESS', 'S100', 'S200',
                  'MADURAI', 'SC300', '00:00:00', '6:40 am', 'TK200', 'S100', 'S200', 3, 500)'''
