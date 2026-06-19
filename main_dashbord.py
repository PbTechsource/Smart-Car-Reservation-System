import customtkinter as ctk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

DATA_FILE = "cars.json"

def load_cars():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        cars = [
            {"name": "BMW M5 Competition", "count": 5},
            {"name": "Mercedes G63 AMG", "count": 4},
            {"name": "Audi R8", "count": 3},
            {"name": "Porsche 911 Turbo", "count": 2}
        ]
        save_cars(cars)
        return cars

def save_cars(cars):
    with open(DATA_FILE, "w") as f:
        json.dump(cars, f)

cars = load_cars()
cart = []
is_admin = True


def show_dashboard():
    clear_frame()



    title = ctk.CTkLabel(main_frame, text="Dashboard", font=("Arial", 26, "bold"), text_color="#00FFFF")
    title.pack(pady=10)

    for car in cars:
        frame = ctk.CTkFrame(main_frame, fg_color="#2b2b2b", corner_radius=12)
        frame.pack(fill="x", pady=8, padx=20)

        label = ctk.CTkLabel(frame, text=f"{car['name']} | available: {car['count']}", font=("Arial", 18))
        label.pack(side="left", padx=15, pady=10)

        reserve_btn = ctk.CTkButton(frame, text="Reserve", fg_color="#1E90FF", width=120, height=35,
                                    command=lambda c=car: reserve_car(c))
        reserve_btn.pack(side="right", padx=15, pady=10)

    if is_admin:
        admin_btn = ctk.CTkButton(main_frame, text="Admin Panel", fg_color="#FF4500", width=150, height=40, 
                                  command=show_admin_panel)
        admin_btn.pack(pady=15)


def reserve_car(car):
    if car["count"] > 0:
        car["count"] -= 1
        cart.append(car["name"])
        save_cars(cars)
        messagebox.showinfo("Reserved", f"{car['name']} reserved successfully.")
        show_dashboard()
    else:
        messagebox.showwarning("Error", "This car is not available!")


def show_cart():
    clear_frame()
    title = ctk.CTkLabel(main_frame, text="Your Booking Basket", font=("Arial", 26, "bold"), text_color="#00FFFF")
    title.pack(pady=10)

    if not cart:
        ctk.CTkLabel(main_frame, text="Your cart is empty.", font=("Arial", 16)).pack(pady=10)
    else:
        for i, c in enumerate(cart):
            frame = ctk.CTkFrame(main_frame, fg_color="#2b2b2b", corner_radius=10)
            frame.pack(fill="x", padx=20, pady=5)

            label = ctk.CTkLabel(frame, text=f"{c}", font=("Arial", 16))
            label.pack(side="left", padx=15, pady=5)

            remove_btn = ctk.CTkButton(frame, text="Remove", fg_color="#FF6347", width=100, height=30,
                                       command=lambda idx=i: remove_from_cart(idx))
            remove_btn.pack(side="right", padx=10, pady=5)

def remove_from_cart(index):
    if 0 <= index < len(cart):
        removed_car = cart.pop(index)
        for car in cars:
            if car["name"] == removed_car:
                car["count"] += 1
        save_cars(cars)
        messagebox.showinfo("Removed", f"{removed_car} removed from cart.")
        show_cart()


def show_admin_panel():
    clear_frame()
    title = ctk.CTkLabel(main_frame, text="Admin Panel", font=("Arial", 26, "bold"), text_color="#00FFFF")
    title.pack(pady=10)

    for car in cars:
        frame = ctk.CTkFrame(main_frame, fg_color="#2b2b2b", corner_radius=10)
        frame.pack(fill="x", pady=5, padx=15)

        label = ctk.CTkLabel(frame, text=f"{car['name']} | available: {car['count']}", font=("Arial", 18))
        label.pack(side="left", padx=15, pady=8)

        plus_btn = ctk.CTkButton(frame, text="+", width=45, height=35, command=lambda c=car: change_count(c, 1))
        plus_btn.pack(side="right", padx=5)

        minus_btn = ctk.CTkButton(frame, text="-", width=45, height=35, command=lambda c=car: change_count(c, -1))
        minus_btn.pack(side="right", padx=5)

    ctk.CTkButton(main_frame, text="Show Chart", fg_color="#32CD32", width=180, height=40,
                  command=show_chart).pack(pady=20)


def change_count(car, delta):
    car["count"] = max(0, car["count"] + delta)
    save_cars(cars)
    show_admin_panel()


def show_chart():
    names = [car["name"] for car in cars]
    counts = [car["count"] for car in cars]

    plt.bar(names, counts)
    plt.title("Available Cars")
    plt.xlabel("Car Name")
    plt.ylabel("Count")
    plt.xticks(rotation=15)
    plt.show()


def search_car():
    query = search_entry.get().lower()
    clear_frame()

    results = [car for car in cars if query in car["name"].lower()]
    if not results:
        ctk.CTkLabel(main_frame, text="Car not found!", font=("Arial", 18)).pack(pady=10)
    else:
        for car in results:
            frame = ctk.CTkFrame(main_frame, fg_color="#2b2b2b")
            frame.pack(fill="x", pady=5, padx=10)
            label = ctk.CTkLabel(frame, text=f"{car['name']} | available: {car['count']}", font=("Arial", 16))
            label.pack(side="left", padx=10)


def logout():
    root.destroy()
    messagebox.showinfo("Exit", "You have successfully logged out.")


def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()


ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("950x650")
root.title("Car Reservation Dashboard")






topbar = ctk.CTkFrame(root, height=60, fg_color="#1a1a1a")
topbar.pack(fill="x", side="top")

ctk.CTkLabel(topbar, text="Car Reservation System", font=("Arial", 22, "bold"), text_color="#00FFFF").pack(side="left", padx=20)
ctk.CTkButton(topbar, text="Exit", fg_color="#FF4500", command=logout, width=80, height=35).pack(side="right", padx=20)

sidebar = ctk.CTkFrame(root, width=200, fg_color="#2b2b2b")
sidebar.pack(side="left", fill="y")

ctk.CTkButton(sidebar, text="Dashboard", command=show_dashboard, width=150, height=35).pack(pady=10)
ctk.CTkButton(sidebar, text="Reserve Basket", command=show_cart, width=150, height=35).pack(pady=10)

search_entry = ctk.CTkEntry(sidebar, placeholder_text="Car search", width=150)
search_entry.pack(pady=10)
ctk.CTkButton(sidebar, text="Search", command=search_car, width=150, height=35).pack(pady=10)


main_frame = ctk.CTkFrame(root, fg_color="#1f1f1f")
main_frame.pack(side="right", fill="both", expand=True)

show_dashboard()
root.mainloop()