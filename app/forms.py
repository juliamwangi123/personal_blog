from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class  Blog(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    sub_title=StringField('Sub title', validators=[StringField()])
    image=FileField('Blog Image', validators=[DataRequired()])
    content=StringField('Content', validators=[DataRequired()])
    