# Nasar Kamish cohort 8 Group 2
from tkinter.ttk import Combobox

import requests
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import random
import rsaidnumber
import player_Class

Login = Tk()
Login["bg"] = "yellow"
Login.geometry("750x400")
Login.title("Log-in")
currencies = []
current_age = 0
try:
    url = "https://currencyscoop.p.rapidapi.com/currencies"
    headers = {
        'x-rapidapi-key': "eb778cf435mshb0f9b12ab459937p1641a7jsnb899e5de27e9",
        'x-rapidapi-host': "currencyscoop.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    currencies = []
    for key in data["response"]["fiats"].keys():
        currencies.append(key)
except requests.ConnectionError:
    messagebox.showerror("Network Error", "No internet connection")
    exit()


def age_cal():
    global current_age
    now = datetime.date.today()
    if int(en_ID.get()[:2]) >= 21:
        age = int("19" + en_ID.get()[:2])
    else:
        age = int("20" + en_ID.get()[:2])
    current_age = int(now.year) - int(age)
    if current_age >= 18:
        email_verify()
    else:
        sound()
        messagebox.showerror("Error", "You are too young to enter")


def sound():
    playsound("Computer Error sound effect.mp3")


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        Login.destroy()


def id_verify():
    try:
        id_number = rsaidnumber.parse(en_ID.get())
        if id_number.valid:
            age_cal()
    except:
        sound()
        messagebox.showerror("awe", "awe")


def space_verify():
    if en_Name.get() == "":
        sound()
        messagebox.showerror("Error", "Enter your name")
    elif en_Surname.get() == "":
        sound()
        messagebox.showerror("Error", "Enter your surname")
    elif cmb_Currency.get() == "":
        sound()
        messagebox.showerror("Error", "Choose your currency")
    else:
        id_verify()


def email_verify():
    if en_Email.get() == "":
        sound()
        messagebox.showerror("Error", "Enter a valid Email")
    elif en_Email.get() != "":
        try:
            sender_email_id = 'jimmy.local.lotto.game@gmail.com'
            receiver_email_id = en_Email.get()
            password = "SMS31314NOW"
            subject = "Lotto"
            msg = MIMEMultipart()
            msg['From'] = sender_email_id
            msg['To'] = receiver_email_id
            msg['Subject'] = subject
            body = "You are a verified account"
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_email_id, password)
            s.sendmail(sender_email_id, receiver_email_id, text)
            s.quit()
            populate_dict()
        except:
            sound()
            messagebox.showerror("Error", "invalid Email, please make sure to put in right email")


def populate_dict():
    user_age = current_age
    user_name = en_Name.get()
    user_surname = en_Surname.get()
    user_email = en_Email.get()
    user_id = en_ID.get()
    user_Currency = cmb_Currency.get()
    user_player_id = player_id_create()
    user = player_Class.Player(user_name, user_surname, user_age, user_id, user_email, user_Currency, 0, user_player_id)
    user.text_fill()
    messagebox.showinfo("Welcome", "Lets play!")
    Login.destroy()
    import Lotto_game


def player_id_create():
    player_initials = en_Name.get()[:1] + en_Surname.get()[:1]
    player_dob = en_ID.get()[:6]
    player_unique_number = str(random.randint(-1, 10)) + str(random.randint(-1, 10)) + str(random.randint(-1, 10))
    player_unique_number = player_unique_number + str(random.randint(-1, 10)) + str(random.randint(-1, 10))
    player_id = player_initials + player_dob + player_unique_number
    return player_id


# head start
lbl_head = Label(Login, text="Log-in", bg="yellow")
lbl_head["font"] = "Times", 20
lbl_head.place(x=0, y=10, width=750)
# head end

# Row 1 start
# Name start
lbl_Name = Label(Login, text="Name:", bg="yellow")
lbl_Name["font"] = "Times", 15
lbl_Name.place(x=50, y=70)

en_Name = Entry(Login)
en_Name["font"] = "Times", 15
en_Name.place(x=50, y=100, width=300)
# Name end

# ID start
lbl_ID = Label(Login, text="ID Number:", bg="yellow")
lbl_ID["font"] = "Times", 15
lbl_ID.place(x=400, y=70)

en_ID = Entry(Login)
en_ID["font"] = "Times", 15
en_ID.place(x=400, y=100, width=300)
# ID end
# Row 1 end

# Row 2 start
# Surname start
lbl_Surname = Label(Login, text="Surname:", bg="yellow")
lbl_Surname["font"] = "Times", 15
lbl_Surname.place(x=50, y=170)

en_Surname = Entry(Login)
en_Surname["font"] = "Times", 15
en_Surname.place(x=50, y=200, width=300)
# Surname end

# Currency start
lbl_Currency = Label(Login, text="Currency:", bg="yellow")
lbl_Currency["font"] = "Times", 15
lbl_Currency.place(x=400, y=170)

cmb_Currency = Combobox(Login)
cmb_Currency["font"] = "Times", 15
cmb_Currency["state"] = "readonly"
cmb_Currency["values"] = currencies
cmb_Currency.place(x=400, y=200, width=300)
# Currency end
# Row 2 end

# Row 3 start
# Email start
lbl_Email = Label(Login, text="E-Mail:", bg="yellow")
lbl_Email["font"] = "Times", 15
lbl_Email.place(x=50, y=270)

en_Email = Entry(Login)
en_Email["font"] = "Times", 15
en_Email.place(x=50, y=300, width=300)
# Email end

# Buttons start
# Continue start
btn_Continue = Button(Login, text="Continue", borderwidth=10, command=space_verify)
btn_Continue["font"] = "Times", 15
btn_Continue.place(x=400, y=270, width=130, height=60)
# Continue end

# Exit start
btn_Exit = Button(Login, text="Exit", borderwidth=10, command=ex)
btn_Exit["font"] = "Times", 15
btn_Exit.place(x=570, y=270, width=130, height=60)
# Exit end
# Buttons end
# Row 3 end


Login.mainloop()
