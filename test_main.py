# from flask import Flask, render_template, request, redirect, url_for, session, flash
# import psycopg2
# import hashlib
# conn = None
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # PostgreSQL Connection
# def connect_to_postgres():
#     return psycopg2.connect("postgres://mqtt:QUfHMq15UqYIhsUXI6DkXW6na0A5155R@dpg-co3ef021hbls73f0enbg-a.singapore-postgres.render.com/mqttdevices")
# @app.route('/register', methods=['GET', 'POST'])
# def register():
   
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
#         try:
#             conn = connect_to_postgres()
#             cursor = conn.cursor()
            
#             # Insert user into the database
#             sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
#             cursor.execute(sql, (username, hashed_password))
#             conn.commit()
            
#             flash('Registration successful. Please log in.', 'success')
#             return redirect(url_for('login'))
#         except psycopg2.Error as e:
#             flash('Error registering user. Please try again.', 'danger')
#             print("Error:", e)
#         finally:
#             if cursor is not None:
#                 cursor.close()
#             if conn is not None:
#                 conn.close()
   
#     return render_template('admin/register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
   
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
#         cursor=None
#         # conn= None
#         conn = connect_to_postgres()
#         cursor = conn.cursor()
#         try:
            
            
            
#             # Check if the username and password match
#             sql = "SELECT * FROM users WHERE username = %s AND password = %s"
#             cursor.execute(sql, (username, hashed_password))
#             user = cursor.fetchone()
            
#             if user:
#                 session['username'] = username  # Store the username in the session
#                 flash('Login successful.', 'success')
#                 return redirect(url_for('admin_dashboard'))
#             else:
#                 flash('Invalid username or password. Please try again.', 'danger')
#                 return redirect(url_for('login'))
#         except psycopg2.Error as e:
#             flash('Error logging in. Please try again.', 'danger')
#             print("Error:", e)
#         finally:
#             if cursor is not None:
#                 cursor.close()
#             if conn is not None:
#                 conn.close()

#     return render_template('admin/login.html')

# # Logout route
# @app.route('/logout')
# def logout():
#     session.pop('username', None)  # Remove the username from the session
#     flash('You have been logged out.', 'success')
#     return redirect(url_for('login'))


# # test_Dashboard route
# @app.route('main/admin/dashboard')
# def admin_dashboard():
#     if 'username' not in session:
#         return redirect(url_for('login'))  # Redirect to login if user is not logged in
#     data = []
#     print("debug1")
#     try:
#         conn = connect_to_postgres()
#         cursor = conn.cursor()
#         # Get parameters from the query string
#         name = request.args.get('name')
#         # machine_id = request.args.get('machine_id')
#         start_date = request.args.get('start_date')
#         end_date = request.args.get('end_date')

#         # Fetch data from MySQL based on the provided filters
        
#         if name:
#             sql = "SELECT machine_id, test_v,  test_p,  name,  updated_at FROM mqtt_devices_two WHERE name = %s"
#             cursor.execute(sql, (name,))
#             print("debug3")
#         elif start_date and end_date:
#             sql = "SELECT machine_id, test_v,  test_p,  name,  updated_at FROM mqtt_devices_two WHERE updated_at BETWEEN %s AND %s"
#             cursor.execute(sql, (start_date, end_date))
            
#         else:
#             # If no filters provided, fetch all data
#             sql = "SELECT machine_id, test_v,  test_p,  name, updated_at FROM mqtt_devices_two"
#             cursor.execute(sql)
           

#         # Fetch all rows
#         rows = cursor.fetchall()
#         print("rows",rows)
#         # Process the fetched data into a list of dictionaries
#         data = []
#         for row in rows:
#             data.append({
#                 "machine_id": row[0],
#                 "v": row[1],
#                 "p": row[2],
#                 # "at": row[4],
#                 "name": row[3],
#                 # "updated_at": row[4].isoformat()  # Convert datetime object to ISO format string
                
#             })

#     except psycopg2.Error as e:
#         flash('An error occurred while fetching data from the database.', 'danger')
#         print("Error:", e)
#     finally:
#         cursor.close()
#         conn.close()
   
#     # Render the template with the fetched data
#     return render_template('admin/dashboard.html', data=data)

 

# if __name__ == '__main__':
#     app.run(debug=True)
