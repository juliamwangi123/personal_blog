from app import app
from flask import redirect, render_template,flash,url_for
from .forms import BlogForm,LoginForm
from .models import Blog, User

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
    form=BlogForm()
    return render_template('newblog.html' ,form=form)


##route to the login form only for authenticated user
@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.email.data=='juliahwambui3@gmail.com' and form.password.data=='1234':
        flash('Juliah you are logged in', 'success')
        return redirect(url_for('home'))

    return render_template('login.html', form=form)