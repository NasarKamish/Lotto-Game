# Nasar Kamish cohort 8 Group 2
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from playsound import playsound

Claim = Tk()
Claim.title("Claim Reward")
Claim.geometry("750x360")
Claim["bg"] = "yellow"


def sound():
    playsound("Computer Error sound effect.mp3")


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        Claim.destroy()


def space_validation():
    if en_Holder.get() == "":
        sound()
        messagebox.showerror("Error", "Please enter the account holder")
    elif en_Number.get() == "":
        sound()
        messagebox.showerror("Error", "Please enter the account number")
    else:
        pass


# head start
lbl_head = Label(Claim, text="Bank Account", bg="yellow")
lbl_head["font"] = "Times", 20
lbl_head.place(x=0, y=10, width=750)
# head end

# Holder start
lbl_Holder = Label(Claim, text="Account Details:", bg="yellow")
lbl_Holder["font"] = "Times", 15
lbl_Holder.place(x=50, y=70)

en_Holder = Entry(Claim)
en_Holder["font"] = "Times", 15
en_Holder.place(x=50, y=100, width=300)
# Holder end

# Number start
lbl_Number = Label(Claim, text="Account Number:", bg="yellow")
lbl_Number["font"] = "Times", 15
lbl_Number.place(x=400, y=70)

en_Number = Entry(Claim)
en_Number["font"] = "Times", 15
en_Number.place(x=400, y=100, width=300)
# Number end

# Bank start
lbl_Bank = Label(Claim, text="Bank:", bg="yellow")
lbl_Bank["font"] = "Times", 15
lbl_Bank.place(x=0, y=170, width=750)

cmb_Bank = Combobox(Claim)
cmb_Bank["font"] = "Times", 15
cmb_Bank["state"] = "readonly"
cmb_Bank["values"] = ["Capitec", "African Bank", "Nedbank", "FNB", "Absa", "Standard Bank"]
cmb_Bank.place(x=200, y=200, width=350)
# Bank end

# Buttons start
btn_Claim = Button(Claim, text="Claim Reward", borderwidth=5)
btn_Claim["font"] = "Times", 15
btn_Claim.place(x=50, y=270, width=300)

btn_Exit = Button(Claim, text="Exit", borderwidth=5, command=ex)
btn_Exit["font"] = "Times", 15
btn_Exit.place(x=400, y=270, width=300)
# Buttons end

Claim.mainloop()
