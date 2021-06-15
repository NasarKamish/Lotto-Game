# Nasar Kamish cohort 8 Group 2
import requests
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Login = Tk()
Login["bg"] = "yellow"
Login.geometry("750x500")
Login.title("Log-in")
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
    pass


def sound():
    playsound("Computer Error sound effect.mp3")


def ex():
    message = messagebox.askquestion("Exit", "Are you sure")
    if message == "yes":
        Login.destroy()


def verify():
    valid_counter = 9
    if en_Name.get() == "":
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "Enter your name")
    if en_Surname.get() == "":
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "Enter your surname")
    if en_Email.get() == "":
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "Enter a valid Email")
    if len(en_ID.get()) != 13:
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "ID must be 13 characters")
    if len(en_ID.get()) == 13:
        try:
            valid = int(en_ID.get())
            en_ID["text"] = str(valid)
        except ValueError as val:
            if valid_counter == 9:
                valid_counter -= 1
                sound()
                messagebox.showerror("Error", val)
    if en_Street_Name.get == "":
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "Enter your Street name")
    if en_Area.get() == "":
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "Enter your Area name")
    if en_Postal.get() == "":
        if valid_counter == 9:
            valid_counter -= 1
            sound()
            messagebox.showerror("Error", "Enter your Postal code")
    if en_Email.get() != "":
        if valid_counter == 9:
            try:
                sender_email_id = 'jimmy.local.lotto.game@gmail.com'
                receiver_email_id = en_Email.get()
                password = "SMS31314NOW"
                subject = "Lotto"
                msg = MIMEMultipart()
                msg['From'] = sender_email_id
                msg['To'] = receiver_email_id
                msg['Subject'] = subject
                body = "You are verified account"
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender_email_id, password)
                s.sendmail(sender_email_id, receiver_email_id, text)
                s.quit()
                Login.destroy()
                import Lotto_game
            except:
                if valid_counter == 9:
                    valid_counter -= 1
                    sound()
                    messagebox.showerror("Error", "invalid Email, please make sure to put in right email")


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

# Street start
lbl_Street_Name = Label(Login, text="Street Name:", bg="yellow")
lbl_Street_Name["font"] = "Times", 15
lbl_Street_Name.place(x=400, y=70)

en_Street_Name = Entry(Login)
en_Street_Name["font"] = "Times", 15
en_Street_Name.place(x=400, y=100, width=300)
# Street end
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

# Area start
lbl_Area = Label(Login, text="Area Name:", bg="yellow")
lbl_Area["font"] = "Times", 15
lbl_Area.place(x=400, y=170)

en_Area = Entry(Login)
en_Area["font"] = "Times", 15
en_Area.place(x=400, y=200, width=300)
# Area end
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

# Postal start
lbl_Postal = Label(Login, text="Postal Code:", bg="yellow")
lbl_Postal["font"] = "Times", 15
lbl_Postal.place(x=400, y=270)

en_Postal = Entry(Login)
en_Postal["font"] = "Times", 15
en_Postal.place(x=400, y=300, width=300)
# Postal end
# Row 3 end

# Row 4 start
# ID start
lbl_ID = Label(Login, text="ID Number:", bg="yellow")
lbl_ID["font"] = "Times", 15
lbl_ID.place(x=50, y=370)

en_ID = Entry(Login)
en_ID["font"] = "Times", 15
en_ID.place(x=50, y=400, width=300)
# ID end

# Buttons start
# Continue start
btn_Continue = Button(Login, text="Continue", borderwidth=10, command=verify)
btn_Continue["font"] = "Times", 15
btn_Continue.place(x=400, y=370, width=130, height=60)
# Continue end

# Exit start
btn_Exit = Button(Login, text="Exit", borderwidth=10, command=ex)
btn_Exit["font"] = "Times", 15
btn_Exit.place(x=570, y=370, width=130, height=60)
# Exit end
# Buttons end
# Row 4 end

Login.mainloop()
