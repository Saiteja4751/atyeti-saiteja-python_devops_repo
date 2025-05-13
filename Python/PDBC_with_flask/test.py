from flask import *

app = Flask(__name__)
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')

    if uname == 'ayush' and passwrd == 'admin':
        return f"✅ Welcome, {uname}!"
    else:
        return "❌ Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
