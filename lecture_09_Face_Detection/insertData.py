import sqlite3
import face_recognition
import numpy as np

# Example to insert an employee's data
employee_name = "Sarthak Pardeshi"
# Load the image and encode the face
image = face_recognition.load_image_file("pf.png")
encoding = face_recognition.face_encodings(image)[0]
encoding_str = ','.join(map(str, encoding))  # Convert encoding to a string for storage

# Connect to SQLite database
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Insert employee data into the table
c.execute("INSERT INTO employees (name, encoding) VALUES (?, ?)", (employee_name, encoding_str))

# Commit and close
conn.commit()
conn.close()
