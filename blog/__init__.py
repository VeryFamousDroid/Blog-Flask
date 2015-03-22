from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

from models import *

app.debug = True
app.config.from_pyfile('config.py')
toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['password'] != request.form['password-confirm']:
            flash('Passwords do not match.')
            return_templaye('register.html')
        user = User(request.form['username'], request.form['email'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        session['user'] = user

        flash('You have been registered!')
        return render_template('index.html')

    return render_template('register.html')

if __name__ == '__main__':
    app.run()
