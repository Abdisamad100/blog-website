from flask_login import login_required
from flask import render_template,request,redirect,url_for
from . import main
from ..models import User
from .. import db
from datetime import datetime



@main.route('/')
def index():
    tittle="welcome to blog"
    return render_template("index.html")    


@main.route('/blogs')
@login_required
def blogs():
    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).limit(15)

    return render_template('blogs.html', all_blogs=all_blogs)

@main.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).first()

    return render_template('post.html', post=post)


@main.route('/post')
def add():
    return render_template('post.html')

@main.route('/addblog', methods=['GET','POST'])
@login_required
def addpost():

    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_blog = Blog(title=title,
                        content=content, user=current_user)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', form=form)




@main.route('/post/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()

    if form.validate_on_submit():
        content = form.content.data

        new_comment = Comment(
            blog_id=blog.id, comments=content, user=current_user)

        new_comment.save_comment()
        print(new_comment)
        return redirect(url_for('main.index', id=post.id))

    return render_template('new_comment.html', comment_form=form)

