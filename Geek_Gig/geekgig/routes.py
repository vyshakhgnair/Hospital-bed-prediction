import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from geekgig import app, db, bcrypt
from geekgig.forms import LoginForm, DataForm
from geekgig.models import Admin, Supplier, DataA, DataS
from flask_login import login_user, logout_user, current_user, login_required
from geekgig.mean import mean_bed, mean_icu, mean_oxygen

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/admin/login", methods=['GET','POST'])
def adminLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('adminDash'))
        else:
            flash('Login unsuccessful. Please check your username and password', 'danger')
    return render_template('adminLogin.html', title='Admin Login', form=form)

@app.route("/supplier/login", methods=['GET','POST'])
def supplierLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Supplier.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('supplierDash'))
        else:
            flash('Login unsuccessful. Please check your username and password', 'danger')
    return render_template('supplierLogin.html', title='Supplier Login', form=form)

@app.route("/admin/dashboard", methods=['GET','POST'])
def adminDash():
    form = DataForm()
    if form.validate_on_submit():
        data = DataA(beds=mean_bed, oxygen=mean_oxygen, icu=mean_icu, month_posted=form.month_posted.data, admin=current_user)
        db.session.add(data)
        db.session.commit()
        flash('Your data has been entered!', 'success')
        return redirect(url_for('supplierDash'))
    return render_template('adminDash.html', form=form, title='Admin Dashboard')

@app.route("/supplier/dashboard")
def supplierDash():
    data = DataA.query.order_by(DataA.id.desc()).first()
    return render_template('supplierDash.html', data=data, title='Supplier Dashboard')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))