from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Veera@491@localhost:5432/ccbd_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Route: Home
@app.route('/')
def home():
    return render_template('home.html')

# Route: Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']

        # Add user to the database
        new_user = User(name=name, dob=dob, gender=gender, address=address, email=email, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return render_template('success.html')
        except:
            db.session.rollback()
            flash("Email already exists. Please use a different email.")
            return redirect(url_for('register'))

    return render_template('register.html')

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Verify user credentials
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return render_template('show_data.html', users=[user])
        else:
            flash("The Given Data was Wrong")
            return redirect(url_for('login'))

    return render_template('login.html')

# Route: Show All Data
@app.route('/show_data')
def show_data():
    users = User.query.all()
    return render_template('show_data.html', users=users)

# Initialize database tables
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
