from flask import Flask, render_template,request
#from flask import jsonify
import sqlite3 as lite 
import pickle
from flask_sqlalchemy import SQLAlchemy

model=pickle.load(open('pickle_model.pkl','rb'))
# Set up Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class test(db.Model):
    gender=db.column(db.String(100))

    def __repr__(self):
        return '<task %r>' % self.gender


# Set up app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/Take_a_Test',methods=['POST','GET'])
def Take_a_Test():
    return render_template('test.html')


# Tell Flask to run
if __name__ == "__main__":
    app.run()