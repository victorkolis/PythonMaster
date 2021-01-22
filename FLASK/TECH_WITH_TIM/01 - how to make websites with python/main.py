from flask import Flask, redirect, url_for


app = Flask(__name__)


# Defining pages
@app.route('/')
def home():
    return '<h1>AEVUM<h1>'


@app.route('/<name>')  # Getting the data via tag (URL)
def user(name):
    return 'Hello {}!'.format(name)


# Redirecting in case of unauthorized/unauthenticated
@app.route('/admin')
def admin():
    return redirect(url_for('home'))  # The name of the function goes in strings


if __name__ == '__main__':
    app.run(debug=True)
