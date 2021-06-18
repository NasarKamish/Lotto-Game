import json


class Player:
    def __init__(self, name, surname, id, email, currency):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email
        self.currency = currency
        self.dict = {"Name": name, "Surname": surname, "ID": id, "Email": email, "Currency": currency}

    def text_fill(self):
        with open("player.txt", "a+") as player_file:
            player_file.write(json.dumps(self.dict))
