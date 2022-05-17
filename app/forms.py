from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from app.models import User


class BlogForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    sub_title=StringField('Sub_Title', validators=[DataRequired()])
    content=TextAreaField('Content', validators=[DataRequired()])
    add=SubmitField('Add')




class LoginForm(FlaskForm):
    email =StringField("Email", validators=[DataRequired(), Email()])
    password= PasswordField("Password", validators=[DataRequired()])
    remember=BooleanField("Remember me?")
    submit=SubmitField("Login in")


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password= PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


#both username and email have to be unique 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')




#comment table
class CommentForm(FlaskForm):
    body = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")