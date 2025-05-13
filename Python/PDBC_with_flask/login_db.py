from flask import Flask, request, render_template_string
import pymysql

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',  # replace with your password
        database='login_db'
    )

# Login Page (GET)
@app.route('/')
def login_form():
    return '''
        <h2>Login Form</h2>
        <form action="/login" method="post">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

# Handle Login (POST)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if user exists
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            return f"<h3>✅ Welcome back, {username}!</h3>"
        else:
            # Insert new user
            insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            conn.commit()
            return f"<h3>🆕 New user '{username}' created successfully!</h3>"

    except pymysql.MySQLError as e:
        return f"<h3>❌ Database error: {e}</h3>"

    finally:
        if conn and conn.open:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
