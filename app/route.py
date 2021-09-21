import secrets
import os
from flask import render_template, url_for, flash, redirect, request
from app.form import Registration_Form, Login_form, Saless
from app.mydb import User_1, Sales
from app import app, db, bcrypt
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def hello():
    return render_template('landing_page.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login_form()
    if form.validate_on_submit():
        user = User_1.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('betterlogin.html', form=form)


@app.route("/signin", methods=['Get', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration_Form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User_1(email=form.email.data, first_name=form.first_name.data, second_name=form.Second_name.data,
                      phone_number=form.phone_number.data, password=hashed_password, confirm_password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.email.data}!', category="")
        return redirect(url_for('login'))
    return render_template('signin.html', form=form)
@app.route("/home")
@login_required
def home():
    hists = os.listdir('app/static/profile_pics')
    hist = ['profile_pics/' + file for file in hists]
    return render_template('real_home.html', hists=hist)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)
    form_picture.save(picture_path)

    return picture_fn
@app.route("/sell", methods=['GET', 'POST'])
@login_required
def sell():
    form = Saless()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        sale = Sales(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date=datetime.utcnow(),
                     picture=picture_file, price=form.price.data, seller_id=current_user.id)
        db.session.add(sale)
        db.session.commit()
        flash(f'Good posted successfully', category="")
        return redirect(url_for('home'))
    return render_template("seelll.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
    return render_template('home.html')
