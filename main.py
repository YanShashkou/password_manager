import tkinter
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters=[random.choice(letters) for i in range(nr_letters)]
    password_symbols=[random.choice(symbols) for i in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for i in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    print(password)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    #
    # random.shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == '' or email == '' or password == '':
        messagebox.showerror('Something went wrong', 'Please fill all fields')
    else:
        messagebox.showinfo("Success",'Password has been saved!')
        website_entry.delete(0,tkinter.END)
        password_entry.delete(0,tkinter.END)
        with open("data.txt",'a') as data:
            data.write(f"{website} | {email} | {password}\n")
# ---------------------------- UI SETUP ------------------------------- #
# window and logo
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
logo=tkinter.Canvas(height=200,width=189)
image=tkinter.PhotoImage(file='logo.png')
logo.create_image(100,110,image=image)
logo.grid(column=1,row=0)
# ////////////////////////////////
website_label = tkinter.Label(text='Website')
website_label.grid(column=0,row=1)
email_label = tkinter.Label(text='Email/Username')
email_label.grid(column=0,row=2)
password_label = tkinter.Label(text='Password')
password_label.grid(column=0,row=3)
website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry = tkinter.Entry(width=35)
email_entry.insert(0,'shashkou.yan@gmail.com')
email_entry.grid(column=1,row=2,columnspan=2)
password_entry = tkinter.Entry(width=35)
password_entry.grid(column=1,row=3,columnspan=2)
generate_button = tkinter.Button(text='Generate Password',command=generate_password)
generate_button.grid(column=2,row=3)
add_button = tkinter.Button(text='Add',width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
window.mainloop()