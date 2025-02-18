from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

def fetch_logs():
    conn = sqlite3.connect('employees.db')
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df

@app.route('/')
def home():
    logs = fetch_logs()
    return render_template("index.html", tables=[logs.to_html()], titles=[''])

if __name__ == '__main__':
    app.run(debug=True)
