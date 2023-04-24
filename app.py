from flask import Flask, render_template,request
from flask import jsonify
import sqlite3 as lite 
import pickle

model=pickle.load(open('pickle_model.pkl','rb'))
# Set up Flask
app = Flask(__name__)

# Set up app routes
@app.route("/")
def index():
    #return render_template("index.html")
    return "Hello flask"

@app.route('/Take_a_Test',methods=['POST','GET'])
def Take_a_Test():
    return render_template('test.html')

# @app.route('/api/v1.0/data', methods=['GET'])
# def get_data():
#     con = lite.connect('mental_health.db')
#     with con:
#         cur = con.cursor()
#         cur.execute("SELECT * FROM pre_encoded_questions")
#         rows = cur.fetchall()
#         result = []
#         for row in rows:
#             result.append(row)
#     return jsonify({'data': result})

# Tell Flask to run
if __name__ == "__main__":
    app.run()