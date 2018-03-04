
'''
thinhs to be done- 
1) the validation lenght is to be  set ptoparly. Not done yet for testing purposes! 
2) Even the sql table varchar has to be set! 
3) emial and URL validation is not also set 
4) And also we have to do the prevention from SQL injection, Learn that from sendtex. 
5) THere are couple of pics clicked on the phone that tells how to give your sql location whn you are hosting it on the server. 
or go to the flask blog at 24:02, or just copy from it's github code. 
in the post_submitted section, write this- written by _____ on _____
6) change the variable name from 'lol'

'''


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, validators, ValidationError
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm, Form

from datetime import datetime
import random, string


app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI='mysql://username:password@server/databasename'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://sql12220122:xRGkrN23qW@sql12.freemysqlhosting.net/sql12220122'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "some_password"

#3 creating the mysql table!
class posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(60))
    title = db.Column(db.String(60))
    author = db.Column(db.String(20))
    description = db.Column(db.String(70))
    post= db.Column(db.String(3000))
    AuthorDescription= db.Column(db.String(100))
    email = db.Column(db.String(60))
    date_posted = db.Column(db.String(20))
    random = db.Column(db.String(5))



class Post_Form(Form):
    #link = TextField('Link', [validators.Length(min=3, max=20), validators.URL()])
    title = StringField('Title', [validators.Length(min=1, max=60)])
    url= StringField("Website's Link", [validators.Length(min=1, max=60)])
    author = StringField("Author's Name", [validators.Length(min=1, max=20)]) # name of the author
    description = StringField('Description', [validators.Length(min=1, max=60)])
    post = StringField('Post', [validators.Length(min=1, max=3000)])
    AuthorDescription = StringField("Author's Description", [validators.Length(min=1, max=100)])
    email = StringField("Email Address", [validators.Length(min=1, max=20)]) 
    

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))




@app.route('/', methods = ['GET','POST'])
def index():
    form = Post_Form(request.form)   # earlier this code was both under if statement and elif statement, see if it doesn't lead to some error! 
    if request.method == "GET":
        
        return render_template('post.html', form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            url_genrator = randomword(5)
            postedDate = datetime.utcnow().strftime("%d-%m-%y")
            lol = posts(title= form.title.data, url= form.url.data, author=form.author.data, description=form.description.data,post=form.post.data,AuthorDescription=form.AuthorDescription.data,email=form.email.data, date_posted = postedDate, random=url_genrator)
            db.session.add(lol)
            db.session.commit()
            return "Done LOL"
        else : 
            return "i don't know how to react"

##just to clarify few thing, in this code-  'lol = posts(title= form.title.data, url= form.url.data, author=form.author.data, description=form.description.data,post=form.post.data,AuthorDescription=form.AuthorDescription.data,email=form.email.data)'
## 'title' in the left is reffered to the 'title' in the class 'posts', i.e the one resposnible for SQLdb. 
## And the 'form.title.data' refers to the info that we passout in the form. 
## And 'title' in 'form.title.data' refers to variable in the class 'Post_Form'. 
## If that sounds confusing, better clear your concepts :) 



##This endpoint will show the list of all the guest posts
@app.route('/posts', methods= ['GET'])
def submitted_posts():
    dbData = posts.query.all()  
    return render_template('post_submitted.html', dbData= dbData  )


#this endpoint will the specific post and the post will have a randon endpoint
@app.route('/guest-post/<int:random_id>)
def guest_post(random_id):
    article = posts.query.filter_by(random = random_id).one()
    return render_template ('guest_post.html', post = article)
    








if __name__ == '__main__':
   app.run(port= 6002, debug = True)
