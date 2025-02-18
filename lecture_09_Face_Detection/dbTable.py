import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Create employees table (run this once)
c.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        encoding TEXT
    )
''')

# Create logs table (run this once)
c.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        timestamp TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
