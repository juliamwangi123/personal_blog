from datetime import datetime
import re
from app import app
from flask import redirect, render_template, url_for,flash
from app.models import Blog,User
from app.forms import BlogForm,LoginForm,RegistrationForm
from app import db
from flask_login import current_user, login_user
from flask_login import logout_user
# home page route
@app.route('/')
@app.route('/home')
def home():
    blogs=Blog.query.all()
    return render_template('index.html', blogs=blogs)


#route to about section
@app.route('/about')
def about():
    return render_template('about.html')


#route leads to add new blog route
@app.route('/new')
def new():
    form=BlogForm()

    return render_template('newblog.html' ,form=form)


#add new blog route
@app.route('/newblog', methods=['POST', 'GET'])
def newPost():
    form=BlogForm()
    if form.validate_on_submit:
        blog=Blog(title=form.title.data , sub_title=form.sub_title.data, content=form.content.data )
        db.session.add(blog)
        db.session.commit()
        flash('blog added succesfully')
        return redirect(url_for('home'))


#all blogs 
@app.route('/blogs')
def blogs():
      blogs = Blog.query.order_by(Blog.time_posted.desc()).all()

      return render_template('blog.html', blogs=blogs)



#login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)



#logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


#regestration of new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account succesfully created', 'success')
        return redirect(url_for('login'))
    return render_template('reg.html', title='Register', form=form)