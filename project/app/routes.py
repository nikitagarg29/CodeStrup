from flask import render_template, Response, redirect, flash, request, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import sqlite3

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title = 'Code Guide')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/aboutus')
def aboutus():
    return render_template('about.html', title = 'Code Guide')

@app.route('/array')
def array():
    return render_template('array.html', title = 'Code Guide')
@app.route('/stack')
def stack():
    return render_template('stack.html', title = 'Code Guide')
@app.route('/queue')
def queue():
    return render_template('queue.html', title = 'Code Guide')
@app.route('/linkedlist')
def linkedlist():
    return render_template('linkedlist.html', title = 'Code Guide')

questions = [
    {
        "id": "1",
        "question": "What is the Capital of Syria?",
        "answers": ["a) Beirut", "b) Damascus", "c) Baghdad"],
        "correct": "b) Damascus"
    },
    {
        "id": "2",
        "question": "What is the square root of Pi?",
        "answers": ["a) 1.7724", "b) 1.6487", "c) 1.7872"],
        "correct": "a) 1.7724"
    },
    {
        "id": "3",
        "question": "How many counties are there in England?",
        "answers": ["a) 52", "b) 48", "c) 45"],
        "correct": "b) 48"
    }
]

@app.route('/quiz1',  methods=['GET', 'POST'])
def quizll():
    if request.method == 'GET':
        return render_template("quizll.html", data=questions)
    else:
        result = 0
        total = 0
        for question in questions:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        return render_template('result1.html', total=total, result=result)
    #return render_template('quizll.html', title = 'Linked List Quiz')

@app.route("/quiz", methods=['POST', 'GET'])
def quiz():
    if request.method == 'GET':
        return render_template("index.html", data=questions)
    else:
        result = 0
        total = 0
        for question in questions:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        return render_template('results.html', total=total, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
