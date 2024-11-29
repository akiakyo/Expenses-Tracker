from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, OptionMenu, Listbox, END
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import csv
import app
from app import newWindow

window = Tk()
window.title('Login')
window.geometry('925x500+300+200')
window.configure(bg="#0d0e16")  # Dark background
window.resizable(False, False)

# Ensure the CSV file exists
if not os.path.isfile("users.csv"):
    with open("users.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password"])  # Add header for the file

def signin():
    username = user.get()
    password = code.get()

    if username == '' or password == '':
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate against the user data in users.csv
    with open("users.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username and row["Password"] == password:
                # Close the login window and open the Dashboard
                window.destroy()  # Close the login window
                newWindow()  # Open the Dashboard
                return

    messagebox.showerror("Invalid", "Invalid username or password")


def signup():
    def save_user():
        new_username = new_user.get()
        new_password = new_code.get()

        if new_username == '' or new_password == '':
            messagebox.showerror("Error", "All fields are required")
            return

        # Check if the username already exists
        with open("users.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Username"] == new_username:
                    messagebox.showerror("Error", "Username already exists!")
                    return

        # Append new user to the CSV file
        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_username, new_password])
        messagebox.showinfo("Success", "Account created successfully!")
        signup_screen.destroy()

    signup_screen = Toplevel(window)
    signup_screen.title("Sign Up")
    signup_screen.geometry('400x400+400+200')
    signup_screen.configure(bg="#0d0e16")
    signup_screen.resizable(False, False)

    Label(signup_screen, text="Sign Up", fg='#57a1f8', bg='#0d0e16',
          font=('Microsoft YaHei UI Light', 23, 'bold')).pack(pady=20)

    new_user = Entry(signup_screen, width=25, fg='white', border=0,
                     bg='#1e1f29', font=('Microsoft YaHei UI Light', 11))
    new_user.pack(pady=10)
    new_user.insert(0, 'New Username')
    new_user.bind('<FocusIn>', lambda e: new_user.delete(0, 'end') if new_user.get() == 'New Username' else None)
    new_user.bind('<FocusOut>', lambda e: new_user.insert(0, 'New Username') if new_user.get() == '' else None)

    Frame(signup_screen, width=295, height=2, bg='#57a1f8').pack()

    new_code = Entry(signup_screen, width=25, fg='white', border=0,
                     bg='#1e1f29', font=('Microsoft YaHei UI Light', 11))
    new_code.pack(pady=10)
    new_code.insert(0, 'New Password')
    new_code.bind('<FocusIn>', lambda e: new_code.delete(0, 'end') if new_code.get() == 'New Password' else None)
    new_code.bind('<FocusOut>', lambda e: new_code.insert(0, 'New Password') if new_code.get() == '' else None)

    Frame(signup_screen, width=295, height=2, bg='#57a1f8').pack()

    Button(signup_screen, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0,
           command=save_user).pack(pady=20)


# Load and place the image
img1 = PhotoImage(file='assets/lazy.png')
Label(window, image=img1, bg='#0d0e16').place(x=0, y=0, width=450, height=500)

# Ensure that the image is not garbage-collected
window.img1 = img1

frame = Frame(window, width=350, height=350, bg="#1e1f29")
frame.place(x=480, y=70)


heading = Label(frame, text='Sign in', fg='#57a1f8', bg='#1e1f29',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=111, y=5)

# Username entry
def on_enter(e):
    user.delete(0, 'end')
    code.config(show="•")  # Start masking input

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')
        code.config(show="")  # Show placeholder text unmasked

user = Entry(frame, width=25, fg='white', border=0, bg='#1e1f29', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='#57a1f8').place(x=25, y=107)

# Password entry
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='white', border=0, bg='#1e1f29', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='#57a1f8').place(x=25, y=177)

# Sign In Button
Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='white', bg='#1e1f29', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='#1e1f29', cursor='hand2', fg='#57a1f8', command=signup)
sign_up.place(x=215, y=270)

window.mainloop()
