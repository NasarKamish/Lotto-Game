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
        self.player_id_store()

    def text_fill(self):
        with open(str(self.dict["Player ID"]) + ".txt", "w") as player_file:
            player_file.write(json.dumps(self.dict))

    def text_get(self):
        with open(self.dict["Player ID"] + ".txt", "r") as player_file:
            player_details = json.loads(player_file.read())
            return player_details

    def player_id_store(self):
        with open("player.txt", "w") as player_id:
            player_id.write(json.dumps(self.player_ID))


# player = Player("Nasar", "Kamish", 18, "012839", "nasarkamish@gmail.com", "ZAR", 0, "Nk2014")
# player.text_fill()
