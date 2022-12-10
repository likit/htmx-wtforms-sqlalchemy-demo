from flask import render_template, flash, redirect, url_for, make_response
from app.main import main_blueprint as main
from app.main.forms import LoginForm
from app import db
import time
from app.main.models import User


@main.route('/', methods=['GET'])
def index():
    form = LoginForm()
    return render_template('main/index.html', form=form)


@main.route('/api/login', methods=['POST'])
def process_login_form():
    form = LoginForm()
    time.sleep(3)
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if user.password == form.password.data:
                flash('Login Successfully.', 'success')
            else:
                flash('The email already exists.', 'danger')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            flash('Sign Up Successfully.', 'success')
    else:
        for field, err in form.errors.items():
            flash(f'{field}:{err}', 'danger')

    resp = make_response()
    resp.headers['HX-Redirect'] = url_for('main.index')
    return resp


