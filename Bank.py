# Nasar Kamish cohort 8 Group 2
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from playsound import playsound
import player_Class
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Claim = Tk()
Claim.title("Claim Reward")
Claim.geometry("750x360")
Claim["bg"] = "yellow"
user_dict = {}
user = {}


def send_email():
    try:
        sender_email_id = 'jimmy.local.lotto.game@gmail.com'
        receiver_email_id = user_dict["Email"]
        password = "SMS31314NOW"
        subject = "Lotto"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "You are claiming " + str(user_dict["Prize"]) + " " + str(user_dict["Currency"]) + "\n"
        body = body + "The Account holder is " + en_Holder.get() + "\n"
        body = body + "The Account number is " + en_Number.get() + "\n"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
        messagebox.showinfo("Email", "Email has been sent")
    except:
        sound()
        messagebox.showerror("Error", "There was an error")


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
        player_file.write(json.dumps(user))


def class_create():
    global user_dict
    global user
    user_dict = file_get()
    user = player_Class.Player(user_dict["Name"], user_dict["Surname"], user_dict["Age"], user_dict["ID"], user_dict["Email"], user_dict["Currency"], user_dict["Prize"], user_dict["Player ID"])


def sound():
    playsound("Computer Error sound effect.mp3")


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        Claim.destroy()


def account_number_validation():
    if not len(en_Number.get()) > 8:
        sound()
        messagebox.showerror("Error", "Enter a valid account number (8+ characters)")
    else:
        try:
            int(en_Number.get())
            send_email()
        except ValueError as Ve:
            messagebox.showerror("Error", Ve)


def space_validation():
    if en_Holder.get() == "":
        sound()
        messagebox.showerror("Error", "Please enter your account holder")
    elif en_Number.get() == "":
        sound()
        messagebox.showerror("Error", "Please enter your account number")
    elif cmb_Bank.get() == "":
        sound()
        messagebox.showerror("Error", "Please enter your bank")
    else:
        account_number_validation()


class_create()

# head start
lbl_head = Label(Claim, text="Bank Account", bg="yellow")
lbl_head["font"] = "Times", 20
lbl_head.place(x=0, y=10, width=750)
# head end

# Holder start
lbl_Holder = Label(Claim, text="Account Holder:", bg="yellow")
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
btn_Claim["command"] = space_validation
btn_Claim["font"] = "Times", 15
btn_Claim.place(x=50, y=270, width=300)

btn_Exit = Button(Claim, text="Exit", borderwidth=5, command=ex)
btn_Exit["font"] = "Times", 15
btn_Exit.place(x=400, y=270, width=300)
# Buttons end

Claim.mainloop()
