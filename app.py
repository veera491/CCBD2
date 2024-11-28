from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            dob TEXT NOT NULL,
                            gender TEXT NOT NULL,
                            address TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
        conn.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''INSERT INTO users (name, dob, gender, address, email, password)
                                  VALUES (?, ?, ?, ?, ?, ?)''', (name, dob, gender, address, email, password))
                conn.commit()
                return render_template('success.html')
            except sqlite3.IntegrityError:
                flash("Email already exists. Please use a different email.")
                return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
            user = cursor.fetchone()
            if user:
                return render_template('show_data.html', users=[user])
            else:
                flash("The Given Data was Wrong")
                return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/show_data')
def show_data():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return render_template('show_data.html', users=users)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
