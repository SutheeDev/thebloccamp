from flask import Flask, render_template, request, redirect, url_for
import cs50
from datetime import datetime
import calendar

app = Flask(__name__)
db = cs50.SQL("sqlite:///shows.db")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shows')
def shows():
    # Get all the band's name from database
    allartists = db.execute("SELECT artist, description FROM shows")
    # Get all the event date from database
    dates_data = db.execute("SELECT date FROM shows")
    dates = []
    months = []
    years = []

    for i in range(len(dates_data)):
        ymd_str = dates_data[i]['date']
        # Convert a string of date into datetime object
        datetime_obj = datetime.strptime(ymd_str, '%Y-%m-%d').date()

        # Use calendar module to get the abbreviation of month and append to the months list
        months.append(calendar.month_abbr[datetime_obj.month])

        # Get year from datetime object and append to the years list
        year = datetime_obj.strftime("%Y")
        years.append(year)
        # dates.append(datetime_obj)

    # for i in range(len(dates_data)):
    #     ymd = dates_data[i]['date']
    #     yearStr = ''
    #     for i in range(4):
    #         yearStr += ymd[i]
    #     yearInt = int(yearStr)
    #     year = yearInt.strftime("%Y")
    #     dates.append(year)

        # dates.append(dates_data[i]['date'])
    #     return dates

    return render_template('shows.html', allartists=allartists, months=months, years=years)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/subscribe', methods=['POST'])
def subscribe():

    email = request.form.get('email')

    if not email:
        return redirect(url_for('index')+'#subscribe-form')

    return redirect(url_for('index'))
