from flask import Flask, render_template, url_for, flash, redirect
from forms import customer_registration_form, customer_login_form, manager_login_form
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '6364b380cc27fc761cedcbc05b9ad119'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Existing_user(db.Model):
    regID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    contactno = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Existing_user('{self.username}', '{self.email}')"

class Deleted_user(db.Model):
    regID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    contactno = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')##########
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Deleted_user('{self.username}', '{self.email}')"

######################################
class Manager(db.Model):
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Manager('{self.email}')"


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"


customerDB = [{
	'regID': '1779321',
	'name': 'Spriha',
	'email': 'spriha27@gmail.com',
	'address': 'god knows',
	'contactno': '9876543210'
	},
	{
	'regID': '1234567',
	'name': 'Dracula',
	'email': 'blood@gmail.com',
	'address': 'Dark Caves',
	'contactno': '1122334455'
	},
]
#################################
message = 'Login'

@app.route('/')
@app.route('/all_login')
def all_login():
    return render_template('all_login.html',title="Intro",message=message)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route('/customer_options')
def customer_options():
    return render_template('customer_options.html', title="Customer Options")

@app.route('/customer_view_profile')
def customer_view_profile():
    return render_template('customer_view_profile.html')

@app.route('/customer_login', methods=['GET', 'POST'])
def customer_login():
	form = customer_login_form()
	if form.validate_on_submit():
		if form.email.data == 'customer@tcs.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('customer_view_profile'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('customer_login.html', title='Customer_Login', form=form)

@app.route('/customer_set_password')
def customer_set_password():
    return render_template('customer_set_password.html')

@app.route('/customer_registration')
def customer_registration():
	form = customer_registration_form()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('customer_set_password'))
	return render_template('customer_registration.html', title='Register', form=form)

@app.route('/manager_view_details')
def manager_view_details():
    return render_template('manager_view_details.html', customers = customerDB)

@app.route('/manager_login', methods=['GET', 'POST'])
def manager_login():
	form = manager_login_form()
	if form.validate_on_submit():
		if form.email.data == 'manager@tcs.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('manager_view_details'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('manager_login.html', title='Manager_Login', form=form)

if __name__=='__main__':
    app.run(debug=True)

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)