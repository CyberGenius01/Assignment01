from flask import redirect, render_template, url_for
from project import app
from project.forms import LoginForm
from project.models import User
from flask_login import login_required, login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/profile')
def profile_page():
    return render_template('profile.html')


@app.route('/subscriptions')
@login_required
def subscriptions_page():
    return render_template('subscriptions.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
       attempted_user = User.query.filter_by(username='Cipherer').first()
       attempted_password=form.password.data
       print(form.username.data)
       print(attempted_user)
       if attempted_user and attempted_user.password == attempted_password:
           login_user(attempted_user)
           return redirect(url_for('subscriptions_page')) 
    return render_template('login.html', form=form)

         
@app.route('/logout')
def logout_page():  
    logout_user()
    return redirect(url_for('home_page'))
