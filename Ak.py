import tkinter as tk
from tkinter import messagebox

# Global Variables
cart = []
total_amount = 0
product_images = {}

# Tkinter Window
root = tk.Tk()
root.title("FreshKart")
root.geometry("800x600")
root.configure(bg="white")

# Load and resize images once
def load_images():
    paths = {
        "Onion": r"C:\Users\admin\Downloads\onion.png",
        "Tomato": r"C:\Users\admin\Downloads\tomato.png",
        "Potato": r"C:\Users\admin\Downloads\patoto.png",
        "Apple": r"C:\Users\admin\Downloads\Apple.png",
        "Banana": r"C:\Users\admin\Downloads\banana.png",
        "Mango": r"C:\Users\admin\Downloads\mango.png"
    }
    for name, path in paths.items():
        try:
            img = tk.PhotoImage(file=path).subsample(6, 6)
            product_images[name] = img
        except Exception as e:
            print(f"Error loading {name}: {e}")

# Clear screen widgets
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Login Page
def login_page():
    clear_window()
    tk.Label(root, text="Username:", bg="white", fg="black", font=("Helvetica", 12)).place(x=200, y=200)
    username_entry = tk.Entry(root, width=30, bg="white", fg="black", bd=2, relief="solid")
    username_entry.place(x=320, y=200)

    tk.Label(root, text="Phone Number:", bg="white", fg="black", font=("Helvetica", 12)).place(x=200, y=250)
    phone_entry = tk.Entry(root, width=30, bg="white", fg="black", bd=2, relief="solid")
    phone_entry.place(x=320, y=250)

    tk.Button(root, text="Continue", bg="green", fg="white", command=welcome_page).place(x=370, y=300)

# Welcome Page
def welcome_page():
    clear_window()
    emoji_bg = "🍎🍌🥭🍅🥔🥕🥬🍇🍉🍊🥤" * 5
    tk.Label(root, text=emoji_bg, font=("Helvetica", 18), bg="white", wraplength=800).pack(pady=10)

    tk.Label(root, text="Let's shop!", font=("Helvetica", 28), bg="white", fg="black").pack(pady=30)
    tk.Label(root, text="FreshKart", font=("Helvetica", 20, "bold"), bg="white", fg="black").pack()

    tk.Button(root, text="Enter Store", bg="green", fg="white", command=home_page).pack(pady=20)

# Profile Popup
def profile_page():
    top = tk.Toplevel(bg="white")
    top.title("Profile Information")
    top.geometry("400x400")

    labels = ["Country", "State", "Pin Code", "Address", "Landmark"]
    for i, text in enumerate(labels):
        tk.Label(top, text=f"{text}:", font=("Helvetica", 12), bg="white", fg="black").place(x=20, y=30 + i*50)
        e = tk.Entry(top, width=30)
        e.place(x=150, y=30 + i*50)

    tk.Button(top, text="Save", bg="green", fg="white", command=top.destroy).place(x=160, y=300)

# Add to cart function
def add_to_cart(name, price):
    global total_amount
    cart.append((name, price))
    total_amount += price
    messagebox.showinfo("Cart", f"{name} added to cart!")

# Home Page with grid layout
def home_page():
    clear_window()
    header = tk.Frame(root, bg="white")
    header.pack(fill=tk.X, pady=10)

    tk.Label(header, text="FreshKart", font=("Helvetica", 24, "bold"), bg="white", fg="green").pack(side=tk.LEFT, padx=20)
    tk.Button(header, text="Profile", command=profile_page, bg="gray", fg="white").pack(side=tk.RIGHT, padx=20)

    content = tk.Frame(root, bg="white")
    content.pack(pady=10)

    tk.Label(content, text="Products", font=("Helvetica", 18, "bold"), bg="white").grid(row=0, column=0, columnspan=3, pady=10)

    products = [
        ("Onion", 20),
        ("Tomato", 15),
        ("Potato", 10),
        ("Apple", 30),
        ("Banana", 25),
        ("Mango", 50),
    ]

    for idx, (name, price) in enumerate(products):
        row = idx // 3 + 1
        col = idx % 3

        frame = tk.Frame(content, bg="white", padx=10, pady=10, bd=1, relief="solid")
        frame.grid(row=row, column=col, padx=10, pady=10)

        img = product_images.get(name)
        if img:
            tk.Label(frame, image=img, bg="white").pack()
        tk.Label(frame, text=f"{name} - ₹{price}", bg="white", font=("Helvetica", 12)).pack()
        tk.Button(frame, text="Add to Cart", bg="green", fg="white", command=lambda n=name, p=price: add_to_cart(n, p)).pack(pady=5)

    tk.Button(root, text="Checkout", bg="orange", fg="white", command=cart_page).pack(pady=20)

# Cart page
def cart_page():
    clear_window()
    tk.Label(root, text="Your Cart", font=("Helvetica", 20, "bold"), bg="white", fg="black").pack(pady=20)

    y = 100
    for item, price in cart:
        tk.Label(root, text=f"{item} - ₹{price}", font=("Helvetica", 12), bg="white").place(x=100, y=y)
        y += 30

    tk.Label(root, text=f"Total Amount: ₹{total_amount}", font=("Helvetica", 14, "bold"), bg="white", fg="black").place(x=100, y=y + 30)

    tk.Button(root, text="Place Order", bg="green", fg="white", command=confirm_order).place(x=100, y=y + 80)

# Order confirmation
def confirm_order():
    messagebox.showinfo("Order", "Your Order is confirmed!")
    final_page()

# Final page with green circle and white text
def final_page():
    clear_window()
    canvas = tk.Canvas(root, width=800, height=600, bg="white", highlightthickness=0)
    canvas.pack()
    canvas.create_oval(250, 200, 550, 500, fill="green", outline="green")
    canvas.create_text(400, 350, text="Order Successfully Placed!", fill="white", font=("Helvetica", 16, "bold"))

# Start App
load_images()
login_page()
root.mainloop()
