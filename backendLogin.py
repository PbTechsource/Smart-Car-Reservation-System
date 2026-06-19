import tkinter as tk
import signuppage, json
from tkinter import messagebox
import main_dashbord


def login_user(username, password, window):
    try:
        with open("users.json","r") as f:
            users=json.load(f)
    except:
        users={}

    if username not in users:
        messagebox.showerror("Error","User not found")
        return
    if users[username]["password"] != password:
        messagebox.showerror("Error","Wrong password")
        return

    role = users[username].get("role","User")
    window.destroy()
    main_dashbord.start_dashboard(role)


def switch_to_signup_page(window):
    window.destroy()
    signuppage.main_signup()
