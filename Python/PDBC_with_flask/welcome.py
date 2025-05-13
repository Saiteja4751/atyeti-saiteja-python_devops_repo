from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='flaskdb'
    )

# ------------------------
# 1️⃣ Welcome Page
# ------------------------
@app.route('/')
def welcome():
    return render_template('welcome.html')

# ------------------------
# 2️⃣ Insert User
# ------------------------
@app.route('/insert-form')
def insert_form():
    return render_template('insert.html')

@app.route('/insert', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        insert_query = "INSERT INTO users1 (name, email) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, email))
        conn.commit()

        return f"""
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0fdf4;
                color: #2e7d32;
                padding: 40px;
                margin: 100px auto;
                max-width: 600px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                text-align: center;">
        <h2 style="margin-bottom: 20px;">✅ New user '<span style='color:#1b5e20;'>{name}</span>' added successfully!</h2>
        <a href="/" style="
            display: inline-block;
            padding: 12px 24px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            transition: background-color 0.3s ease;">
            🏠 Back to Welcome Page
        </a>
    </div>
"""


    except pymysql.MySQLError as e:
        return f"❌ Error inserting user: {e}"

    finally:
        if conn and conn.open:
            conn.close()

# ------------------------
# 3️⃣ Update User
# ------------------------
@app.route('/update-form')
def update_form():
    return render_template('update.html')

@app.route('/update', methods=['POST'])
def update_user():
    user_id = request.form['id']
    new_name = request.form['name']
    new_email = request.form['email']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        update_query = "UPDATE users1 SET name=%s, email=%s WHERE id=%s"
        cursor.execute(update_query, (new_name, new_email, user_id))
        conn.commit()

        return f"""
        <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #e3f2fd;
                color: #1565c0;
                padding: 40px;
                margin: 100px auto;
                max-width: 600px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                text-align: center;">
        <h2 style="margin-bottom: 20px;">
            ✅ User with ID <span style='color:#0d47a1;'>{user_id}</span> updated successfully!
        </h2>
        <a href="/" style="
            display: inline-block;
            padding: 12px 24px;
            background-color: #1976d2;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            transition: background-color 0.3s ease;">
            🏠 Back to Welcome Page
        </a>
    </div>
"""


    except pymysql.MySQLError as e:
        return f"❌ Error updating user: {e}"

    finally:
        if conn and conn.open:
            conn.close()

# ------------------------
# 4️⃣ View All Users
# ------------------------
@app.route('/view')
def view_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users1")
        users = cursor.fetchall()
        return render_template('view.html', users=users)

    except pymysql.MySQLError as e:
        return f"❌ Error retrieving data: {e}"

    finally:
        if conn and conn.open:
            conn.close()


# ------------------------
# 4️⃣ delete the specific user Users
# ------------------------

@app.route('/delete-form')
def delete_form():
    return render_template('delete.html')



@app.route('/delete', methods=['POST'])
def delete_user():
    user_id = request.form['id']
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Step 1: Delete the user
        delete_query = "DELETE FROM users1 WHERE id = %s"
        cursor.execute(delete_query, (user_id,))
        conn.commit()

        # Step 2: Reorder the IDs (Reset Serial Numbers)
        # Create a temp column if not exists (only once)
        cursor.execute("ALTER TABLE users1 DROP COLUMN IF EXISTS temp_id")
        cursor.execute("ALTER TABLE users1 ADD COLUMN temp_id INT")

        # Step 3: Update temp_id sequentially
        cursor.execute("SET @count = 0")
        cursor.execute("UPDATE users1 SET temp_id = (@count := @count + 1)")

        # Step 4: Drop old ID and rename temp_id
        cursor.execute("ALTER TABLE users1 DROP COLUMN id")
        cursor.execute("ALTER TABLE users1 CHANGE temp_id id INT NOT NULL PRIMARY KEY AUTO_INCREMENT")

        conn.commit()

        return f"""
        <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #fbe9e7;
                    color: #d84315;
                    padding: 40px;
                    margin: 100px auto;
                    max-width: 600px;
                    border-radius: 12px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                    text-align: center;">
            <h2>🗑️ User with ID <span style='color:#bf360c;'>{user_id}</span> deleted successfully!</h2>
            <p>✅ ID column has been reordered!</p>
            <a href="/" style="
                display: inline-block;
                padding: 12px 24px;
                background-color: #ff7043;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                font-size: 16px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
                transition: background-color 0.3s ease;">
                🏠 Back to Welcome Page
            </a>
        </div>
        """

    except pymysql.MySQLError as e:
        return f"❌ Error deleting or resetting user IDs: {e}"

    finally:
        if conn and conn.open:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)