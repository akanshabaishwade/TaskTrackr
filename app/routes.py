from flask import render_template, request, flash, redirect, url_for
from app import db
from app.models import User, Task
from werkzeug.security import generate_password_hash
from datetime import datetime
from app import app, db




@app.route('/')
@app.route('/home')
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)


from flask import render_template, flash

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        email = form.get('email')
        password = form.get('password')

        print("Username:", username)
        print("Email:", email)
        print("Password:", password)

        if username and email and password:  # Ensure all fields are provided
            # Add the user to the database
            entry = User(username=username, email=email, password=password)
            db.session.add(entry)
            db.session.commit()

            # Flash a success message
            flash('User added successfully!', 'success')

            # Retrieve all users including the newly added one
            users = User.query.all()

            # Pass the users data to the template for display
            return render_template('add_user.html', users=users)
        else:
            # Flash an error message
            flash('All fields are required.', 'error')
            print("All fields are required.")  # Print to console for debugging

    # Render the HTML template for the form
    return render_template('add_user.html')


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title or not content:
            flash('Title and Content are required.', 'error')
        else:
            deadline = request.form.get('deadline')
            priority = request.form.get('priority')
            user_id = request.form.get('user_id')

            new_task = Task(title=title, content=content, deadline=deadline, priority=priority, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added successfully.', 'success')
            return redirect(url_for('home'))
    
    return render_template('add_task.html')


@app.route('/tasks')
def get_all_tasks():
    all_tasks = Task.query.all()
    return render_template('tasks.html', tasks=all_tasks)


@app.route('/users')
def get_all_user():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)
