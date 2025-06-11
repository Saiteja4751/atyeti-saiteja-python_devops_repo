from flask import Flask, render_template_string
import os
import mysql.connector

app = Flask(__name__)

# ✅ Reusable DB connection function
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# HTML with button
home_template = """
<h2>✅ Table created and sample data inserted!</h2>
<form action="/data">
    <button type="submit">View Data</button>
</form>
"""

# Route to create table and insert sample data
@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100)
            );
        """)

        # Insert data only if table is empty
        cursor.execute("SELECT COUNT(*) FROM users;")
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');")
            conn.commit()

        cursor.close()
        conn.close()
        return render_template_string(home_template)
    except Exception as e:
        return f"❌ Database error: {str(e)}"

# Route to display rows
@app.route('/data')
def show_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        html = "<h2>📋 Users Table</h2><table border='1'><tr><th>ID</th><th>Name</th></tr>"
        for row in rows:
            html += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
        html += "</table><br><a href='/'>⬅ Back</a>"
        return html
    except Exception as e:
        return f"❌ Failed to fetch data: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
