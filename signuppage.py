import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os, json
import Loginpage

if not os.path.exists("users.json"):
    json.dump({}, open("users.json","w"))

def setup_window_signup():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    w=ctk.CTk(); w.geometry("1166x718"); w.resizable(False,False); return w

def setup_background(window):
    window.configure(fg_color="#1e1e2f")

def setFrameSignup(window):
    f=ctk.CTkFrame(window,fg_color="#1e1e2f",corner_radius=20)
    f.place(relx=0.5,rely=0.5,anchor="center",relwidth=0.38,relheight=0.55)
    return f

def signup_components(frame,window):
    role_var=ctk.StringVar(value="User")
    ctk.CTkLabel(frame,text="Sign up",font=("Arial",32,"bold")).place(relx=.5,rely=.12,anchor="center")
    ctk.CTkComboBox(frame,variable=role_var,values=["User","Admin"],width=400).place(relx=.05,rely=.23)
    usernameVar=ctk.StringVar(); passwordVar=ctk.StringVar()
    ctk.CTkEntry(frame,textvariable=usernameVar,width=400).place(relx=.05,rely=.40)
    ctk.CTkEntry(frame,textvariable=passwordVar,width=400,show="●").place(relx=.05,rely=.60)

    def signup_user():
        u=usernameVar.get().strip(); p=passwordVar.get().strip(); r=role_var.get()
        if not u or not p:
            messagebox.showerror("Error","Fill all fields") ; return
        with open("users.json","r") as f: users=json.load(f)
        if u in users:
            messagebox.showerror("Error","Username already exists") ; return
        users[u]={"password":p,"role":r}
        with open("users.json","w") as f: json.dump(users,f,indent=4)
        messagebox.showinfo("Success","Account created")
        window.destroy(); Loginpage.main_login()

    ctk.CTkButton(frame,text="SIGN UP",width=400,command=signup_user).place(relx=.05,rely=.75)
    ctk.CTkButton(frame,text="you have a account?",width=400,fg_color="transparent",command=lambda:(window.destroy(),Loginpage.main_login())).place(relx=.05,rely=.87)

def main_signup():
    w=setup_window_signup(); setup_background(w); f=setFrameSignup(w); signup_components(f,w); w.mainloop()