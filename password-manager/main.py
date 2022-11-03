from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# Password Generator Section
# before generating a new password, delete the password that was there initially
# use pass_gen() to generate password and store it in "generated_password"
# use pyperclip to copy generated password to clipboard
# insert generated password into the -password_entry-
def generate():
    password_entry.delete(0, END)
    generated_password = pass_gen()
    pyperclip.copy(generated_password)
    password_entry.insert(END, string=generated_password)


# This function generates a new password
def pass_gen():
    numbers = "0123456789"
    symbols = "!@#$().%*"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # concatenate numbers, symbols, lower and upper
    concat_all = lower + upper + numbers + symbols
    length = 13
    # selects randomly from the variable concat_all and the join method makes it a string
    the_password = "".join(random.sample(concat_all, length))

    return the_password


# Save Password
# when user inputs all necessary details and clicks "save", the details are held in a dictionary(new_data)
# then each new_data is saved in the json file
def save():
    the_website = website_entry.get()
    the_email_username = email_username_entry.get()
    the_password = password_entry.get()
    new_data = {
        the_website: {
            "email": the_email_username,
            "password": the_password,
        }
    }

    if len(the_website) == 0 and len(the_password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")

    else:
        entry_ok = messagebox.askokcancel(title=the_website, message=f"These are the details entered: "
                                                                     f"\nEmail: {the_email_username} \nPassword: "
                                                                     f"{the_password} \nDo you want to save?")
        if entry_ok:
            try:
                with open("data.json", "r") as details_file:
                    # Reading old data
                    data = json.load(details_file)
            except FileNotFoundError:
                with open("data.json", "w") as details_file:
                    json.dump(new_data, details_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as details_file:
                    # saving updated data
                    json.dump(data, details_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# to find a password/details of a given website, open and load the json file that stores the data
# display the details of the searched website if it was previously stored
def find_password():
    the_website = website_entry.get()
    try:
        with open("data.json") as file:
            data_file = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if the_website in data_file:
            email = data_file[the_website]["email"]
            the_pass = data_file[the_website]["password"]
            messagebox.showinfo(title=the_website, message=f"Email: {email} \nPassword: {the_pass}")
        else:
            messagebox.showinfo(title="Error", message=f"Details Not Found For '{the_website}' ")


# UI SETUP


# Configure the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# configure the canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# configure the Labels
website = Label(text="Website:")
website.grid(row=1, column=0)


email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)


password = Label(text="Password:")
password.grid(row=3, column=0)


# The Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_username_entry = Entry()
email_username_entry.insert(0, string="spacesurfer3005@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

gen_password_button = Button(text="Generate Password", command=generate)
gen_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
