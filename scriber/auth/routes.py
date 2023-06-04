from scriber.auth import bp
from flask import render_template, flash, url_for, redirect
from scriber.forms.user import RegisterForm, LoginForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login Successful!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Registration Successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)