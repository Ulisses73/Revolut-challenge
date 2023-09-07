from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

# Helper function to validate the date format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# SQLite database setup
conn = sqlite3.connect('userdata.db')
conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        date_of_birth DATE
    )
''')
conn.close()

# API endpoint to save/update user data
@app.route('/hello/<username>', methods=['PUT'])
def save_user_data(username):
    data = request.get_json()

    if not username.isalpha():
        return 'Username must contain only letters.', 400

    dob = data.get('dateOfBirth')

    if not is_valid_date(dob):
        return 'Invalid date format. Please use YYYY-MM-DD.', 400

    today = datetime.now().date()
    dob_date = datetime.strptime(dob, '%Y-%m-%d').date()

    if dob_date >= today:
        return 'Date of birth must be before today.', 400

    try:
        conn = sqlite3.connect('userdata.db')
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO users (username, date_of_birth) VALUES (?, ?)', (username, dob))
        conn.commit()
        conn.close()
        return '', 204
    except Exception as e:
        return str(e), 500

# API endpoint to get birthday message
@app.route('/hello/<username>', methods=['GET'])
def get_birthday_message(username):
    try:
        conn = sqlite3.connect('userdata.db')
        cursor = conn.cursor()
        cursor.execute('SELECT date_of_birth FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return 'User not found', 404

        dob_date = datetime.strptime(row[0], '%Y-%m-%d').date()
        today = datetime.now().date()

        next_birthday = dob_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days
        if days_until_birthday == 0:
            message = f'Hello, {username}! Happy birthday!'
        else:
            message = f'Hello, {username}! Your birthday is in {days_until_birthday} day(s)'

        return jsonify({'message': message}), 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
