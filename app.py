from flask import Flask, render_template, request, redirect, url_for
import cs50

app = Flask(__name__)
db = cs50.SQL("sqlite:///shows.db")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shows')
def shows():
    allartists = db.execute("SELECT artist FROM shows")
    return render_template('shows.html', allartists=allartists)


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
