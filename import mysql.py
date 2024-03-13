import tkinter
import subprocess
import mysql.connector

# Function to handle sign-in button
def enter_app():
    print("Entering app")

# Function to handle sign-up button
def userdetails():
    subprocess.Popen(["python", "UserInformation.py"])
    window.withdraw()  # Hide the current window when opening a new one

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
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except mysql.connector.Error as error:
    print("Failed to connect to MySQL: {}".format(error))

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
