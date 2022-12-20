from flask import Flask, render_template, request, redirect, url_for, g, redirect, session
# from flask_session import Session
from functools import wraps
import cs50
from datetime import datetime
import calendar

app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

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
    allInfo[i]['day'] = day
    allInfo[i]['month'] = month
    allInfo[i]['year'] = year


@app.route('/')
def index():
    fourUpcoming = []
    for i in range(4):
        fourUpcoming.append(allInfo[i])
    return render_template('index.html', allInfo=allInfo, fourUpcoming=fourUpcoming)


@app.route('/shows', methods=['GET', 'POST'])
def shows():
    if request.method == 'POST':
        # if request.form.get('Get Tickets') == 'Get Tickets':
        return render_template('tickets.html')

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


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():

    # email = request.form.get('email')

    # if not email:
    #     return redirect(url_for('index')+'#subscribe-form')

    return render_template('subscribe.html')


@app.route('/subscribed', methods=['GET', 'POST'])
def subscribed():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email-address')
        db.execute("INSERT INTO subscribers (firstname, lastname, email) VALUES (?, ?, ?)",
                   firstname, lastname, email)
        return render_template('subscribed.html', firstname=firstname)

    return redirect('subscribe.html')
