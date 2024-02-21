# from flask import Flask,render_template

# app = Flask(__name__)

# #main index file
# @app.route('/')
# def index():
#     return render_template('index.html', title="")

# #admin login
# @app.route('/admin/')
# def adminIndex():
#     return render_template('admin/index.html', title="Admin Login")

# #-------------user area------------

# #main index file
# @app.route('/user/')
# def userIndex():
#     return render_template('user/index.html', title="user login")



# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random
from datetime import datetime, timedelta

app = Flask(__name__)
Bootstrap(app)

# Generate random data
def generate_data():
    data = []
    now = datetime.now()
    for i in range(60):
        data.append({
            'datetime': now.strftime("%Y-%m-%d %H:%M:%S"),
            'hour': now.strftime("%Y-%m-%d %H"),
            'minute': now.strftime("%Y-%m-%d %H:%M"),
            'value': random.randint(0, 100)
        })
        if i % 60 == 0:  # Store hourly data
            data[-1]['value_hourly'] = random.randint(0, 100)
        now -= timedelta(seconds=60)
    return data

@app.route('/')
def dashboard():
    data = generate_data()
    return render_template('admin/dashboard.html', data=data)

@app.route('/filter', methods=['POST'])
def filter_data():
    date_filter = request.form.get('date_filter')
    time_filter = request.form.get('time_filter')
    data = generate_data()
    if date_filter:
        data = [item for item in data if item['datetime'].startswith(date_filter)]
    if time_filter:
        data = [item for item in data if item['datetime'].split()[1].startswith(time_filter)]
    return render_template('admin/dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
