from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


@app.route('/shows')
def shows():
    title = 'Shows'
    return render_template('shows.html', title=title)


@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html', title=title)


@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.html', title=title)


@app.route('/login')
def login():
    title = 'Log In'
    return render_template('login.html', title=title)
