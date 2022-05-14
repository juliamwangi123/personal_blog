from turtle import title
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,BooleanField


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