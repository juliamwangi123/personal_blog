from tkinter import S
from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Email
from flask_wtf.file import FileField

class  BlogForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    sub_title=StringField('Sub title', validators=[DataRequired()])
    image=FileField('Blog Image', validators=[DataRequired()])
    content=TextAreaField('Content', validators=[DataRequired()])
    add=SubmitField('ADD')


class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    login=SubmitField('Login')