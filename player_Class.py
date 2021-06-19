import json


class Player:
    def __init__(self, name, surname, age, id, email, currency, prize, player_ID):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id
        self.email = email
        self.currency = currency
        self.prize = prize
        self.player_ID = player_ID
        self.dict = {"Name": name, "Surname": surname, "Age": age, "ID": id, "Email": email, "Currency": currency, "Prize": prize, "Player ID": player_ID}

    def text_fill(self):
        with open("player.txt", "w") as player_file:
            player_file.write(json.dumps(self.dict))

    def text_get(self):
        with open("player.txt", "r") as player_file:
            player_details = json.loads(player_file.read())
            return player_details


# player = Player("Nasar", "Kamish", "012839", "nasarkamish@gmail.com", "ZAR", 0)
