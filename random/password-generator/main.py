from tkinter import *
from tkinter import messagebox
import json

window = Tk()
window.title("Password generator")
window.config(width=400, height=450)


password_list = []



import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    letter_list = [random.choice(letters) for _ in range (nr_letters)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    char_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letter_list + number_list + char_list


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, f"{password}")


website = Label(text="Website", font=("courier", 15, "bold"))
website.grid(column=1, row=2)

website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()

email = Label(text="Email",font=("courier",15, "bold"))
email.grid(column=1, row=3)

email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(END, "simone.marton89@gmail.com")

password = Label(text="Password", font=("courier", 15, "bold"))
password.grid(column=1, row=4)

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

button = Button(text="Generate password", command=generate_password)
button.grid(column=3, row=4)

data = {
    website :{
        "email":email,
        "password": password
    }
}

def add_function():

    if len(email_entry.get()) == 0 or len(password_entry.get())== 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="please don t leave any field empty")

    else:
            with open("data.json", "w") as file:  
                json.dumb(data, file)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


button_add = Button(text="Add", command=add_function)
button_add.config(width=36)
button_add.grid(column=2, row=5, columnspan=2)










window.mainloop()