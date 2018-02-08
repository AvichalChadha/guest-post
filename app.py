from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI= 'mysql://username:password@server/databasename'
SQLALCHEMY_DATABASE_URI= ''
db = SQLAlchemy(app)



class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)


## FOR CREATING THE TABLE! 

## >>> import app from db
## >>> db.create_all()
## >>> db.session.commit()








