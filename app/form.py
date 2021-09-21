from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField,IntegerField
from app.mydb import User_1
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Registration_Form(FlaskForm):
    first_name = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=40)])
    Second_name = StringField('Second name', validators=[DataRequired(), Length(min=2, max=40)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=9, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    Confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        user = User_1.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email already exist')


class Login_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Pasword', validators=[DataRequired()])
    submit = SubmitField()


class Saless(FlaskForm):
    name = StringField('Goods_Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    picture = FileField('Picture', validators=[FileAllowed(['png', 'jpg'])])
    price = IntegerField('price', validators=[DataRequired()])
    submit = SubmitField('POST')
