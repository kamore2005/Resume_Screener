from flask_bcrypt import Bcrypt
import MySQLdb

# Initializing bcrypt
bcrypt = Bcrypt()

# Connecting to MySQL Database
db = MySQLdb.connect(host="localhost", user="root", passwd="kartik@2005", db="resume_screener")
cursor = db.cursor()

# Setting Admin Credentials
username = "admin"
password = bcrypt.generate_password_hash("password123").decode("utf-8")  # Hash the password

# Check if user already exists
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
existing_user = cursor.fetchone()

if existing_user:
    print(" User 'admin' already exists. Skipping insertion.")
else:
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    print(" User created successfully!")

db.close()

