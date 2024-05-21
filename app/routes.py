from flask import Blueprint, render_template, url_for, flash, redirect
from app import db
from app.models import User, Task

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', title='Tasks', tasks=tasks)
