from flask import render_template,request,redirect,url_for,abort,flash

# from app.email import mail_message
from . import main
# from flask_login import login_required,current_user
# from ..models import Subscriber, User,Pitch,Comment
# from .forms import UpdateProfile,BlogForm,CommentForm,UpdateBlog,SubscribeForm
# from .. import db,photos



@main.route('/')
def index():
    return render_template('index.html')
    