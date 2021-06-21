# Nasar Kamish cohort 8 Group 2
import random
from tkinter import *
from tkinter import messagebox
import player_Class
import json

Game = Tk()
Game["bg"] = "yellow"
Game.title("Lotto game")
Game.geometry("750x450")
prices = [0.00, 0.00, 20.00, 100.50, 2384.00, 8584.00, 10000000.00]
winnings = 0
user_dict = {}
user = {}


def file_get():
    with open("player.txt", "r") as player_file:
        player_id = json.loads(player_file.read())

    with open(str(player_id) + ".txt", "r") as player_file:
        player_details = json.loads(player_file.read())
        return player_details


def file_fill():
    with open("player.txt", "r") as player_file:
        player_id = json.loads(player_file.read())

    with open(str(player_id) + ".txt", "w") as player_file:
        player_file.write(json.dumps(str(user)))


def class_create():
    global user_dict
    global user
    user_dict = file_get()
    user = player_Class.Player(user_dict["Name"], user_dict["Surname"], user_dict["Age"], user_dict["ID"], user_dict["Email"], user_dict["Currency"], user_dict["Prize"], user_dict["Player ID"])


def play_again():
    lbl_Output["text"] = ""

    sb_Guess_1["state"] = "normal"
    sb_Guess_2["state"] = "normal"
    sb_Guess_3["state"] = "normal"
    sb_Guess_4["state"] = "normal"
    sb_Guess_5["state"] = "normal"
    sb_Guess_6["state"] = "normal"

    en_Lotto_1["state"] = "normal"
    en_Lotto_1.delete(0, END)
    en_Lotto_1["state"] = "readonly"

    en_Lotto_2["state"] = "normal"
    en_Lotto_2.delete(0, END)
    en_Lotto_2["state"] = "readonly"

    en_Lotto_3["state"] = "normal"
    en_Lotto_3.delete(0, END)
    en_Lotto_3["state"] = "readonly"

    en_Lotto_4["state"] = "normal"
    en_Lotto_4.delete(0, END)
    en_Lotto_4["state"] = "readonly"

    en_Lotto_5["state"] = "normal"
    en_Lotto_5.delete(0, END)
    en_Lotto_5["state"] = "readonly"

    en_Lotto_6["state"] = "normal"
    en_Lotto_6.delete(0, END)
    en_Lotto_6["state"] = "readonly"

    btn_Play["state"] = "disabled"
    btn_Generate["state"] = "normal"
    btn_Claim["state"] = "disabled"


def play():
    btn_Claim["state"] = "normal"
    btn_Generate["state"] = "disabled"
    btn_Play["state"] = "normal"

    sb_Guess_1["state"] = "readonly"
    sb_Guess_2["state"] = "readonly"
    sb_Guess_3["state"] = "readonly"
    sb_Guess_4["state"] = "readonly"
    sb_Guess_5["state"] = "readonly"
    sb_Guess_6["state"] = "readonly"

    generate_list = list(range(1, 50))
    random.shuffle(generate_list)
    generate_list = generate_list[:6]
    input_list = list((int(sb_Guess_1.get()), int(sb_Guess_2.get()), int(sb_Guess_3.get()), int(sb_Guess_4.get()), int(sb_Guess_5.get()), int(sb_Guess_6.get())))
    matched_list = list(set(generate_list).intersection(input_list))
    numbers_matched = len(matched_list)

    lbl_Output["text"] = "You have " + str(numbers_matched) + " matches, and won " + str(prices[numbers_matched]) + " " + str(user_dict["Currency"])

    global winnings
    winnings = float(winnings) + float(prices[numbers_matched])

    en_Lotto_1["state"] = "normal"
    en_Lotto_2["state"] = "normal"
    en_Lotto_3["state"] = "normal"
    en_Lotto_4["state"] = "normal"
    en_Lotto_5["state"] = "normal"
    en_Lotto_6["state"] = "normal"

    en_Lotto_1.delete(0, END)
    en_Lotto_2.delete(0, END)
    en_Lotto_3.delete(0, END)
    en_Lotto_4.delete(0, END)
    en_Lotto_5.delete(0, END)
    en_Lotto_6.delete(0, END)

    en_Lotto_1.insert(0, generate_list[0])
    en_Lotto_2.insert(0, generate_list[1])
    en_Lotto_3.insert(0, generate_list[2])
    en_Lotto_4.insert(0, generate_list[3])
    en_Lotto_5.insert(0, generate_list[4])
    en_Lotto_6.insert(0, generate_list[5])

    en_Lotto_1["state"] = "readonly"
    en_Lotto_2["state"] = "readonly"
    en_Lotto_3["state"] = "readonly"
    en_Lotto_4["state"] = "readonly"
    en_Lotto_5["state"] = "readonly"
    en_Lotto_6["state"] = "readonly"


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        Game.destroy()


def claim():
    msg = messagebox.askquestion("Confirm", "Are you sure?")
    if msg == "yes":
        global user
        global user_dict
        user_dict["Prize"] = str(float(user_dict["Prize"]) + float(winnings))
        user = player_Class.Player(user_dict["Name"], user_dict["Surname"], user_dict["Age"], user_dict["ID"], user_dict["Email"], user_dict["Currency"], user_dict["Prize"], user_dict["Player ID"])
        user.text_fill()
        Game.destroy()
        import Bank


class_create()
# head start
lbl_head = Label(Game, text="Lotto Game", bg="yellow")
lbl_head["font"] = "Times", 20
lbl_head.place(x=0, y=10, width=750)
# head end

# Enter start
lbl_Enter = Label(Game, text="Enter your numbers:", bg="Yellow")
lbl_Enter["font"] = "Times", 15
lbl_Enter.place(x=50, y=70)

fm_Enter = LabelFrame(Game, bg="white")
fm_Enter["font"] = "Times", 15
fm_Enter.place(x=50, y=100, height=100, width=300)

# Guesses start
sb_Guess_1 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
sb_Guess_1["font"] = "Times", 15
sb_Guess_1.place(x=10, y=10, width=75)

sb_Guess_2 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
sb_Guess_2["font"] = "Times", 15
sb_Guess_2.place(x=110, y=10, width=75)

sb_Guess_3 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
sb_Guess_3["font"] = "Times", 15
sb_Guess_3.place(x=210, y=10, width=75)

sb_Guess_4 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
sb_Guess_4["font"] = "Times", 15
sb_Guess_4.place(x=10, y=50, width=75)

sb_Guess_5 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
sb_Guess_5["font"] = "Times", 15
sb_Guess_5.place(x=110, y=50, width=75)

sb_Guess_6 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
sb_Guess_6["font"] = "Times", 15
sb_Guess_6.place(x=210, y=50, width=75)
# Guesses end

# Enter end

# Lotto start
lbl_Lotto = Label(Game, text="Lotto Numbers:", bg="Yellow")
lbl_Lotto["font"] = "Times", 15
lbl_Lotto.place(x=400, y=70)

fm_Lotto = LabelFrame(Game, bg="white")
fm_Lotto["font"] = "Times", 15
fm_Lotto.place(x=400, y=100, height=100, width=300)

# Lotto spin boxes start
en_Lotto_1 = Entry(fm_Lotto, bg="Yellow")
en_Lotto_1["state"] = "readonly"
en_Lotto_1["font"] = "Times", 15
en_Lotto_1.place(x=10, y=10, width=75)

en_Lotto_2 = Entry(fm_Lotto, bg="Yellow")
en_Lotto_2["state"] = "readonly"
en_Lotto_2["font"] = "Times", 15
en_Lotto_2.place(x=110, y=10, width=75)

en_Lotto_3 = Entry(fm_Lotto, bg="Yellow")
en_Lotto_3["state"] = "readonly"
en_Lotto_3["font"] = "Times", 15
en_Lotto_3.place(x=210, y=10, width=75)

en_Lotto_4 = Entry(fm_Lotto, bg="Yellow")
en_Lotto_4["state"] = "readonly"
en_Lotto_4["font"] = "Times", 15
en_Lotto_4.place(x=10, y=50, width=75)

en_Lotto_5 = Entry(fm_Lotto, bg="Yellow")
en_Lotto_5["state"] = "readonly"
en_Lotto_5["font"] = "Times", 15
en_Lotto_5.place(x=110, y=50, width=75)

en_Lotto_6 = Entry(fm_Lotto, bg="Yellow")
en_Lotto_6["state"] = "readonly"
en_Lotto_6["font"] = "Times", 15
en_Lotto_6.place(x=210, y=50, width=75)
# Lotto spin boxes end

# Lotto end

# Generate btn start
btn_Generate = Button(Game, text="Generate Lotto Number", bg="white", borderwidth=5)
btn_Generate["command"] = play
btn_Generate["font"] = "Times", 15
btn_Generate.place(x=200, y=210, width=350)
# Generate btn end

# output start
lbl_Output = Label(Game, text="", bg="Yellow")
lbl_Output["font"] = "Times", 15
lbl_Output.place(x=50, y=270, width=650)
# output end

# Bottom buttons start
btn_Play = Button(Game, text="Play again", bg="white", borderwidth=5)
btn_Play["command"] = play_again
btn_Play["state"] = "disabled"
btn_Play["font"] = "Times", 15
btn_Play.place(x=50, y=300, width=300)

btn_Claim = Button(Game, text="Claim Reward", bg="white", borderwidth=5)
btn_Claim["command"] = claim
btn_Claim["state"] = "disabled"
btn_Claim["font"] = "Times", 15
btn_Claim.place(x=400, y=300, width=300)

btn_Exit = Button(Game, text="Exit", bg="white", borderwidth=5, command=ex)
btn_Exit["font"] = "Times", 15
btn_Exit.place(x=200, y=360, width=350)
# Bottom buttons end

Game.mainloop()
