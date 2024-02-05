from main import db, Message, app


with app.app_context():
    all_messages = Message.query.all()
    print(all_messages)

    message_1 = Message.query.get(1)
    print(message_1)

    message_antanas = Message.query.filter_by(name="Antanas")
    print(message_antanas.all())

# [Antanas - antanas@mail.lt]
#  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]
