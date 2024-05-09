 

#-----------------------------------------19/03-01---------------------------------
from flask import Flask, render_template, request, redirect, url_for, session, flash
import psycopg2
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# PostgreSQL Connection
def connect_to_postgres():
    return psycopg2.connect("postgres://mqtt:QUfHMq15UqYIhsUXI6DkXW6na0A5155R@dpg-co3ef021hbls73f0enbg-a.singapore-postgres.render.com/mqttdevices")

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
        try:
            conn = connect_to_postgres()
            cursor = conn.cursor()
            
            # Insert user into the database
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, hashed_password))
            conn.commit()
            
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        except psycopg2.Error as e:
            flash('Error registering user. Please try again.', 'danger')
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()
   
    return render_template('admin/register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
        try:
            conn = connect_to_postgres()
            cursor = conn.cursor()
            
            # Check if the username and password match
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, hashed_password))
            user = cursor.fetchone()
            
            if user:
                session['username'] = username  # Store the username in the session
                flash('Login successful.', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid username or password. Please try again.', 'danger')
                return redirect(url_for('login'))
        except psycopg2.Error as e:
            flash('Error logging in. Please try again.', 'danger')
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    return render_template('admin/login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


# Dashboard route
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if user is not logged in
    
     # Check if filters are applied
    apply_filters = 'applyFilters' in request.args
    
    data = []
    try:
        conn = connect_to_postgres()
        cursor = conn.cursor()
        # Get parameters from the query string
        name = request.args.get('Name')
        # machine_id = request.args.get('machine_id')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        # Fetch data from MySQL based on the provided filters
       
        if name:
            sql = "SELECT machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l,  updated_at FROM mqtt_devices WHERE Name = %s"
            cursor.execute(sql, (name,))
        elif start_date and end_date:
            sql = "SELECT machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l,  updated_at FROM mqtt_devices WHERE updated_at BETWEEN %s AND %s"
            cursor.execute(sql, (start_date, end_date))
        else:
            # If no filters provided, fetch all data
            sql = "SELECT machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, Name, updated_at FROM mqtt_devices"
            cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()
       
        # Process the fetched data into a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "machine_id": row[0],
                "v": row[1],
                "c": row[2],
                "p": row[3],
                "tt": row[4],
                "at": row[5],
                # "l": row[6].decode('utf-8'),
                "l": int(row[6]),
                "name": row[7],
                # "updated_at": row[8].isoformat()  # Convert datetime object to ISO format string
                
            })
        
    except psycopg2.Error as e:
        flash('An error occurred while fetching data from the database.', 'danger')
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
        

    # Render the template with the fetched data
    return render_template('admin/dashboard.html', data=data, filters_applied=apply_filters)
    


# Dashboard route
@app.route('/test/admin/dashboard')
def test_admin_dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if user is not logged in
    
     # Check if filters are applied
    apply_filters = 'applyFilters' in request.args
    
    data = []
    try:
        conn = connect_to_postgres()
        cursor = conn.cursor()
        # Get parameters from the query string
        name = request.args.get('name')
        # machine_id = request.args.get('machine_id')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        # Fetch data from MySQL based on the provided filters
        if name:
            sql = "SELECT machine_id, test_v,  test_p, test_at,  updated_at FROM mqtt_devices_two WHERE name = %s"
            cursor.execute(sql, (name,))
            print("debug3")
        elif start_date and end_date:
            sql = "SELECT machine_id, test_v,  test_p, test_at,  updated_at FROM mqtt_devices_two WHERE updated_at BETWEEN %s AND %s"
            cursor.execute(sql, (start_date, end_date))
            
        else:
            # If no filters provided, fetch all data
            sql = "SELECT machine_id, test_v,  test_p, test_at,  name, updated_at FROM mqtt_devices_two"
            cursor.execute(sql)
           

        # Fetch all rows
        rows = cursor.fetchall()
       
        # Process the fetched data into a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "machine_id": row[0],
                "v": row[1],
                "p": row[2],
                "at": row[3],
                "name": row[4],
                # "updated_at": row[4].isoformat()  # Convert datetime object to ISO format string
                
            })
        
    except psycopg2.Error as e:
        flash('An error occurred while fetching data from the database.', 'danger')
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
        

    # Render the template with the fetched data
    return render_template('admin/test_dashboard.html', data=data, filters_applied=apply_filters)
    
 

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(port=5001, debug=True)
