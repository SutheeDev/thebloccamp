from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
from functools import wraps
import cs50
from datetime import datetime
import calendar

app = Flask(__name__)

db = cs50.SQL("sqlite:///shows.db")

# Get band info from the database
allInfo = db.execute("SELECT * FROM shows ORDER BY date")
for i in range(len(allInfo)):
    # Get the date column, which is string and alter them into a datetime object
    ymd_str = allInfo[i]['date']
    datetime_obj = datetime.strptime(ymd_str, '%Y-%m-%d').date()
    # Get date from the datetimeobject
    day_num = datetime_obj.day
    # Get the day name from the datetimeobject
    day = datetime_obj.strftime('%A')
    # Get month from the datetimeobject
    month = calendar.month_abbr[datetime_obj.month]
    # Get year from the datetimeobject
    year = datetime_obj.strftime('%Y')
    # Append date, day, month, year back to the allInfo dictionary
    allInfo[i]['day_num'] = day_num
    allInfo[i]['day'] = day
    allInfo[i]['month'] = month
    allInfo[i]['year'] = year


@app.route('/')
def index():
    fourUpcoming = []
    # Want to have 4 slides in the slideshow, so append the first four shows from the allInfo to a new list called fourUpcoming
    for i in range(4):
        fourUpcoming.append(allInfo[i])
    return render_template('index.html', allInfo=allInfo, fourUpcoming=fourUpcoming)


@app.route('/shows')
def shows():
    return render_template('shows.html', allInfo=allInfo)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        # Passed the 'Get Tickets.eachInfo['id']' in the shows page
        # So need to extract the band id out of the name attribute here
        for key in request.form:
            if key.startswith('Get Tickets.'):
                id = key.partition('.')[-1]
                # Obtain the band info from the database using the extracted id
                bandInfos = db.execute("SELECT * FROM shows WHERE id = ?", id)
                # Change date column to the datetime object
                ymd_str = bandInfos[0]['date']
                datetime_obj = datetime.strptime(ymd_str, '%Y-%m-%d').date()
                # Append back to the bandInfos
                bandInfos[0]['day_num'] = datetime_obj.day
                bandInfos[0]['day'] = datetime_obj.strftime('%A')
                bandInfos[0]['month'] = calendar.month_abbr[datetime_obj.month]
                bandInfos[0]['year'] = datetime_obj.strftime('%Y')
        return render_template('tickets.html', bandInfos=bandInfos)
    return render_template('tickets.html')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')


@app.route('/subscribed', methods=['POST'])
def subscribed():
    if request.method == 'POST':
        # Get information from the form input
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email-address')

        # Handle error if a user doesn't fill in all fields
        if not firstname or not lastname or not email:
            error_statement = '* All form fields are required'
            return render_template('subscribe.html', error_statement=error_statement)

        # Utilize smtplib library to notify the page admin via email
        message = "You've been subscribed to the Bloc Camp email newsletter"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("sutheedevtest@gmail.com", os.environ.get('MY_PASSWORD'))
        server.sendmail("sutheedevtest@gmail.com", email, message)

        # Add subscriber info into the subscribers table
        db.execute("INSERT INTO subscribers (firstname, lastname, email) VALUES (?, ?, ?)",
                   firstname, lastname, email)
        return render_template('subscribed.html', firstname=firstname)

    return redirect('subscribe.html')
