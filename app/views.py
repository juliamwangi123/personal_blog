from crypt import methods
from csv import writer
from datetime import datetime
from email import message
from http import server
import re
from app import app
from flask import redirect, render_template, url_for,flash,request
from app.models import Blog,User,Comment
from app.forms import BlogForm,LoginForm,RegistrationForm,CommentForm
from app import db
from flask_login import current_user, login_user
from flask_login import logout_user
import smtplib 
import urllib.request, json
from flask_login import login_required

# home page route
@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():
    url='http://quotes.stormconsultancy.co.uk/random.json'
    response=urllib.request.urlopen(url)
    data=response.read()
    dict=json.loads(data)
   

    if request.method=='POST':
        email=request.form.get('email')
        message="You have subscribed successfully to InnerPieces"
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('innerpiece33@gmail.com', 'Mwangi@123')
        server.sendmail('innerpiece33@gmail.com', email,message)
        flash(f'subcribed successfuly', 'success')
        return redirect(url_for('home'))


    blogs=Blog.query.all()
    return render_template('index.html', blogs=blogs ,quotes=dict)


#route to about section
@app.route('/about')
def about():
    return render_template('about.html')


#add a ne blog

@app.route('/new')
@login_required
def new():
    form=BlogForm()

    return render_template('newblog.html' ,form=form)


#add new blog route
@app.route('/newblog', methods=['POST', 'GET'])
@login_required
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
    return redirect(url_for('home'))


#regestration of new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account succesfully created', 'success')
        return redirect(url_for('login'))
    return render_template('reg.html', title='Register', form=form)

#read full articale route
@app.route('/post/<int:post_id>', methods=['POST','GET'])
def post(post_id):
    blogs = Blog.query.filter_by(id=post_id).one()
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(body=form.body.data, blog_id=post_id, author=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added to the post", "success")
        return redirect(url_for("post", post_id=blogs.id))

    comments=Comment.query.filter_by(blog_id=blogs.id)
    return render_template('indvidual_blogs.html', blogs=blogs, comments=comments,form=form)



# @app.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
# def comment_post(post_id):
#     post = Blog.query.get_or_404(post_id)
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = Comment(body=form.body.data, blog_id=post_id, author=current_user.id)
#         db.session.add(comment)
#         db.session.commit()
#         flash("Your comment has been added to the post", "success")
#         return redirect(url_for("post", post_id=post.id))
#     return render_template("comment.html", title="Comment Post", form=form, post=post)



#edit post
@app.route('/blog/<int:blog_id>',methods=['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.author == current_user:
        flash(f'You have no permission to edit' , 'danger')
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.sub_title=form.sub_title.data
        blog.content = form.content.data
        db.session.commit()
        flash('Your pitch has been updated','success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.sub_title.data=blog.sub_title
        form.content.data = blog.content
    return render_template('newblog.html',form=form, blog=blog)


#delete blog
@app.route('/delete<int:blog_id>',methods=['POST', 'GET'])
@login_required
def delete(blog_id):
    blog=Blog.query.get_or_404(blog_id)
    if current_user != blog.author:
        db.session.delete(blog)
        db.session.commit()

    return redirect(url_for('blogs'))


