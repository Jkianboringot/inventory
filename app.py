import re
from tkinter.messagebox import RETRY
from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Integer, default=0)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"

@app.route("/",methods=["POST","GET"])
def home() :
    if request.method == "POST":
        taskcontent=request.form["content"]
        inve= Inventory(content=taskcontent)

        try:
            db.session.add(inve)
            db.session.commit()
            return redirect("/")
        except:
            return "you fuck up"
    else:
        tasks=Inventory.query.order_by(Inventory.date_create).all()
        return render_template("index.html",tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_delete=Inventory.query.get_or_404(id)

    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "cant delete fix later"
    
@app.route('/update/<int:id>',methods=["GET","POST"])
def update(id):
        task=Inventory.query.get_or_404(id)
        if request.method == "POST":
             task.content=request.form["content"]
             try:
                db.session.commit()
                return redirect("/")
             except:
                return "can update"
        else:

            return render_template("update.html",task=task)


if __name__ == "__main__":
    app.run(debug=True)
