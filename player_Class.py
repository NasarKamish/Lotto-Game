import json


class Player:
    def __init__(self, name, surname, id, email, currency, prize):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email
        self.currency = currency
        self.prize = prize
        self.dict = {"Name": name, "Surname": surname, "ID": id, "Email": email, "Currency": currency, "Prize": prize}
        self.text_fill()

    def text_fill(self):
        with open("player.txt", "w") as player_file:
            player_file.write(json.dumps(self.dict))

    def text_get(self):
        with open("player.txt", "r") as player_file:
            player_details = json.loads(player_file.read())
            print(dict(player_details))
            return player_details


player = Player("Nasar", "Kamish", "012839", "nasarkamish@gmail.com", "ZAR", 0)
