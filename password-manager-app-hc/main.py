from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pw_input.insert(0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_username_input.get()
    password = pw_input.get()
    new_data = {
        website: {
            "email/username": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
            messagebox.showwarning(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data:
                # Read old data
                data_json = json.load(data)
        except FileNotFoundError:
            with open ("data.json", mode="w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # Update old data with new data
            data_json.update(new_data)

            with open("data.json", mode="w") as data:
                # Save updated data
                json.dump(data_json, data, indent=4)
        finally:
            website_input.delete(0, END)
            pw_input.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():

    website = website_input.get()

    try:
        with open("data.json", mode="r") as data:
            data_json = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    else:
        if website in data_json:
            email = data_json[website].get('email/username')
            password = data_json[website].get('password')
            messagebox.showinfo(title="User Details",message=f"These are the details: \n\nEmail: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Please add website", message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# create canvas
canvas = Canvas(width=200, height= 200, bg= "white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=lock_img)
canvas.grid(row=0, column=1)

# create labels
website = Label(text="Website:")
website.grid(row=1, column=0)
website.config(bg="white", fg="black")

email_username = Label(text="Email/Username:")
email_username .grid(row=2, column=0)
email_username .config(bg="white", fg="black")

pw = Label(text="Password:")
pw.grid(row=3, column=0)
pw.config(bg="white", fg="black")

# create entry input
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()
website_input.config(bg="white", highlightbackground="white", fg="black")

email_username_input = Entry(width=38)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, string="john.doe@gmail.com")
email_username_input.config(bg="white", highlightbackground="white", fg="black")

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)
pw_input.config(bg="white", highlightbackground="white", fg="black")

# create buttons
add_pw = Button(text="Add", command=save)
add_pw.grid(row=4, column=1, columnspan=2)
add_pw.config(width=36, highlightbackground="white")

generate_pw = Button(text="Generate Password", command=generate_pw)
generate_pw.grid(row=3, column=2)
generate_pw.config(highlightbackground="white")

search = Button(text="Search", command=find_password, width=13)
search.grid(row=1, column=2)
search.config(highlightbackground="white")

window.mainloop()
