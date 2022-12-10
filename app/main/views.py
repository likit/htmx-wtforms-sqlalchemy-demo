from flask import render_template, flash
from app.main import main_blueprint as main
from app.main.forms import LoginForm
from app import db
from app.main.models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.get(form.email.data):
            flash('The email already exists.', 'danger')
        else:
            user = User()
            user.email = form.email.data
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            flash('Login or sign up successfully.', 'success')
    else:
        for field, err in form.errors.items():
            flash(f'{field}:{err}', 'danger')

    return render_template('main/index.html', form=form)

