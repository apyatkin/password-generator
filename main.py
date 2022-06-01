from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    password = entry_password.get()
    email = entry_email.get()
    password_entry = f"{website} | {email} | {password}\n"
    with open("data.txt", mode="a") as datafile:
        datafile.write(password_entry)
        entry_email.delete(0, END)
        entry_password.delete(0, END)
        entry_website.delete(0, END)
        entry_email.insert(0, "av.pyatkin@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
logo = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Username/Email:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)

entry_email = Entry(width=35)
entry_email.insert(0, "av.pyatkin@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons
button_generate = Button(text="Generate Password")
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4)

window.mainloop()
