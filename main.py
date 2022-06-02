from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    gen_password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_field():
    entry_email.delete(0, END)
    entry_password.delete(0, END)
    entry_website.delete(0, END)
    entry_email.insert(0, "av.pyatkin@gmail.com")


def save():
    website = entry_website.get()
    password = entry_password.get()
    email = entry_email.get()
    password_entry = f"{website} | {email} | {password}\n"

    if len(website) < 1 or len(password) < 1:
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty!")
        clear_field()
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it OK to save?")
        if is_ok:
            with open("data.txt", mode="a") as datafile:
                datafile.write(password_entry)
                clear_field()


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
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4)

window.mainloop()
