
'''
thinhs to be done- 
2) Even the sql table varchar has to be set! 
5) THere are couple of pics clicked on the phone that tells how to give your sql location whn you are hosting it on the server. 
or go to the flask blog at 24:02, or just copy from it's github code. 
in the post_submitted section, write this- written by _____ on _____
7) recaptcha before posting the blog post
'''


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, validators, ValidationError, TextAreaField, TextField
from wtforms.validators import InputRequired, Email, Length, URL
from flask_wtf import Form
from flask_wtf import FlaskForm

from flask_bootstrap import Bootstrap
from datetime import datetime
import random, string


app = Flask(__name__)
Bootstrap(app)

#SQLALCHEMY_DATABASE_URI='mysql://username:password@server/databasename'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://database32:Ya29~Z1iY~36@den1.mysql1.gear.host/database32'
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
    title = TextField('Title',validators=[InputRequired(), Length(min=5, max=60, message="The field must be between 5 and 60 characters long")],render_kw={"placeholder": "Title of your Post"})
    url= TextField("Website's Link",render_kw={"placeholder": "Your Blog's Link If You Have Any"})
    author = TextField("Author's Name",validators=[InputRequired(), Length(min=3, max=40, message="The field must be between 5 and 40 characters long")],render_kw={"placeholder": "Author's Name"}) # name of the author
    description = TextField('Subtitle', validators=[InputRequired(), Length(min=5, max=400, message="The field must be between 5 and 380 characters long")] ,render_kw={"placeholder": "Subtitle Of Your Post"})
    post = TextAreaField('Post', validators=[InputRequired(), Length(min=5, max=5000, message="The field must be between 5 and 2000 characters long")], render_kw={"rows": 30, "cols": 50})
    AuthorDescription = TextAreaField("Author's Description",validators=[InputRequired(), Length(min=30, max=1000, message="The field must be between 5 and 60 characters long")], render_kw={"rows": 5, "cols": 50})
    email = TextField("Email Address",validators=[InputRequired(),Email(message='Enter a valid email'), Length(min=10, max=100)],render_kw={"placeholder": "Your Email Address"}) 
    

    

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
            Data = posts(title= form.title.data, url= form.url.data, author=form.author.data, description=form.description.data,post=form.post.data,AuthorDescription=form.AuthorDescription.data,email=form.email.data, date_posted = postedDate, random=url_genrator)
            db.session.add(Data)
            db.session.commit()

            return redirect(url_for('after_submissions'))
        else : 
            return render_template("post.html",form=form)

##just to clarify few thing, in this code-  'lol = posts(title= form.title.data, url= form.url.data, author=form.author.data, description=form.description.data,post=form.post.data,AuthorDescription=form.AuthorDescription.data,email=form.email.data)'
## 'title' in the left is reffered to the 'title' in the class 'posts', i.e the one resposnible for SQLdb. 
## And the 'form.title.data' refers to the info that we passout in the form. 
## And 'title' in 'form.title.data' refers to variable in the class 'Post_Form'. 



##This endpoint will show the list of all the guest posts
@app.route('/posts', methods= ['GET'])
def submitted_posts():
    dbData = posts.query.all()  
    return render_template('post_submitted.html', dbData= dbData  )



#this endpoint will the specific post and the post will have a randon endpoint
@app.route('/guest-post/<random_id>')
def guest_post(random_id):
    article = posts.query.filter_by(random=random_id ).one()
    return render_template ('guest_post.html', post = article)
    


@app.route('/submitted_posts/')
def after_submissions():
    return render_template ('submission.html')



if __name__ == '__main__':
   app.run(port= 6001, debug = True)
'''



class Post_Form(Form):
    #link = TextField('Link', [validators.Length(min=3, max=20), validators.URL()])
    title = StringField('Title', [validators.Length(min=5, max=60)])
    url= StringField("Website's Link", [validators.Length(min=5, max=60)])
    author = StringField("Author's Name", [validators.Length(min=1, max=20)]) # name of the author
    description = StringField('Sub', [validators.Length(min=1, max=150)])
    post = StringField('Post', [validators.Length(min=60, max=3000)])
    AuthorDescription = StringField("Author's Description", [validators.Length(min=20, max=300)])
    email = StringField("Email Address", [validators.Length(min=5, max=50)]) 



'''
