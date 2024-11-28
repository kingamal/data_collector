from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from dotenv import load_dotenv
import os
from send_email import send_email
from werkzeug.utils import secure_filename

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLALCHEMY_DATABASE_URI')
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_


@app.route("/")
def index():
    return render_template("index.html", btn=None)

@app.route("/success", methods=["POST"])
def success():
    global file
    if request.method=="POST":
        # email=request.form["email_name"]
        # height=request.form["height_name"]
        file=request.files["file"]
        filename="uploaded"+file.filename
        file.save(secure_filename(filename))
        with open(filename, "a") as f:
            f.write("\nThis was added later!")
        # if db.session.query(Data).filter(Data.email_==email).count() == 0:
        #     data=Data(email, height)
        #     db.session.add(data)
        #     db.session.commit()
        #     average_height=db.session.query(func.avg(Data.height_)).scalar()
        #     average_height=round(average_height,1)
        #     count=db.session.query(Data.height_).count()
        #     send_email(email, height, average_height, count)
        #     return render_template("success.html")
    return render_template("index.html", btn="download.html")
    # return render_template("index.html", 
    #     text="Seems like we've got something from that email address already")

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, download_name="yourfile.csv", as_attachment=True)

if __name__ == "__main__":
    app.debug=True
    app.run()