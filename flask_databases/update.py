from main import app, db, Message

with app.app_context():
    antanas = Message.query.get(2)
    antanas.email = "geras.zmogus@lrs.lt"
    db.session.add(antanas)
    db.session.commit()
    print(Message.query.all())

# [Jonas - jonas@mail.com, Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]
