import os
from main import db, Message, app
from flask import request, render_template


@app.route("/")
def user():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        filter_by_email = bool(Message.query.filter_by(email=email).first())
        if filter_by_email:
            return render_template(
                "login.html", warning_message="User with this email already exists"
            )
        message = request.form["message"]
        query = Message(name, email, message)
        db.session.add(query)
        db.session.commit()
        return render_template("greetings.html", vardas=name)
    elif request.method == "GET":
        return render_template("login.html")


@app.route("/showall", methods=["GET"])
def show_all():
    with app.app_context():
        all_messages = Message.query.all()
        print(all_messages)
        return render_template("show_all.html", all_messages=all_messages)


@app.route("/delete", methods=["GET", "POST"])
def delete_by_email():
    if request.method == "POST":
        with app.app_context():
            email = request.form["email"]
            filter_by_email = Message.query.filter_by(email=email).first()
            db.session.delete(filter_by_email)
            db.session.commit()
            all_messages = Message.query.all()
        return render_template("delete.html", all_messages=all_messages)
    elif request.method == "GET":
        with app.app_context():
            all_messages = Message.query.all()
            return render_template("delete.html", all_messages=all_messages)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
