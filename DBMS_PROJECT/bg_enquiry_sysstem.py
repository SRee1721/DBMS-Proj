from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

# Replace these values with your actual Oracle database connection details
oracle_username = "system"
oracle_password = "Srinivas17"

oracle_service_name = "XE"

# Set up Oracle database connection
dsn_tns = cx_Oracle.makedsn( service_name=oracle_service_name)
oracle_connection = cx_Oracle.connect(user=oracle_username, password=oracle_password, dsn=dsn_tns)
oracle_cursor = oracle_connection.cursor()

# Example route for rendering the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission, authenticate user with the Oracle database, etc.
        # (Note: This is a placeholder, replace with your actual logic)
        entered_username = request.form['username']
        entered_password = request.form['password']

        # Implement your authentication logic here
        # ...

        return redirect(url_for('booking'))

    return render_template('login.html')

# Example route for rendering the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form submission, insert user into the Oracle database, etc.
        # (Note: This is a placeholder, replace with your actual logic)
        new_username = request.form['username']
        new_password = request.form['password']
        phone_number = request.form['phone']
        address = request.form['address']

        # Implement your registration logic here
        # ...

        return redirect(url_for('login'))

    return render_template('register.html')

# Example route for rendering the booking page
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle form submission, search for trains in the Oracle database, etc.
        # (Note: This is a placeholder, replace with your actual logic)
        source_station = request.form['source']
        destination_station = request.form['destination']

        # Implement your search trains logic here
        # ...

        return render_template('booking.html', results=results)

    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)
