import tkinter
from tkinter import messagebox, ttk
import mysql.connector
import logging
import re
from datetime import datetime
from tkcalendar import Calendar  # Importing the Calendar widget

# Define the connection variable in the global scope
connection = None
order_cart_window = None
cart_items = []


# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to handle sign-in button
def enter_app():
    user_id = userid_entry.get()
    password = password_entry.get()

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User_Account WHERE User_ID = %s AND Password = %s", (user_id, password))
        user_account = cursor.fetchone()

        if user_account:
            # Authentication successful, open order cart screen
            print("Authentication successful. Entering app.")
            clear_signin_entries()
            order_cart_screen()  # Open order cart screen
        else:
            print("Invalid credentials. Please try again.")
            logging.warning("Invalid sign-in attempt with user ID: %s", user_id)
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

    except mysql.connector.Error as error:
        print("Error occurred during sign-in:", error)
        logging.error("Error occurred during sign-in: %s", error)
        messagebox.showerror("Error", "Error occurred during sign-in. Please try again.")


# Function to clear sign-in entries
def clear_signin_entries():
    userid_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)


# Function to handle sign-up button
def userdetails():
    # Create a new window for sign-up
    signup_window = tkinter.Toplevel(window)
    signup_window.title("Sign Up")

    # Create a frame to organize widgets
    frame = tkinter.Frame(signup_window)
    frame.pack()

    # User info frame
    user_info_frame = tkinter.LabelFrame(frame, text="User Details")
    user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

    first_name_label = tkinter.Label(user_info_frame, text="First Name:")
    first_name_label.grid(row=0, column=0)

    first_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=0, column=1)

    last_name_label = tkinter.Label(user_info_frame, text="Last Name:")
    last_name_label.grid(row=1, column=0)

    last_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry.grid(row=1, column=1)

    email_label = tkinter.Label(user_info_frame, text="Email:")
    email_label.grid(row=2, column=0)

    email_entry = tkinter.Entry(user_info_frame)
    email_entry.grid(row=2, column=1)

    phone_label = tkinter.Label(user_info_frame, text="Phone:")
    phone_label.grid(row=3, column=0)

    phone_entry = tkinter.Entry(user_info_frame)
    phone_entry.grid(row=3, column=1)

    dob_label = tkinter.Label(user_info_frame, text="Date of Birth:")
    dob_label.grid(row=4, column=0)

    dob_entry = tkinter.Entry(user_info_frame)
    dob_entry.grid(row=4, column=1)

    # Function to set the selected date in the Date of Birth entry
    def set_date():
        dob_entry.delete(0, tkinter.END)
        dob_entry.insert(0, cal.get_date())

    # Calendar button for selecting DOB
    def show_calendar():
        def on_date_select():
            dob_entry.delete(0, tkinter.END)
            dob_entry.insert(0, cal.get_date())
            cal_window.destroy()

        cal_window = tkinter.Toplevel(signup_window)
        cal_window.title("Select Date of Birth")
        cal = Calendar(cal_window, selectmode="day", date_pattern="MM/DD/YYYY")
        cal.pack()
        select_button = tkinter.Button(cal_window, text="Select", command=on_date_select)
        select_button.pack()

    cal_button = tkinter.Button(user_info_frame, text="Calendar", command=show_calendar)
    cal_button.grid(row=4, column=2)

    user_id_label = tkinter.Label(user_info_frame, text="User ID:")
    user_id_label.grid(row=5, column=0)

    user_id_entry = tkinter.Entry(user_info_frame)
    user_id_entry.grid(row=5, column=1)

    password_label = tkinter.Label(user_info_frame, text="Password:")
    password_label.grid(row=6, column=0)

    password_entry = tkinter.Entry(user_info_frame, show="*")  # Passwords are shown as asterisks
    password_entry.grid(row=6, column=1)

    retype_password_label = tkinter.Label(user_info_frame, text="Retype Password:")
    retype_password_label.grid(row=7, column=0)

    retype_password_entry = tkinter.Entry(user_info_frame, show="*")
    retype_password_entry.grid(row=7, column=1)

    def validate_email(email):
        # Regular expression for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    # Function to add a new user to the database
    def add_user():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        dob = dob_entry.get()
        user_id = user_id_entry.get()
        password = password_entry.get()
        retype_password = retype_password_entry.get()

        # Validate email format
        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email format. Please enter a valid email.")
            return

        # Validate phone number length
        if len(phone) != 10:
            messagebox.showerror("Error", "Phone number should be 10 digits.")
            return

        # Validate date format
        try:
            dob_formatted = datetime.strptime(dob, "%m/%d/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use MM/DD/YYYY.")
            return

        # Validate age
        today = datetime.today()
        dob_datetime = datetime.strptime(dob, "%m/%d/%Y")
        age = today.year - dob_datetime.year - ((today.month, today.day) < (dob_datetime.month, dob_datetime.day))
        if age < 18:
            messagebox.showerror("Error", "You must be at least 18 years old to sign up.")
            return

        # Validate password match
        if password != retype_password:
            messagebox.showerror("Error", "Passwords do not match. Please retype password correctly.")
            return

        # Check if User ID is unique
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT User_ID FROM User_Account WHERE User_ID = %s", (user_id,))
            existing_user = cursor.fetchone()
            if existing_user:
                messagebox.showerror("Error", "User ID already exists. Please choose a different one.")
                return
        except mysql.connector.Error as error:
            print("Error occurred while checking user ID:", error)
            logging.error("Error occurred while checking user ID: %s", error)
            messagebox.showerror("Error", "Error occurred while checking user ID. Please try again.")
            return

        try:
            cursor.execute(
                "INSERT INTO Customer (First_Name, Last_Name, Email_ID, Phone_No, Date_of_Birth, User_Acc_ID) VALUES (%s, %s, %s, %s, %s, %s)",
                (first_name, last_name, email, phone, dob_formatted, None))
            connection.commit()
            cursor.execute("INSERT INTO User_Account (User_ID, Password) VALUES (%s, %s)", (user_id, password))
            connection.commit()
            print("User added successfully.")
            logging.info("New user added to the database.")
            messagebox.showinfo("Success", "User added successfully.")
            signup_window.destroy()  # Close the sign-up window after successful registration
        except mysql.connector.Error as error:
            print("Error occurred while adding user:", error)
            logging.error("Error occurred while adding user: %s", error)
            messagebox.showerror("Error", "Error occurred while adding user. Please try again.")

    # Sign-up button
    btnSignUp = tkinter.Button(frame, width=10, text="Sign Up", command=add_user)
    btnSignUp.grid(row=1, column=0, padx=20, pady=10)

    # Cancel button
    btnCancel = tkinter.Button(frame, width=10, text="Cancel", command=signup_window.destroy)
    btnCancel.grid(row=1, column=1, padx=20, pady=10)


# Function to create the order cart screen
def order_cart_screen():
    global order_cart_window
    order_cart_window = tkinter.Toplevel(window)
    order_cart_window.title("Order Cart")

    # Create a frame to organize widgets
    frame = tkinter.Frame(order_cart_window)
    frame.pack()

    # Add widgets for the order cart screen
    # Label for the title
    title_label = tkinter.Label(frame, text="Order Cart", font=("Helvetica", 16))
    title_label.pack(pady=10)

    # Fetch products from the database
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT Product_ID, Description, Price FROM Product")
        products = cursor.fetchall()
        connection.commit()

        # Display products in a list format
        for product in products:
            product_label = tkinter.Label(frame, text=f"{product[1]} - ${product[2]}")
            product_label.pack()

            quantity_label = tkinter.Label(frame, text="Quantity:")
            quantity_label.pack()

            # Combobox for selecting quantity
            quantity_combobox = ttk.Combobox(frame, values=[i for i in range(1, 6)], state="readonly")
            quantity_combobox.pack()

            # Button to add the product to cart
            add_to_cart_button = tkinter.Button(frame, text="Add to Cart",
                                                 command=lambda p_id=product[0], desc=product[1],
                                                                price=product[2], qty=quantity_combobox: add_to_cart(
                                                     p_id, desc, price, qty))
            add_to_cart_button.pack()

    except mysql.connector.Error as error:
        print("Error occurred while fetching products:", error)
        logging.error("Error occurred while fetching products: %s", error)
        messagebox.showerror("Error", "Error occurred while fetching products. Please try again.")

    # Button to view cart
    view_cart_button = tkinter.Button(frame, text="View Cart", command=view_cart)
    view_cart_button.pack(pady=10)


# Function to add a product to the cart
def add_to_cart(product_id, description, price, quantity):
    global cart_items
    cart_items.append((product_id, description, price, quantity))
    messagebox.showinfo("Success", "Product added to cart.")


# Function to view the cart
def view_cart():
    global cart_items
    if not cart_items:
        messagebox.showinfo("Info", "Your cart is empty.")
    else:
        cart_window = tkinter.Toplevel(order_cart_window)
        cart_window.title("View Cart")

        # Create a frame to organize widgets
        frame = tkinter.Frame(cart_window)
        frame.pack()

        # Add widgets to display cart items
        title_label = tkinter.Label(frame, text="Cart Items", font=("Helvetica", 16))
        title_label.pack(pady=10)

        total_price = 0
        for item in cart_items:
            product_id, description, price, quantity = item
            total_price += price * quantity
            item_label = tkinter.Label(frame, text=f"{description} - ${price} x {quantity}")
            item_label.pack()

        total_label = tkinter.Label(frame, text=f"Total: ${total_price}")
        total_label.pack(pady=10)


# Function to place an order
def place_order():
    # Implement the logic to place an order here
    # You can fetch the selected products from the UI and save the order details to the database
    messagebox.showinfo("Success", "Order placed successfully!")
    # Clear cart items after placing the order
    cart_items.clear()
    # Close the order cart window after placing the order
    order_cart_window.destroy()


try:
    # Replace '141.209.241.81', 'bis698_S24_w200', 'grp2w200', and 'passinit' with your actual database details
    connection = mysql.connector.connect(
        host='141.209.241.81',  # Or your database server IP
        database='bis698_S24_w200',
        user='grp2w200',
        password='passinit'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("SELECT database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except mysql.connector.Error as error:
    print("Failed to connect to MySQL:", error)
    logging.error("Failed to connect to MySQL: %s", error)
    messagebox.showerror("Error", "Failed to connect to MySQL. Please try again.")

# Create the main window
window = tkinter.Tk()
window.title("Indian Grocery Hub Login Page")

# Create a frame to organize widgets
frame = tkinter.Frame(window)
frame.pack()

# User info frame
user_info_frame = tkinter.LabelFrame(frame, text="User Credentials")
user_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

userid_label = tkinter.Label(user_info_frame, text="User ID:")
userid_label.grid(row=0, column=0)

userid_entry = tkinter.Entry(user_info_frame)
userid_entry.grid(row=0, column=1)

password_label = tkinter.Label(user_info_frame, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tkinter.Entry(user_info_frame, show="*")  # Passwords are shown as asterisks
password_entry.grid(row=1, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Buttons frame
buttons_frame = tkinter.LabelFrame(frame, text="Buttons")
buttons_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

btnSignIn = tkinter.Button(buttons_frame, width=10, text="Sign-In", command=enter_app)
btnSignIn.grid(row=3, column=0)

btnSignUp = tkinter.Button(buttons_frame, width=10, text="Sign-Up", command=userdetails)
btnSignUp.grid(row=3, column=1)

btnExit = tkinter.Button(buttons_frame, width=10, text="Exit", command=window.destroy)
btnExit.grid(row=3, column=2)

for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Start the main event loop
window.mainloop()
