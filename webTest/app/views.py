from app import app, db, login_manager
from app.models import User
from app.forms import SignUpForm, LoginForm
from flask import render_template, redirect, url_for, flash, jsonify, session
from flask_login import login_user, current_user, login_required, logout_user
import random
from passlib.apps import custom_app_context as pwd_context
from flask_admin.contrib.sqla import ModelView


login_manager.login_view = "signin"


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/signin/', methods=("GET", "POST"))
def signin():
    if current_user.is_active:
        flash("You are already signed in.")
        return redirect(url_for("index"))
    signup = SignUpForm()
    login = LoginForm()
    if login.validate_on_submit():
        username = login.username_l.data.lower()
        password = login.password_l.data
        u = User.query.filter_by(username=username).first()
        if u:
            if not u.is_active:
                flash("This account has been deactivated because of too many complaints from users.")
            elif pwd_context.verify(password, u.password):
                login_user(u)
                flash("You're in.")
                return redirect(url_for("public_profile", name=u.username))
            else:
                flash("Wrong password.")
        else:
            flash('Never heard of you.')
    if signup.validate_on_submit():
        username = signup.username_s.data.lower()
        password = pwd_context.encrypt(signup.password_s.data)
        blurb = signup.about_s.data
        url = signup.url_s.data
        badu = User.query.filter_by(username=username).first()
        if not badu:
            u = User(username, password, url, blurb)
            db.session.add(u)
            db.session.commit()
            login_user(u)
            flash("Welcome.")
            return redirect(url_for("index"))
        else:
            flash("Sorry, that one's taken.")
    return render_template("signin.html", signup=signup, login=login)