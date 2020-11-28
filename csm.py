from flask import Flask, render_template
app = Flask(__name__)

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

@app.route('/')
@app.route('/allLogin')
def all_login():
    return render_template('all_login.html')

@app.route('/customer_options')
def customer_options():
    return render_template('customer_options.html')

@app.route('/customer_login')
def customer_login():
    return render_template('customer_login.html')

@app.route('/customer_view_profile')
def customer_view_profile():
    return render_template('customer_view_profile.html')

@app.route('/customer_registration')
def customer_registration():
    return render_template('customer_registration.html')

@app.route('/customer_set_password')
def customer_set_password():
    return render_template('customer_set_password.html')

@app.route('/manager_login')
def manager_login():
    return render_template('manager_login.html')

@app.route('/manager_view_details')
def manager_view_details():
    return render_template('manager_view_details.html', customers = customerDB)