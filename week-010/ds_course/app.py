from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ds_course_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<User {self.id} {self.username}>" 
    
@app.route('/')
def home():
    usrs = User.query.all()
    return render_template("home.html", users=usrs)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        un = request.form["username"]
        pw = request.form["password"]
        user = User(username=un, password=pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("register.html")

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)

#db.session.add(new_student)
#db.session.commit()