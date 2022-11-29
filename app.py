from flask import Flask, render_template , request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy()
db.init_app(app)

# Tworzenie tabeli
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

# Wyswietlanie strony internetowej
@app.route("/")
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("todo.html", todo_list=todo_list)

# Dodawanie zadania
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

# Usuwanie zadania (id przekazujemy aby wiedziec co usunac)
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

with app.app_context():
        db.create_all()
        db.session.commit()

if __name__ == "__main__":
        app.run(debug=True)