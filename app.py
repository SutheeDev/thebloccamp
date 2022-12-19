from flask import Flask, render_template, request, redirect, url_for
import cs50
from datetime import datetime
import calendar

app = Flask(__name__)
db = cs50.SQL("sqlite:///shows.db")

allInfo = db.execute("SELECT * FROM shows")
for i in range(len(allInfo)):
    ymd_str = allInfo[i]['date']
    datetime_obj = datetime.strptime(ymd_str, '%Y-%m-%d').date()
    day_num = datetime_obj.day
    day = datetime_obj.strftime('%A')
    month = calendar.month_abbr[datetime_obj.month]
    year = datetime_obj.strftime('%Y')
    allInfo[i]['day_num'] = day_num
    allInfo[i]['day'] = day[:3]
    allInfo[i]['month'] = month
    allInfo[i]['year'] = year


@app.route('/')
def index():
    return render_template('index.html', allInfo=allInfo)


@app.route('/shows')
def shows():
    return render_template('shows.html', allInfo=allInfo)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/subscribe', methods=['POST'])
def subscribe():

    email = request.form.get('email')

    if not email:
        return redirect(url_for('index')+'#subscribe-form')

    return redirect(url_for('index'))
