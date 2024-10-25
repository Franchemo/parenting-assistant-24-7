import sqlite3
import hashlib
import os
from datetime import datetime

class Database:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        # Create users table
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        ''')
        
        # Create user_profiles table
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_profiles (
                user_id INTEGER PRIMARY KEY,
                child_age TEXT,
                child_personality TEXT,
                kindergarten TEXT,
                interests TEXT,
                languages TEXT,
                family_members INTEGER,
                has_siblings TEXT,
                siblings_age TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password, email):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            
            hashed_password = self.hash_password(password)
            c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                     (username, hashed_password, email))
            
            conn.commit()
            return True, "Registration successful"
        except sqlite3.IntegrityError as e:
            if "username" in str(e):
                return False, "Username already exists"
            elif "email" in str(e):
                return False, "Email already exists"
            return False, "Registration failed"
        finally:
            conn.close()

    def verify_user(self, username, password):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        hashed_password = self.hash_password(password)
        c.execute('SELECT id FROM users WHERE username = ? AND password = ?',
                 (username, hashed_password))
        
        result = c.fetchone()
        
        if result:
            # Update last login time
            c.execute('UPDATE users SET last_login = ? WHERE id = ?',
                     (datetime.now(), result[0]))
            conn.commit()
            
        conn.close()
        return result[0] if result else None

    def save_user_profile(self, user_id, profile_data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        try:
            c.execute('''
                INSERT OR REPLACE INTO user_profiles 
                (user_id, child_age, child_personality, kindergarten, interests, 
                languages, family_members, has_siblings, siblings_age)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, profile_data.get('child_age'), profile_data.get('child_personality'),
                 profile_data.get('kindergarten'), profile_data.get('interests'),
                 profile_data.get('languages'), profile_data.get('family_members'),
                 profile_data.get('has_siblings'), profile_data.get('siblings_age')))
            
            conn.commit()
            return True, "Profile saved successfully"
        except Exception as e:
            return False, f"Failed to save profile: {str(e)}"
        finally:
            conn.close()

    def get_user_profile(self, user_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        c.execute('SELECT * FROM user_profiles WHERE user_id = ?', (user_id,))
        result = c.fetchone()
        
        conn.close()
        
        if result:
            return {
                'child_age': result[1],
                'child_personality': result[2],
                'kindergarten': result[3],
                'interests': result[4],
                'languages': result[5],
                'family_members': result[6],
                'has_siblings': result[7],
                'siblings_age': result[8]
            }
        return None
