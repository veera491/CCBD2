from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:veera491@localhost:5432/ccbd_db'
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
    users = User.query.all()
    return render_template('show_data.html', users=users)


# Route: Show All Data
@app.route('/show_data')
def show_data():
    users = User.query.all()
    return render_template('show_data.html', users=users)

# Initialize database tables (using app context)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
