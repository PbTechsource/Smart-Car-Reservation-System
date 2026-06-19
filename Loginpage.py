import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import backendLogin


def main_login():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


    window = ctk.CTk()
    window.geometry("1166x718")
    window.title("Modern Login Page")
    window.resizable(False, False)


    try:
        bg_image = Image.open("images/backgroundlogin.jpg")
        bg_image = bg_image.resize(size=(1200,750))
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        window.configure(fg_color="#0f172a")


    loginFrame = ctk.CTkFrame(window, width=450, height=480, corner_radius=20, fg_color="#1e1e2f")
    loginFrame.place(relx=0.5, rely=0.5, anchor="center")


    title_label = ctk.CTkLabel(
        loginFrame, text="Welcome Back", font=ctk.CTkFont("Poppins", 26, "bold"), text_color="white"
    )
    title_label.place(relx=0.5, rely=0.15, anchor="center")


    username_label = ctk.CTkLabel(loginFrame, text="Username:", font=ctk.CTkFont("Arial", 14))
    username_label.place(relx=0.1, rely=0.28)
    username_entry = ctk.CTkEntry(loginFrame, width=320, height=40, corner_radius=8)
    username_entry.place(relx=0.1, rely=0.33)


    password_label = ctk.CTkLabel(loginFrame, text="Password:", font=ctk.CTkFont("Arial", 14))
    password_label.place(relx=0.1, rely=0.44)
    password_entry = ctk.CTkEntry(loginFrame, width=320, height=40, corner_radius=8, show="●")
    password_entry.place(relx=0.1, rely=0.49)


    login_btn = ctk.CTkButton(
        loginFrame,
        text="LOGIN",
        width=320,
        height=45,
        corner_radius=10,
        fg_color="#00FFC6",
        text_color="#000000",
        hover_color="#00E0B0",
        command=lambda: backendLogin.login_user(username_entry.get(), password_entry.get(), window),
    )
    login_btn.place(relx=0.1, rely=0.62)


    signup_btn = ctk.CTkButton(
        loginFrame,
        text="Dont have an account? Sign up",
        width=320,
        height=35,
        corner_radius=10,
        fg_color="transparent",
        hover_color="#222222",
        text_color="#00FFC6",
        command=lambda: backendLogin.switch_to_signup_page(window),
    )
    signup_btn.place(relx=0.1, rely=0.75)


    back_btn = ctk.CTkButton(
        loginFrame,
        text="← Back",
        width=80,
        height=30,
        corner_radius=6,
        fg_color="transparent",
        text_color="#FFFFFF",
        hover_color="#222222",
        command=lambda: backendLogin.switch_to_signup_page(window),
    )
    back_btn.place(x=10, y=10)

    window.mainloop()


if __name__ == "__main__":
    main_login()