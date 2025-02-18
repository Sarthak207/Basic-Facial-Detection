import cv2
import face_recognition
import sqlite3
import numpy as np
from datetime import datetime

# Load database
conn = sqlite3.connect('employees.db')
c = conn.cursor()
c.execute("SELECT name, encoding FROM employees")
data = c.fetchall()

known_names = []
known_encodings = []

for row in data:
    name = row[0]
    encoding = np.array([float(val) for val in row[1].split(',')])  # Convert stored string back to numpy array
    known_names.append(name)
    known_encodings.append(encoding)

# Open video capture
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # Resize for speed
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            matched_index = matches.index(True)
            name = known_names[matched_index]

            # Log Entry Time
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO logs (name, timestamp) VALUES (?, ?)", (name, timestamp))
            conn.commit()

        # Draw rectangle around face
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Employee Entry System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
conn.close()
