# Nasar Kamish cohort 8 Group 2
import random
from tkinter import *
from tkinter import messagebox

Game = Tk()
Game["bg"] = "yellow"
Game.title("Lotto game")
Game.geometry("750x450")


def play_again():
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

    btn_Play["state"] = "disable"
    btn_Generate["state"] = "normal"
    btn_Claim["state"] = "disable"


def play():
    # btn_Claim["state"] = "normal"
    # btn_Generate["state"] = "disable"
    # btn_Play["state"] = "normal"

    generate_list = list(range(1, 50))
    random.shuffle(generate_list)
    generate_list = generate_list[:6]
    input_list = list((int(sb_Guess_1.get()), int(sb_Guess_2.get()), int(sb_Guess_3.get()), int(sb_Guess_4.get()), int(sb_Guess_5.get()), int(sb_Guess_6.get())))
    matched_list = list(set(generate_list).intersection(input_list))
    numbers_matched = len(matched_list)
    print(matched_list)
    print(numbers_matched)
    print(input_list)
    print(generate_list)


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        Game.destroy()


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
lbl_Output = Label(Game, text="You have 6 matches and you won R10,000", bg="Yellow")
lbl_Output["font"] = "Times", 15
lbl_Output.place(x=50, y=270, width=650)
# output end

# Bottom buttons start
btn_Play = Button(Game, text="Play again", bg="white", borderwidth=5)
btn_Play["font"] = "Times", 15
btn_Play.place(x=50, y=300, width=300)

btn_Claim = Button(Game, text="Claim Reward", bg="white", borderwidth=5)
btn_Claim["font"] = "Times", 15
btn_Claim.place(x=400, y=300, width=300)

btn_Exit = Button(Game, text="Exit", bg="white", borderwidth=5, command=ex)
btn_Exit["font"] = "Times", 15
btn_Exit.place(x=200, y=360, width=350)
# Bottom buttons end

Game.mainloop()
