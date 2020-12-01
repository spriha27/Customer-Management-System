from website import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from website.forms import customer_registration_form, customer_login_form, manager_login_form
from website.database import Existing_user, Deleted_user, Manager
from flask_login import login_user, current_user, logout_user, login_required
import random

def Userid():
    id = random.randint(17500, 18500)
    userid = Existing_user.query.filter_by(userid=id).first()
    if userid:
        Userid()
    return id

message = "Login"

@app.route('/')
@app.route('/all_login')
def all_login():
    return render_template("all_login.html",title="Intro",message=message)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route('/customer_options')
def customer_options():
    return render_template('customer_options.html', title="Customer Options")

@app.route('/customer_registration',methods=['GET', 'POST'])
def customer_registration():
    if current_user.is_authenticated:
        return redirect(url_for('customer_view_profile'))
    form = customer_registration_form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        userid = Userid()
        customer = Existing_user(userid=userid,username=form.username.data,email=form.email.data,address=form.address.data,
            contact_no=form.contact_no.data,password=hashed_password)
        db.session.add(customer)
        db.session.commit()
        flash(f'Account created Successfully! Please note that your Customer id is {userid}','success')
        return redirect(url_for('customer_view_profile'))
    return render_template('customer_registration.html', title='Register', form=form)

@app.route('/customer_login', methods=['GET', 'POST'])
def customer_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = customer_login_form()
    if form.validate_on_submit():
        user = Existing_user.query.filter_by(userid=form.userid.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'You have been logged in!','success')
            return redirect(url_for('customer_view_profile'))
        else:
            flash(f'Check you User id or password!','danger')
    return render_template("customer_login.html", title="User Login", form = form)

@app.route('/customer_view_profile')
def customer_view_profile():
    return render_template('customer_view_profile.html')

# @app.route('/customer_set_password')
# def customer_set_password():
#     return render_template('customer_set_password.html')

@app.route('/manager_view_details')
def manager_view_details():
    return render_template('manager_view_details.html')

@app.route('/manager_login', methods=['GET', 'POST'])
def manager_login():
    form = manager_login_form()
    if form.validate_on_submit():
        manager = Manager.query.filter_by(email=form.email.data).first()
        password = Manager.query.filter_by(password=form.password.data).first()
        if manager and password:
            login_user(manager, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('manager_view_details'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('manager_login.html', title='Manager Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('all_login'))
