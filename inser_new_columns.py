import psycopg2

def add_column_to_table():
    try:
        # Connect to your database
        conn = psycopg2.connect("postgres://mqtt:QUfHMq15UqYIhsUXI6DkXW6na0A5155R@dpg-co3ef021hbls73f0enbg-a.singapore-postgres.render.com/mqttdevices")
        
        # Create a cursor object
        cur = conn.cursor()
        
        # SQL statement to add a new column
        cur.execute("ALTER TABLE mqtt_devices_two ADD COLUMN test_at Float")
        
        # Commit the changes to the database
        conn.commit()
        
        print("Column added successfully.")
        
    except psycopg2.Error as e:
        print(f"Error adding column: {e}")
    finally:
        # Close the cursor and connection to so the server can allocate
        # bandwidth to other requests
        if cur:
            cur.close()
        if conn:
            conn.close()

# Example usage
add_column_to_table()
