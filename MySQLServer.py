import mysql.connector
import os
try:
    connection = mysql.connector.connect(
        user =os.environ.get('DB_USER'),
        host ="127.0.0.1",
        password =os.environ.get('DB_PASS'),

    )

    my_cursor = connection.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    
    if connection.is_connected():
        print("'alx_book_store' created successfully!")
        
    connection.commit()
    my_cursor.close()
    connection.close()
    print(connection.is_connected())
    
except mysql.connector.Error as e:
    print(f"Error:{e}")

    