from app import app
from flask import render_template
from .forms import Blog

# home page route
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


#route to about section
@app.route('/about')
def about():
    return render_template('about.html')


#route to new blog
@app.route('/new_blog' , methods=['GET', 'POST'])
def new_blog():
    form=Blog()
    return render_template('newblog.html' ,form=form)
