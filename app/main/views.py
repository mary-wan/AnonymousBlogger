from flask import render_template,request,redirect,url_for,abort,flash

from app.email import mail_message
from . import main
from flask_login import login_required,current_user
from ..models import Upvote, User,Blog,Comment,Downvote
from .forms import UpdateProfile,BlogForm,CommentForm,UpdateBlog
from .. import db,photos



@main.route('/')
def index():
    blogs = Blog.query.all()
    general = Blog.query.filter_by(category = 'General').all()
    politics = Blog.query.filter_by(category = 'Politics').all()
    religion = Blog.query.filter_by(category = 'Religion').all()
    relationships = Blog.query.filter_by(category = 'Relationships').all()
    
    return render_template('index.html',blogs=blogs,general=general,politics=politics,religion=religion,relationships=relationships)

@main.route('/create_new',methods=['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data   
        new_blog =Blog(title = title,post=post,user=current_user)
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    
    return render_template('new_blog.html',form=form, title="Create Blog")

@main.route('/comment/<int:blog_id>',methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    if form.validate_on_submit():
        comment= form.comment.data
        new_comment= Comment(comment=comment,blog_id=blog_id)
        new_comment.save_comment()
        blog_id=blog_id
        return redirect(url_for('.comment',blog_id=blog_id))
    return render_template('comment.html',form=form,comments=comments)
        
    
