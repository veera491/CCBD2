from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpassword@localhost:5432/ccbd_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Test database connection
with app.app_context():  # Ensure you are within the app context
    try:
        # Create all tables (if not already created)
        db.create_all()
        print("Database connected successfully")
    except Exception as e:
        print(f"Error connecting to database: {e}")
