import json


class Player:
    def __init__(self, name, surname, id, email, currency):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email
        self.currency = currency
        self.dict = {"Name": name, "Surname": surname, "ID": id, "Email": email, "Currency": currency}
        self.text_fill()

    def text_fill(self):
        with open("player.txt", "w") as player_file:
            player_file.write(json.dumps(self.dict))

    def text_get(self):
        with open("player.txt", "r") as player_file:
            player_details = json.loads(player_file.read())
            print(player_details)


player = Player("Nasar1", "Kamish", "012839", "nasarkamish@gmail.com", "ZAR")
