from app import app
from flask import render_template
from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from app.editor import MyForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'My Page')
@app.route('/project')
def project():
    return render_template('projects.html')
@app.route('/experience')
def experience():
    return render_template('experience.html')
@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/editor', methods = ['GET', 'POST'])
def editor():
    form = MyForm()
    if form.validate_on_submit():
        text = form.source_code.data
    return render_template('editor.html', form=form)