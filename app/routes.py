from app.send_email import send_email
from app.model import Data
from app import db, app, email_id, password

from flask import render_template, request
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser
import csv





#creating a csv file with the given values in database
def to_csv():

    q = db.session.query(Data)


    with open("DATA.csv", 'w') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        header = Data.__table__.columns.keys()

        outcsv.writerow(header)     

        for record in q.all():
            outcsv.writerow([getattr(record, c) for c in header ])









#home page
@app.route("/")
def home():
    global posts

    if len(Data.query.all()) > 3:
        posts=Data.query.all()[-3:]
        text= "Last three entries:"
    else:
        posts=Data.query.all()
        text=""
    return render_template('search.html',text1= text, posts=posts)



#adding data page
@app.route("/insert")
def insert():

    return render_template("insert.html")



#search page
@app.route("/search", methods=['POST'])
def search():
    if request.method=='POST':

        name=request.form["name1"]
        name=str(name)
        posts1 = Data.query.filter_by(name_=name)
        count = Data.query.filter_by(name_=name).count()
        if count != 0:
            return render_template('user.html', posts1=posts1)

    return render_template('search.html',posts=posts,text="Invalid Name")



#sucess page
@app.route("/success", methods=['POST'])
def success():

    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        name=request.form["name1"]
        

        #checking if the given email already exists
        if db.session.query(Data).filter(Data.email_==email).count()==0:

            #mapping the variable to the database model  
            data=Data(email,height,name)

            #inserting the data in database
            db.session.add(data)
            db.session.commit()

            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height, 1)
            count = db.session.query(Data.height_).count()


            to_csv()


            #calling the send_email func
            #send_email(email_id,password,email, height, name, average_height, count)
            
            return render_template("success.html")

    return render_template('insert.html', text="Seems like we got something from that email once!")

