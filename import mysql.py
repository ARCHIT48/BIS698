import tkinter
from tkinter import messagebox
import mysql.connector
import logging
import re
from tkcalendar import Calendar

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
            # Authentication successful, proceed with application
            print("Authentication successful. Entering app.")
            # Implement your application logic here
            
        else:
            print("Invalid credentials. Please try again.")
            logging.warning("Invalid sign-in attempt with user ID: %s", user_id)
            messagebox.showerror("Error", "Invalid credentials. Please try again.")
    
    except mysql.connector.Error as error:
        print("Error occurred during sign-in:", error)
        logging.error("Error occurred during sign-in: %s", error)
        messagebox.showerror("Error", "Error occurred during sign-in. Please try again.")

# Function to validate email format
def validate_email(email):
    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

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

    # Calendar button for selecting DOB
    def select_date():
        cal = Calendar(signup_window, selectmode="day", year=2024, month=3, day=13)
        cal.pack()

        def set_date():
            dob_entry.delete(0, tkinter.END)
            dob_entry.insert(0, cal.get_date())
            cal.pack_forget()

        select_button = tkinter.Button(signup_window, text="Select", command=set_date)
        select_button.pack()

    dob_calendar_button = tkinter.Button(user_info_frame, text="Calendar", command=select_date)
    dob_calendar_button.grid(row=4, column=2)

    # Sign-up button
    btnSignUp = tkinter.Button(frame, width=10, text="Sign Up", command=lambda: add_user(first_name_entry.get(), last_name_entry.get(), email_entry.get(), phone_entry.get(), dob_entry.get()))
    btnSignUp.grid(row=1, column=0, padx=20, pady=10)

    # Cancel button
    btnCancel = tkinter.Button(frame, width=10, text="Cancel", command=signup_window.destroy)
    btnCancel.grid(row=1, column=1, padx=20, pady=10)

# Function to add a new user to the database
def add_user(first_name, last_name, email, phone, dob):
    # Validate email format
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format. Please enter a valid email.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Customer (First_Name, Last_Name, Email_ID, Phone_No, Date_of_Birth, User_Acc_ID) VALUES (%s, %s, %s, %s, %s, %s)", (first_name, last_name, email, phone, dob, None))
        connection.commit()
        print("User added successfully.")
        logging.info("New user added to the database.")
        messagebox.showinfo("Success", "User added successfully.")
    except mysql.connector.Error as error:
        print("Error occurred while adding user:", error)
        logging.error("Error occurred while adding user: %s", error)
        messagebox.showerror("Error", "Error occurred while adding user. Please try again.")

try:
    # Replace '141.209.241.81', 'bis698_S24_w200', 'grp2w200', and 'passinit' with your actual database details
    connection = mysql.connector.connect(
        host='141.209.241.81',       # Or your database server IP
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

password_entry = tkinter.Entry(user_info_frame)
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
