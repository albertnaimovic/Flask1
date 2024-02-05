from main import app, db, Message

with app.app_context():
    message_antanas = Message.query.filter_by(email="Antanas")
    print(message_antanas.all())
    jonas = Message.query.get(1)
    db.session.delete(jonas)
    db.session.commit()
    print(Message.query.all())

# [Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]