from flask import Flask , render_template,redirect ,url_for,request
import sqlite3
import socket as sck

app = Flask(__name__)

def sever():
    host = "0.0.0.0"
    port = 7000  
    
    c = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)   


def validate(username,password):
    completion = False
    connect = sqlite3.connect('login/logindb.db') 
    cur = connect.cursor()
    cur.execute("SELECT * FROM username")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        if dbUser == username:
            completion = check_password(dbPass, password)
            print("giusto")
    return completion
    

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method =='POST':
        username = request.form['username']
        password =  request.form['password']
        completion = validate(username,password)
        if completion == False:
            error  = 'inavalid credentials,try again'
        else:
            return redirect(url_for('secret'))
        return render_template('submit.html',error=error)

@app.route('/secret')
def secret():
    return "secret page "

if __name__=="__main__":
    app.run()
