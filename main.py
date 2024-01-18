from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    total_password = ""
    for char in password_list:
        total_password += char
    password_entry.insert(0, total_password)
    # paperclip.copy(total_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    # Checking whether fields are empty or not
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please Make Sure that You Haven't left any Fields Empty.")
    else:
        # Exception Handling
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FINDING PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Search is not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=27)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.insert(0, "abc@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

# buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
