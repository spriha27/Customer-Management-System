from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from website.database import Existing_user, Deleted_user, Manager

class customer_registration_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    address = TextAreaField('Address', validators=[DataRequired()])
    contact_no = StringField('Contact Details', validators=[DataRequired(),Length(min=10,max=10)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        customer = Existing_user.query.filter_by(username=username.data).first()
        if customer:
            raise ValidationError('User name already exits, try again!')
    def validate_email(self, email):
        customer = Existing_user.query.filter_by(email=email.data).first()
        if customer:
            raise ValidationError('email already exits, try again!')

class customer_login_form(FlaskForm):
    userid = StringField('User id',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Customer login')

class manager_login_form(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Manager login')
