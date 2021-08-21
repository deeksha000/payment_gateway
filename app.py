
from flask import Flask, render_template,request
import os
import sys
sys.path.insert(0,'D:\payment\Email')
import smtplib
from email.message import EmailMessage
from email_sender import send_email


app = Flask(__name__) 

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/details',methods=['POST','GET'])
def details():
    #email = request.form.get('emailId')
    #send_email(email)
    send_email()
    return render_template("details.html")
@app.route('/pay')
def pay():
    return render_template("pay.html")


if __name__ == "__main__":
    app.run(debug=True)
