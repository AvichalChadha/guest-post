from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import validators, ValidationError


app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI='mysql://username:password@server/databasename'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://sql12220122:xRGkrN23qW@sql12.freemysqlhosting.net/sql12220122'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#3 creating the mysql table! 
class posts_enter(db.Model):
    __tablename__ = 'posts_enter'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    author = db.Column(db.String(20))
    description = db.Column(db.String(120))
    post= db.Column(db.String(120))
    AuthorDescription= db.Column(db.String(120))


@app.route('/send', methods = ['GET','POST'])
# gotta check if the send used in the html file is the same define or the url ????
def send():
    if request.method == "POST":
        title= request.form['title']
        author= request.form['AuthorName']
        description= request.form['Description']
        post= request.form['post']
        AuthorDescription= request.form['AuthorDescription']

        lol = posts_enter(title=title,author=author,description=description,post=post,AuthorDescription=AuthorDescription)
        db.session.add(lol)
        db.session.commit()
        return redirect(url_for('yoyo'))
    elif request.method == "GET":
        return render_template("posts.html")

'''
@app.route('/send', methods = ['GET','POST'])
# gotta check if the send used in the html file is the same define or the url ????
def send():
    if request.method == "POST":
        ## difference in the two code start from here! 
        a= request.form['title']
        s= request.form['AuthorName']
        d= request.form['Description']
        f= request.form['post']
        g= request.form['AuthorDescription']

        lol = posts_enter(title=a,author=s,description=d,post=f,AuthorDescription=g)
        db.session.add(lol)
        db.session.commit()
        return redirect(url_for('yoyo'))
    elif request.method == "GET":
        return render_template("posts.html")
'''



@app.route('/result',methods = ['POST', 'GET'])
def yoyo():
    return "hepls"
   

      



if __name__ == '__main__':
   app.run(debug = True)




