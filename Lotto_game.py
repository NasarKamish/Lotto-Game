# Nasar Kamish cohort 8 Group 2
from tkinter import *
from tkinter import messagebox

Game = Tk()
Game["bg"] = "yellow"
Game.title("Lotto game")
Game.geometry("750x450")


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
en_Guess_1 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
en_Guess_1["font"] = "Times", 15
en_Guess_1.place(x=10, y=10, width=75)

en_Guess_2 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
en_Guess_2["font"] = "Times", 15
en_Guess_2.place(x=110, y=10, width=75)

en_Guess_3 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
en_Guess_3["font"] = "Times", 15
en_Guess_3.place(x=210, y=10, width=75)

en_Guess_4 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
en_Guess_4["font"] = "Times", 15
en_Guess_4.place(x=10, y=50, width=75)

en_Guess_5 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
en_Guess_5["font"] = "Times", 15
en_Guess_5.place(x=110, y=50, width=75)

en_Guess_6 = Spinbox(fm_Enter, bg="Yellow", from_=1, to=49)
en_Guess_6["font"] = "Times", 15
en_Guess_6.place(x=210, y=50, width=75)
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
en_Lotto_1 = Spinbox(fm_Lotto, bg="Yellow", from_=1, to=49)
en_Lotto_1["font"] = "Times", 15
en_Lotto_1.place(x=10, y=10, width=75)

en_Lotto_2 = Spinbox(fm_Lotto, bg="Yellow", from_=1, to=49)
en_Lotto_2["font"] = "Times", 15
en_Lotto_2.place(x=110, y=10, width=75)

en_Lotto_3 = Spinbox(fm_Lotto, bg="Yellow", from_=1, to=49)
en_Lotto_3["font"] = "Times", 15
en_Lotto_3.place(x=210, y=10, width=75)

en_Lotto_4 = Spinbox(fm_Lotto, bg="Yellow", from_=1, to=49)
en_Lotto_4["font"] = "Times", 15
en_Lotto_4.place(x=10, y=50, width=75)

en_Lotto_5 = Spinbox(fm_Lotto, bg="Yellow", from_=1, to=49)
en_Lotto_5["font"] = "Times", 15
en_Lotto_5.place(x=110, y=50, width=75)

en_Lotto_6 = Spinbox(fm_Lotto, bg="Yellow", from_=1, to=49)
en_Lotto_6["font"] = "Times", 15
en_Lotto_6.place(x=210, y=50, width=75)
# Lotto spin boxes end

# Lotto end

# Generate btn start
btn_Generate = Button(Game, text="Generate Lotto Number", bg="white", borderwidth=5)
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
