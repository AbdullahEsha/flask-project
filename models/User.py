# # models/user.py
# from config.db import db
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime

# class User(db.Model):  # Make sure this inherits from db.Model
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     role = db.Column(db.String(50), default='user')
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     def __init__(self, name, email, password, role='user'):
#         self.name = name
#         self.email = email
#         self.password = generate_password_hash(password)  # Store hashed password
#         self.role = role

#     def check_password(self, password):
#         return check_password_hash(self.password, password)
