import tkinter as tk
import traceback
from tkinter import *
import tkinter as ttk
from tkinter import Label, Entry, Button, LabelFrame, RIDGE, GROOVE
import random, os, tempfile, smtplib
import sys
from pymongo import MongoClient
from fpdf import FPDF
from tkinter import filedialog, messagebox, END
import os
import smtplib
import tempfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter.scrolledtext import ScrolledText
from fpdf import FPDF
from pymongo import MongoClient
from PIL import Image, ImageTk
import re
import sys
from tkcalendar import Calendar
from tkinter import Label, StringVar, OptionMenu, font
import os
import random
import smtplib
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
import ssl
from dotenv import load_dotenv
from tkinter.ttk import Combobox
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from pathlib import Path

import os





def perfect_center(window, width, height):
    """Mathematically perfect centering using screen dimensions"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coord = (screen_width - width) // 2
    y_coord = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x_coord}+{y_coord}")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    path = os.path.join(base_path, relative_path)
    if not os.path.exists(path):
        # Try one level up
        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, relative_path)

    return path


# Create and configure the main window
root = tk.Tk()
root.title("Pizzeria - signUp")
root.config(background="white")

# Set window dimensions
window_width = 650
window_height = 600

# Position window perfectly centered before it appears
root.withdraw()  # Hide window during setup
perfect_center(root, window_width, height=window_height)

# Load icon
try:
    icon_path = resource_path("favicon.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)  # Primary method for Windows
        try:
            img = Image.open(icon_path)
            photo = ImageTk.PhotoImage(img)
            root.iconphoto(False, photo)  # Fallback method
        except:
            pass
except Exception as e:
    print(f"Icon error: {e}")

# Create main frame without packing
master = ttk.Frame(root, width=window_width, height=window_height)
master.place(x=0, y=0)  # Using place instead of pack

# Create entry widget
inputs = ttk.Entry(master)
inputs.place(relx=0.5, rely=0.5, anchor="center")  # Centered in frame

# Show the window now that everything is ready


perfect_center(root, window_width, window_height)

master = ttk.Frame(root, width=window_width, height=window_height, background="black")
inputs = ttk.Entry(master)

root.deiconify()


class Data:
    def __init__(self, master, inputs):
        self.master = master
        self.inputs = inputs
        self.fName = ""
        self.lName = ""
        self.gender = ""
        self.age = ""
        self.gmail = ""
        self.forotp = ""
        self.state = ""
        self.mobile = ""
        self.username = ""
        self.password = ""
        self.confirmP = ""

    def abc(self):
        pass


class InputsLabel(Data):
    def __init__(self, master):
        super().__init__(master, self)
        self.username = ""

    def get_username(self):
        gmail_address = self.gmailinp.get().lower()
        if "@" in gmail_address:
            username = gmail_address.split("@")[0]
            return username
        return ""

    def __init__(self, master):
        super().__init__(master, self)
        self.v = IntVar()
        # self.v.set(0)
        label_font = ("calibri", 14)
        label_font2 = ("calibri", 14)

        self.finame = Label(master, text="First Name", height=1, borderwidth=9, font=label_font)
        self.finame.grid(row=1, column=1, padx=23, pady=6)

        self.fnameinp = Entry(master, borderwidth=1, validate="key",
                              validatecommand=(master.register(self.validate_name_input), "%P"), relief="solid",
                              width=20, font=label_font2)
        self.fnameinp.grid(row=1, column=2, padx=32, pady=6)

        self.laname = Label(master, text="Last Name", height=1, borderwidth=9, font=label_font)
        self.laname.grid(row=2, column=1)

        self.lanameinp = Entry(master, borderwidth=1, validate="key",
                               validatecommand=(master.register(self.validate_name_input), "%P"), relief="solid",
                               width=20, font=label_font2)
        self.lanameinp.grid(row=2, column=2)

        self.gender_label = Label(master, text="Gender", height=1, borderwidth=9, font=label_font)
        self.gender_label.grid(row=3, column=1, padx=0, pady=6)

        self.gender_frame = Frame(master, relief="solid", borderwidth=1)
        self.gender_frame.grid(row=3, column=2, columnspan=3, padx=38, pady=6, sticky="ew")

        self.male_radio = Radiobutton(self.gender_frame, text="Male", padx=10, pady=6, borderwidth=1, fg="orange",
                                      variable=self.v, value=1, font=label_font, width=5)
        self.male_radio.grid(row=3, column=0, padx=5, pady=6)

        self.female_radio = Radiobutton(self.gender_frame, text="Female", padx=10, pady=6, borderwidth=1, fg="green",
                                        variable=self.v, value=2, font=label_font2, width=5)
        self.female_radio.grid(row=3, column=1, padx=5, pady=6)

        self.other_radio = Radiobutton(self.gender_frame, text="Other", padx=10, pady=6, borderwidth=1, fg="blue",
                                       variable=self.v, value=3, font=label_font2, width=5)
        self.other_radio.grid(row=3, column=2, padx=5, pady=6)

        self.age = Label(master, text="Age", height=1, borderwidth=9, font=label_font)
        self.age.grid(row=4, column=1, padx=23, pady=6)

        self.ageinp = Spinbox(master, from_=0, to=80, relief="solid", width=19, font=label_font2)
        self.ageinp.grid(row=4, column=2, padx=30, pady=6)

        self.gmail = Label(master, text="Gmail", height=1, borderwidth=9, font=label_font)
        self.gmail.grid(row=5, column=1, padx=23, pady=6)

        self.gmailinp = Entry(master, borderwidth=1, width=20, font=label_font2, relief="solid")
        self.gmailinp.grid(row=5, column=2)

        self.phone = Label(master, text="Phone No.", height=1, borderwidth=9, font=label_font)
        self.phone.grid(row=8, column=1, padx=23, pady=6)

        self.phoneinp = Entry(master, borderwidth=1, width=20, font=label_font2, relief="solid", validate="key",
                              validatecommand=(master.register(self.validate_phone), "%P"))
        self.phoneinp.grid(row=8, column=2)

        self.password = Label(master, text="Password", height=1, borderwidth=3, font=label_font)
        self.password.grid(row=9, column=1, padx=23, pady=6)

        self.passwordinp = Entry(master, borderwidth=1, relief="solid", show="\u2022", width=20, font=label_font2)
        self.passwordinp.grid(row=9, column=2)

        self.confirmP = Label(master, text="Confirm Password", height=1, borderwidth=9, font=label_font)
        self.confirmP.grid(row=10, column=1, padx=23, pady=6)

        self.confirmPinp = Entry(master, borderwidth=1, relief="solid", show="\u2022", width=20, font=label_font2)
        self.confirmPinp.grid(row=10, column=2)

        self.error_message = Label(master, text="", fg="red", bg="white", font=("calibri", 12))
        self.error_message.grid(row=11, column=2, columnspan=1)

        from PIL import Image
        self.eye_show_image = Image.open(resource_path("show.png"))
        self.eye_hide_image = Image.open(resource_path("hide.png"))
        # self.eye_show_image = Image.open(resource_path("show.png"))  # Open the closed eye image
        # self.eye_hide_image = Image.open(resource_path("hide.png"))  # Open the open eye image

        # Resize images to appropriate size (e.g., 24x24 pixels)
        self.eye_show_image = self.eye_show_image.resize((24, 24))
        self.eye_hide_image = self.eye_hide_image.resize((24, 24))

        # Convert images to Tkinter-compatible format
        self.eye_show_image = ImageTk.PhotoImage(self.eye_show_image)
        self.eye_hide_image = ImageTk.PhotoImage(self.eye_hide_image)

        # Password visibility toggle button with eye icon
        self.show_password_button = tk.Button(master, image=self.eye_show_image, command=self.toggle_password, bd=0,
                                              font=("calibri", 14))
        self.show_password_button.grid(row=9, column=3, padx=10, pady=10)

        # Confirm password visibility toggle button with eye icon
        self.show_confirm_password_button = tk.Button(master, image=self.eye_show_image,
                                                      command=self.toggle_confirm_password, bd=0, font=("calibri", 14))
        self.show_confirm_password_button.grid(row=10, column=3, padx=10, pady=10)

    def check_mail(self, mail):
        if not mail.endswith("@gmail.com"):
            messagebox.showwarning("Invalid Gmail", "Please enter a valid gmail address (e.g ., xyz@gmail.com)")
            return False
        return True

    def toggle_password(self):
        # Toggle the password visibility
        if self.passwordinp.cget("show") == "":
            self.passwordinp.config(show="\u2022")  # Hide password
            self.show_password_button.config(image=self.eye_show_image)  # Show closed eye
        else:
            self.passwordinp.config(show="")  # Show password
            self.show_password_button.config(image=self.eye_hide_image)  # Show open eye

    def toggle_confirm_password(self):
        # Toggle the confirm password visibility
        if self.confirmPinp.cget("show") == '':
            self.confirmPinp.config(show="\u2022")  # Hide confirm password
            self.show_confirm_password_button.config(image=self.eye_show_image)  # Show closed eye
        else:
            self.confirmPinp.config(show="")  # Show confirm password
            self.show_confirm_password_button.config(image=self.eye_hide_image)

    def toggle_password(self):
        # Toggle the password visibility
        if self.passwordinp.cget("show") == "":
            self.passwordinp.config(show="\u2022")  # Hide password
            self.show_password_button.config(image=self.eye_show_image)  # Show closed eye
        else:
            self.passwordinp.config(show="")  # Show password
            self.show_password_button.config(image=self.eye_hide_image)  # Show open eye

    def toggle_confirm_password(self):
        # Toggle the confirm password visibility
        if self.confirmPinp.cget("show") == "":
            self.confirmPinp.config(show="\u2022")  # Hide confirm password
            self.show_confirm_password_button.config(image=self.eye_show_image)  # Show closed eye
        else:
            self.confirmPinp.config(show="")  # Show confirm password
            self.show_confirm_password_button.config(image=self.eye_hide_image)  # Sho

    def toggle_password(self):
        # Toggle the password visibility
        if self.passwordinp.cget("show") == "":
            self.passwordinp.config(show="\u2022")  # Hide password
            self.show_password_button.config(image=self.eye_show_image)  # Show closed eye
        else:
            self.passwordinp.config(show="")  # Show password
            self.show_password_button.config(image=self.eye_hide_image)  # Show open eye

    def toggle_confirm_password(self):
        # Toggle the confirm password visibility
        if self.confirmPinp.cget("show") == "":
            self.confirmPinp.config(show="\u2022")  # Hide confirm password
            self.show_confirm_password_button.config(image=self.eye_show_image)  # Show closed eye
        else:
            self.confirmPinp.config(show="")  # Show confirm password
            self.show_confirm_password_button.config(image=self.eye_hide_image)

    def validate_otp(self, otp, length=6):
        if otp.isdigit() and len(otp) <= length:
            return True
        elif otp == "":
            return True
        else:
            messagebox.showerror("Invalid OTP", "OTP must be numeric and up to 6 digits")
            return False

    def validate_phone(self, phone, length=10):
        if phone.isdigit() and len(phone) <= length:
            return True
        elif phone == "":
            return True
        else:
            messagebox.showerror("Invalid OTP", "Phone number must be numeric and up to 10 digits")
            return False

    def get_first_name(self):
        return self.fnameinp.get()

    def get_last_name(self):
        return self.lanameinp.get()

    def get_gender(self):
        gender_value = self.v.get()
        if gender_value == 1:
            return "Male"
        elif gender_value == 2:
            return "Female"
        elif gender_value == 3:
            return "Other"
        else:
            return "Not Selected"

    def get_age(self):
        return self.ageinp.get()

    def get_mobile(self):
        return self.phoneinp.get()

    def get_gmail(self):
        return self.gmailinp.get().lower()

    def get_password(self):
        return self.passwordinp.get()

    def get_confirm_password(self):
        return self.confirmPinp.get()

    def info2(self):
        self.error_message.config(text="", height=0)

        if not self.get_first_name():
            self.error_message.config(text="First Name is required")
            return False

        if not self.get_last_name():
            self.error_message.config(text="Last Name is required")
            return False

        if self.v.get() == 0:
            self.error_message.config(text="Gender is required")
            return False

        if not self.get_age():
            self.error_message.config(text="Age is required")
            return False

        if not self.get_gmail():
            self.error_message.config(text="Gmail is required")
            return False

        if not self.get_mobile():
            self.error_message.config(text="Phone Number is required")
            return False

        if not self.get_password():
            self.error_message.config(text="Password is required")
            return False

        if not self.get_confirm_password():
            self.error_message.config(text="Confirm Password is required")
            return False

        password_error = self.validate_password_strength(self.get_password())
        if password_error:
            self.error_message.config(text=password_error)
            return False

        if self.get_password() != self.get_confirm_password():
            self.error_message.config(text="Passwords do not match")
            return False

        self.error_message.config(text="")
        return True

    def validate_password_strength(self, password):
        if len(password) < 8:
            return "Password must be at least 8 characters long"
        if not re.search("[0-9]", password):
            return "Password must contain at least one digit"
        if not re.search("[!@#$%^&]", password):
            return "Password must contain at least one symbol "
        if not re.search("[a-z]", password):
            return "Password must contain at least one letter"
        return None

    def validate_name_input(self, name):
        if name.isalpha() or name == "":
            return True
        else:
            return False


class Buttons(Data):
    def __init__(self, master):
        super().__init__(master, InputsLabel(master))
        self.generated_otp = ""
        self.gmail = None
        self.btn1 = tk.Button(master, text="Continue", command=self.on_click, relief="flat", bg="skyblue",
                              font=("calibri", 13))
        self.btn1.grid(row=12, column=2)

        self.btn2 = tk.Button(master, text="login", command=self.open_login_page_window, relief="flat", bg="yellow",
                              width=8,
                              font=("calibri", 13))
        self.btn2.grid(row=12, column=3)
        # open_login_page_window add after

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        window.geometry(f"{width}x{height}+{position_right}+{position_top}")

    def send_verification_success_email(self, email):
        try:
            # Sending verification success email
            ob = smtplib.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login("adityabhoir291@gmail.com", "sheohmubyfsmoomg")  # Use your correct login credentials here

            msg = MIMEMultipart()
            msg["From"] = "adityabhoir291@gmail.com"
            msg["To"] = email
            msg["Subject"] = "Registration Successful"

            html_body = f"""
                              <html>
                              <head>
                                  <style>
                                      body {{
                                          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                                          background-color: #f9f9f9;
                                          margin: 0;
                                          padding: 0;
                                          color: #555;
                                      }}
                                      .container {{
                                          width: 100%;
                                          max-width: 600px;
                                          margin: 0 auto;
                                          background-color: #ffffff;
                                          padding: 20px;
                                          border-radius: 8px;
                                          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                                      }}
                                      h1 {{
                                          color: #4CAF50;
                                          font-size: 24px;
                                          margin-bottom: 20px;
                                      }}
                                      p {{
                                          font-size: 16px;
                                          line-height: 1.6;
                                      }}
                                      .greeting {{
                                          font-size: 18px;
                                          color: #333;
                                          margin-bottom: 15px;
                                      }}
                                      .info {{
                                          background-color: #f4f4f9;
                                          border-left: 4px solid #4CAF50;
                                          padding: 15px;
                                          margin: 20px 0;
                                          border-radius: 6px;
                                      }}
                                      .info ul {{
                                          padding-left: 20px;
                                          font-size: 16px;
                                      }}
                                      .info li {{
                                          margin-bottom: 10px;
                                      }}
                                      .footer {{
                                          text-align: center;
                                          margin-top: 40px;
                                          font-size: 14px;
                                          color: #888;
                                      }}
                                      .footer a {{
                                          color: #4CAF50;
                                          text-decoration: none;
                                      }}
                                      .button {{
                                          background-color: #4CAF50;
                                          color: white;
                                          padding: 10px 20px;
                                          font-size: 16px;
                                          border-radius: 4px;
                                          text-align: center;
                                          text-decoration: none;
                                          display: inline-block;
                                          margin-top: 20px;
                                      }}
                                      .button:hover {{
                                          background-color: #45a049;
                                      }}
                                  </style>
                              </head>
                              <body>
                                  <div class="container">
                                      <h1>Registration Successful</h1>
                                      <p class="greeting"><strong>Dear {self.fName} {self.lName},</strong></p>
                                      <p>Congratulations! Your registration was successful. Below are your details:</p>

                                      <div class="info">
                                          <ul>
                                              <li><strong>Username:</strong> {self.username}</li>
                                              <li><strong>Password:</strong> {self.password}</li>
                                          </ul>
                                      </div>
                                      <div class="footer">
                                          <p>Thank you for registering with us!</p>
                                      </div>
                                  </div>
                              </body>
                              </html>
                              """

            msg.attach(MIMEText(html_body, "html"))

            ob.sendmail(msg["From"], msg["To"], msg.as_string())
            ob.quit()
            messagebox.showinfo("Success",
                                f"OTP verified successfully! Username and password has been sent to {self.gmail}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to send confirmation email. Please try again.\nError: {e}")

    def open_verification_window(self):
        def resource_path(relative_path):
            """Get absolute path to resource, works for development and PyInstaller."""
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            return os.path.join(base_path, relative_path)

        # Hide the main window
        self.master.withdraw()

        # Create a new Toplevel window for verification
        verification_window = tk.Toplevel(self.master)
        verification_window.title("Verification Window")

        # Set the window icon
        try:
            icon_path = resource_path("favicon.ico")  # Resolve the icon path
            verification_window.wm_iconbitmap(icon_path)
        except tk.TclError as e:
            print(f"Error loading icon: {e}")  # Handle icon load errors gracefully
        window_width, window_height = 500, 600
        self.center_window(verification_window, window_width, window_height)

        def enable_email_edit():
            verification_window.destroy()
            self.master.deiconify()

        def verify_otp():
            entered_otp = otp_entry.get()
            if entered_otp == self.generated_otp:
                self.send_verification_success_email(self.gmail)
                verification_window.destroy()
                self.open_login_page_window()
            else:
                messagebox.showerror("Invalid OTP", "The OTP you entered is incorrect.")

        def get_otp():
            email = self.gmail
            try:
                # Generate OTP - using self.generated_otp instead of global generated_otp
                self.generated_otp = ''.join(random.choices("0123456789", k=6))
                print(f"Generated OTP (for debugging): {self.generated_otp}")

                current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                # MongoDB Connection
                client = MongoClient("mongodb+srv://adityabhoir983_db_user:TUViJnRnUnaO3qFS@cluster0.txhrbfx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
                db = client["user_data"]
                collection = db["users"]

                user_data = {
                    "Date and Time": current_datetime,
                    "First Name": self.fName,
                    "Last Name": self.lName,
                    "Gender": self.gender,
                    "Age": self.age,
                    "Gmail": self.gmail,
                    "Generated OTP": self.generated_otp,
                    "Mobile Number": self.mobile,
                    "Username": self.username,
                    "Password": self.password,
                    "Confirm Password": self.confirmP,
                    "Status": "Inactive"  # Default status is Inactive
                }

                # Insert user data
                collection.insert_one(user_data)

                # Email configuration
                sender_email = "adityabhoir291@gmail.com"
                sender_password = "sheohmubyfsmoomg"

                # Create message container
                msg = MIMEMultipart('alternative')
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = "Confirm your email to complete registration"

                # Create HTML email content
                html_body = f"""
                <html>
                <head>
                    <style>
                        body {{
                            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                            background-color: #f9f9f9;
                            margin: 0;
                            padding: 0;
                            color: #555;
                        }}
                        .container {{
                            width: 100%;
                            max-width: 600px;
                            margin: 0 auto;
                            background-color: #ffffff;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        }}
                        h1 {{
                            font-size: 26px;
                            color: #4CAF50;
                            text-align: center;
                            margin-bottom: 20px;
                        }}
                        .greeting {{
                            font-size: 18px;
                            color: #333;
                            margin-bottom: 15px;
                            text-align: center;
                        }}
                        .otp {{
                            background-color: #f4f4f9;
                            border-left: 4px solid #4CAF50;
                            padding: 15px;
                            font-size: 32px;
                            font-weight: bold;
                            text-align: center;
                            border-radius: 6px;
                            margin: 20px 0;
                        }}
                        p {{
                            font-size: 16px;
                            line-height: 1.6;
                            color: #555;
                            text-align: center;
                        }}
                        .footer {{
                            text-align: center;
                            margin-top: 40px;
                            font-size: 14px;
                            color: #888;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Email Verification</h1>
                        <p class="greeting"><strong>Hello {self.fName},</strong></p>
                        <p>Please verify your email address with the following code:</p>
                        <div class="otp">
                            <strong>{self.generated_otp}</strong>
                        </div>
                        <p>Enter this code in the verification page to complete the process.</p>
                        <div class="footer">
                        </div>
                    </div>
                </body>
                </html>
                """

                # Attach HTML content
                msg.attach(MIMEText(html_body, 'html'))

                # Send email using SMTP_SSL
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login(sender_email, sender_password)
                    server.send_message(msg)

                messagebox.showinfo("Success", "OTP sent successfully to your email!")

            except smtplib.SMTPAuthenticationError:
                messagebox.showerror("Error",
                                     "Failed to authenticate with email server.\n"
                                     "Please check your email credentials and ensure you're using an App Password.")
            except smtplib.SMTPRecipientsRefused:
                messagebox.showerror("Error", "The recipient email address was refused.")
            except smtplib.SMTPServerDisconnected:
                messagebox.showerror("Error", "The server unexpectedly disconnected.")
            except smtplib.SMTPException as e:
                messagebox.showerror("Error", f"Email sending failed: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

        def on_hover(event):
            welcome_label.config(fg="#0066cc")

        def on_leave(event):
            welcome_label.config(fg="#333333")

        # Header with the title "OTP Verification"
        header_frame = tk.Frame(verification_window)
        header_frame.grid(row=0, column=0, pady=50)

        welcome_label = tk.Label(
            header_frame,
            text="OTP Verification",
            font=("Helvetica Neue", 32, "bold"),
            fg="#333333",
            pady=10, padx=65
        )
        welcome_label.bind("<Enter>", on_hover)
        welcome_label.bind("<Leave>", on_leave)
        welcome_label.grid(row=0, column=0, padx=10)

        # OTP Entry Frame
        otp_frame = tk.Frame(verification_window)
        otp_frame.grid(row=1, column=0, pady=50)

        email_label = tk.Label(otp_frame, text="Email", font=("Arial", 12))
        email_label.grid(row=0, column=0, pady=2, sticky="w")

        email_entry = tk.Entry(otp_frame, font=("Arial", 14), width=30)
        email_entry.insert(0, self.gmail)
        email_entry.config(state="readonly")
        email_entry.grid(row=1, column=0, pady=2, columnspan=2)

        edit_email_button = tk.Button(
            otp_frame, text="Edit", command=enable_email_edit,
            font=("Arial", 10, "bold"), fg="green", bd=0, cursor="hand2",
            activeforeground="#078C6E"
        )
        edit_email_button.grid(row=1, column=1, padx=(200, 0), sticky="w")

        # Get OTP Button
        get_otp_button = tk.Button(
            otp_frame, text="Get OTP", command=get_otp,
            font=("calibri", 14), width=32, pady=8, bg="lightblue",
            fg="white", relief="solid"
        )
        get_otp_button.grid(row=2, column=0, pady=10, columnspan=2)

        # OTP Label & Entry
        tk.Label(otp_frame, text="Enter OTP", font=("Arial", 12)).grid(row=3, column=0, pady=2, sticky="w")
        otp_entry = tk.Entry(otp_frame, font=("Arial", 14), width=30, justify="center")
        otp_entry.grid(row=4, column=0, pady=2, columnspan=2)

        # Verify OTP Button
        verify_button = tk.Button(
            otp_frame, text="Verify OTP", command=verify_otp,
            font=("calibri", 14), width=32, pady=8, bg="lightgreen",
            fg="white", relief="solid"
        )
        verify_button.grid(row=5, column=0, pady=10, columnspan=2)

        verification_window.mainloop()

    def resource_path(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def open_login_page_window(self):

        def open_signup_window():
            login_window.destroy()
            self.master.deiconify()

        self.master.withdraw()
        login_window = tk.Toplevel(self.master)
        login_window.title("Login page")

        # Use resource_path to get the correct icon path
        icon_path = resource_path("favicon.ico")
        login_window.wm_iconbitmap(icon_path)

        window_width, window_height = 500, 600
        self.center_window(login_window, window_width, window_height)

        client = MongoClient("mongodb+srv://adityabhoir983_db_user:TUViJnRnUnaO3qFS@cluster0.txhrbfx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client["user_data"]
        collection = db["users"]

        def read_file():
            username = username_entry.get().strip().lower()
            password = password_entry.get().strip()

            try:
                # Find user with matching credentials and inactive status
                user = collection.find_one({
                    "Username": username,
                    "Password": password,
                    "Status": "Inactive"
                })

                if user:
                    # Update status to Active upon successful login
                    collection.update_one(
                        {"Username": username},
                        {"$set": {"Status": "Active"}}
                    )

                    messagebox.showinfo("Success", "Login successful! Account activated.")
                    login_window.destroy()
                    self.billingsystem()
                else:
                    # Check if user exists but is already active
                    existing_user = collection.find_one({"Username": username})
                    if existing_user:
                        if existing_user["Status"] == "Active":
                            messagebox.showinfo("Info", "Login successful!")
                            login_window.destroy()
                            self.billingsystem()
                        else:
                            messagebox.showerror("Error", "Invalid credentials or account not verified.")
                    else:
                        messagebox.showerror("Error", "User not found.")

            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}")

        def on_hover(event):
            welcome_label.config(fg="#0066cc")

        def on_leave(event):
            welcome_label.config(fg="#333333")

        header_frame = tk.Frame(login_window)
        header_frame.grid(row=0, column=0, pady=50, padx=95)

        welcome_label = tk.Label(header_frame, text="Welcome back", font=("Helvetica Neue", 32, "bold"),
                                 fg="#333333",
                                 pady=10)
        welcome_label.bind("<Enter>", on_hover)
        welcome_label.bind("<Leave>", on_leave)
        welcome_label.grid(row=0, column=0)

        input_frame = tk.Frame(login_window)
        input_frame.grid(row=1, column=0, pady=20)

        username_entry = tk.Entry(input_frame, font=("Arial", 16), width=30, bd=2, relief="solid")
        password_entry = tk.Entry(input_frame, font=("Arial", 16), width=30, bd=2, relief="solid")

        def add_placeholder(entry, placeholder_text):
            entry.insert(0, placeholder_text)
            entry.configure(fg="grey")

            def on_focus_in(event):
                if entry.get() == placeholder_text:
                    entry.delete(0, tk.END)
                    entry.configure(fg="black")

            def on_focus_out(event):
                if not entry.get():
                    entry.insert(0, placeholder_text)
                    entry.configure(fg="grey")

            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)

        add_placeholder(username_entry, "Enter username ")
        username_entry.grid(row=0, column=0, padx=10, pady=10)

        add_placeholder(password_entry, "Enter password")
        password_entry.grid(row=1, column=0, padx=10, pady=10)

        submit = tk.Button(login_window, text="Login", font=("calibri", 14), command=read_file, width=35, pady=5,
                           padx=3,
                           bg="lightgreen", relief="solid")
        submit.grid(row=3, column=0, pady=20)

        signup_btn = tk.Button(
            login_window,
            text="Create New Account",
            font=("Calibri", 14),
            command=open_signup_window,
            bg="#f5f5f5",
            fg="#0066cc",
            activebackground="#f5f5f5",
            activeforeground="#004d99",
            relief="flat",
            borderwidth=0
        )
        signup_btn.grid(row=4, column=0, pady=20)

    def billingsystem(self):
        serial_entry = None

        def clear():
            nonlocal serial_entry  # Add this if you modify serial_entry in clear()

            chocolateentry.delete(0, END)
            butterscotchentry.delete(0, END)
            vanillaentry.delete(0, END)
            strawberryentry.delete(0, END)
            mangoentry.delete(0, END)
            caramelentry.delete(0, END)



            pepsientry.delete(0, END)
            cocacolaentry.delete(0, END)
            maazaentry.delete(0, END)
            dewentry.delete(0, END)
            spriteentry.delete(0, END)
            frootientry.delete(0, END)

            chocolateentry.insert(0, 0)
            butterscotchentry.insert(0, 0)
            vanillaentry.insert(0, 0)
            strawberryentry.insert(0, 0)
            mangoentry.insert(0, 0)
            caramelentry.insert(0, 0)

            pepsientry.insert(0, 0)
            cocacolaentry.insert(0, 0)
            maazaentry.insert(0, 0)
            dewentry.insert(0, 0)
            spriteentry.insert(0, 0)
            frootientry.insert(0, 0)

            icecreamsgstentry.delete(0, END)
            # chocolatesgstentry.delete(0, END)
            drinkssgstentry.delete(0, END)
            icecreamcgstentry.delete(0, END)
            # chocolatecgstentry.delete(0, END)
            drinkscgstentry.delete(0, END)

            icecreampriceentry.delete(0, END)
            # cadburypriceentry.delete(0, END)
            drinkspriceentry.delete(0, END)

            name_entry.delete(0, END)
            phone_entry.delete(0, END)
            billno_entry.delete(0, END)
            textarea.delete(1.0, END)
            gst_entry.delete(0, END)
            company_combobox.delete(0, END)
            serial_entry.delete(0, END)



        def search_bill():
            search_number = billno_entry.get().strip()  # Get and clean the bill number

            if not search_number:  # Check if empty
                messagebox.showerror('Error', 'Please enter a bill number')
                return

            found = False
            bills_dir = 'bills'

            # Check if bills directory exists
            if not os.path.exists(bills_dir):
                messagebox.showerror('Error', 'Bills directory not found')
                return

            try:
                # Walk through all date subdirectories
                for root, dirs, files in os.walk(bills_dir):
                    for filename in files:
                        # Remove extension and check match
                        if os.path.splitext(filename)[0] == search_number:
                            try:
                                filepath = os.path.join(root, filename)
                                with open(filepath, 'r', encoding='utf-8') as f:
                                    textarea.delete(1.0, END)
                                    textarea.insert(END, f.read())
                                found = True
                                return  # Exit after finding the first match
                            except Exception as e:
                                messagebox.showerror('Error', f'Failed to read bill: {str(e)}')
                                return

                if not found:
                    messagebox.showerror('Error', f'Bill {search_number} not found in any date folder')

            except Exception as e:
                messagebox.showerror('Error', f'Search failed: {str(e)}')

        def format_line(product, quantity, price):
            return f"{product:<20}{quantity:^10}{price:>15.2f} Rs"

        def validate_invoice_number():
            invoice_no = serial_entry.get().strip()
            if not invoice_no:
                messagebox.showerror("Error", "Invoice number is required")
                return False
            if not invoice_no.isdigit():
                messagebox.showerror("Error", "Invoice number must be numeric")
                return False
            return True

        def bill_area():
            if (icecreampriceentry.get() == '' and drinkspriceentry.get() == '') or \
                    (icecreampriceentry.get() == '0 Rs' and drinkspriceentry.get() == '0 Rs'):
                messagebox.showerror("Error", "No Products Selected")
            else:
                textarea.delete(1.0, END)

                invoice_no = serial_entry.get()

                # Get current date and time
                now = datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                time_str = now.strftime("%H:%M:%S")

                # Constants for formatting
                header_width = 60
                col1_width = 25  # Product column
                col2_width = 10  # Quantity column
                col3_width = 15  # Price column
                line_char = '═'
                thin_line_char = '─'

                # Header Section
                textarea.insert(END, line_char * header_width + '\n')
                textarea.insert(END, 'HARESH GAYKAR ENTERPRISES'.center(header_width) + '\n')
                textarea.insert(END, line_char * header_width + '\n')

                # Invoice info section
                textarea.insert(END, f"DATE:     {date_str:<16}INVOICE NO:     {serial_entry.get():>3}\n")
                textarea.insert(END, f"TIME:     {time_str:<16}GSTIN:    27AKOPG8754D1ZV\n")
                textarea.insert(END, thin_line_char * header_width + '\n')

                # Consignee Details
                textarea.insert(END, "BILL TO:\n")
                textarea.insert(END, f"{company_combobox.get()}\n")
                textarea.insert(END, f"GSTIN: {gst_entry.get()} \n")
                textarea.insert(END, thin_line_char * header_width + '\n')

                # Customer Details if available
                if name_entry.get() or phone_entry.get():
                    textarea.insert(END, "OTHER DETAILS:\n")
                    if name_entry.get():
                        textarea.insert(END, f"{'Vehicle no.: ':<10}{name_entry.get()}\n")
                    if phone_entry.get():
                        textarea.insert(END, f"{'Place of Supply: ':<10}{phone_entry.get()}\n")
                    textarea.insert(END, thin_line_char * header_width + '\n')

                # Product Table Header
                textarea.insert(END, f"{'DESCRIPTION':<{col1_width}}{'QTY':^{col2_width}}{'AMOUNT':>{col3_width}}\n")
                textarea.insert(END, thin_line_char * header_width + '\n')


                icecream_products = [
                    ('Package drinking water', chocolateentry, 29),
                    ('Bislery 250 ml', butterscotchentry, 240),
                    ('Bislery 500 ml', vanillaentry, 340),
                    ('Bislery 1l', strawberryentry, 240),
                    ('Bislery 2l', mangoentry, 270),
                    ('Bislery 5l', caramelentry, 75)
                ]
                coldrink_products = [
                    ('Pepsi', maazaentry, 45),
                    ('Sprite', frootientry, 35),
                    ('Jira Soda', dewentry, 15),
                    ('Sting', pepsientry, 15),
                    ('Thums Up', spriteentry, 45),
                    ('CocaCola', cocacolaentry, 45)
                ]

                # Calculate subtotals and taxes separately
                icecream_subtotal = 0
                coldrink_subtotal = 0

                # Ice cream products (9% GST)
                for name, entry, rate in icecream_products:
                    qty = entry.get()
                    if qty != '0' and qty != '':
                        qty_num = int(qty)
                        item_total = qty_num * rate
                        icecream_subtotal += item_total
                        textarea.insert(END,
                                        f"{name:<{col1_width}}{qty:^{col2_width}}{item_total:>{col3_width}.2f} Rs\n")

                # Cold drink products (20% GST)
                for name, entry, rate in coldrink_products:
                    qty = entry.get()
                    if qty != '0' and qty != '':
                        qty_num = int(qty)
                        item_total = qty_num * rate
                        coldrink_subtotal += item_total
                        textarea.insert(END,
                                        f"{name:<{col1_width}}{qty:^{col2_width}}{item_total:>{col3_width}.2f} Rs\n")

                subtotal = icecream_subtotal + coldrink_subtotal
                textarea.insert(END, thin_line_char * header_width + '\n')

                # Calculate taxes correctly
                icecream_sgst = icecream_subtotal * 0.09
                icecream_cgst = icecream_subtotal * 0.09
                coldrink_sgst = coldrink_subtotal * 0.20
                coldrink_cgst = coldrink_subtotal * 0.20

                # Amounts section
                textarea.insert(END, f"{'SUBTOTAL:':<{col1_width + col2_width}}{subtotal:>{col3_width}.2f} Rs\n")

                # Ice cream taxes (9%)
                if icecream_cgst > 0:
                    textarea.insert(END,
                                    f"{'Icecream CGST @9%:':<{col1_width + col2_width}}{icecream_cgst:>{col3_width}.2f} Rs\n")
                if icecream_sgst > 0:
                    textarea.insert(END,
                                    f"{'Icecream SGST @9%:':<{col1_width + col2_width}}{icecream_sgst:>{col3_width}.2f} Rs\n")
                if coldrink_cgst > 0:
                    textarea.insert(END,
                                    f"{'Coldrink CGST @20%:':<{col1_width + col2_width}}{coldrink_cgst:>{col3_width}.2f} Rs\n")
                if coldrink_sgst > 0:
                    textarea.insert(END,
                                    f"{'Coldrink SGST @20%:':<{col1_width + col2_width}}{coldrink_sgst:>{col3_width}.2f} Rs\n")

                # Grand Total
                total_tax = icecream_sgst + icecream_cgst + coldrink_sgst + coldrink_cgst
                global grand_total
                grand_total = subtotal + total_tax

                textarea.insert(END, line_char * header_width + '\n')
                textarea.insert(END, f"{'GRAND TOTAL:':<{col1_width + col2_width}}{grand_total:>{col3_width}.2f} Rs\n")
                textarea.insert(END, line_char * header_width + '\n')
                save_bill(serial_entry, textarea)

        def save_bill(serial_entry, textarea):
            try:
                # Detect script directory correctly in all environments
                if getattr(sys, 'frozen', False):
                    script_dir = os.path.dirname(sys.executable)
                else:
                    script_dir = os.path.dirname(os.path.abspath(__file__))

                default_folder = os.path.join(script_dir, "bills")
                fallback_folder = os.path.join(os.path.expanduser("~"), "PythonProject1", "bills")

                try:
                    os.makedirs(default_folder, exist_ok=True)
                    base_folder = default_folder
                except:
                    os.makedirs(fallback_folder, exist_ok=True)
                    base_folder = fallback_folder

                today_date = datetime.now().strftime("%d-%m-%Y")
                daily_folder = os.path.join(base_folder, today_date)
                os.makedirs(daily_folder, exist_ok=True)

                invoice_no = serial_entry.get().strip()
                if not invoice_no:
                    messagebox.showerror("Error", "Invoice number is required")
                    return False

                bill_content = textarea.get("1.0", END).strip()
                if not bill_content:
                    messagebox.showerror("Error", "No bill content to save")
                    return False

                file_path = os.path.join(daily_folder, f"{invoice_no}.txt")
                with open(file_path, "w", encoding='utf-8') as f:
                    f.write(bill_content)

                messagebox.showinfo("Success", f"Bill saved successfully to:\n{file_path}")
                return True

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save bill: {str(e)}")
                return False

        def Total():
            global chocolateprice, butterscotchprice, vanillaprice, strawberryprice, mangoprice, Caramelprice
            global maazaprice, frootiprice, dewprice, pepsiprice, spriteprice, cocacolaprice
            global totalbill


            # Prices for Products
            WATER_PRICE = 29
            BUTTERSCOTCH_PRICE = 240
            VANILLA_PRICE = 240
            STRAWBERRY_PRICE = 240
            MANGO_PRICE = 270
            CARAMEL_PRICE = 75

            MAAZA_PRICE = 50
            FROOTI_PRICE = 20
            DEW_PRICE = 30
            PEPSI_PRICE = 20
            SPRITE_PRICE = 45
            COCACOLA_PRICE = 90

            # Calculate Subtotal for Each Category
            # Water/Ice Cream Products (9% GST each)
            water_icecream_subtotal = (
                    int(chocolateentry.get()) * WATER_PRICE +
                    int(butterscotchentry.get()) * BUTTERSCOTCH_PRICE +
                    int(vanillaentry.get()) * VANILLA_PRICE +
                    int(strawberryentry.get()) * STRAWBERRY_PRICE +
                    int(mangoentry.get()) * MANGO_PRICE +
                    int(caramelentry.get()) * CARAMEL_PRICE
            )

            # Cold Drink Products (20% GST each)
            cold_drinks_subtotal = (
                    int(maazaentry.get()) * MAAZA_PRICE +
                    int(frootientry.get()) * FROOTI_PRICE +
                    int(dewentry.get()) * DEW_PRICE +
                    int(pepsientry.get()) * PEPSI_PRICE +
                    int(spriteentry.get()) * SPRITE_PRICE +
                    int(cocacolaentry.get()) * COCACOLA_PRICE
            )

            # Calculate Taxes for Each Category
            # Water/Ice Cream Taxes (9% SGST + 9% CGST)
            water_icecream_sgst = water_icecream_subtotal * 0.09
            water_icecream_cgst = water_icecream_subtotal * 0.09

            # Cold Drinks Taxes (20% SGST + 20% CGST)
            cold_drinks_sgst = cold_drinks_subtotal * 0.20
            cold_drinks_cgst = cold_drinks_subtotal * 0.20

            # Calculate Totals
            subtotal = water_icecream_subtotal + cold_drinks_subtotal
            total_tax = (water_icecream_sgst + water_icecream_cgst +
                         cold_drinks_sgst + cold_drinks_cgst)
            totalbill = subtotal + total_tax

            # Update GUI Fields
            icecreampriceentry.delete(0, END)
            icecreampriceentry.insert(0, f"{water_icecream_subtotal:.2f}")

            drinkspriceentry.delete(0, END)
            drinkspriceentry.insert(0, f"{cold_drinks_subtotal:.2f}")

            icecreamsgstentry.delete(0, END)
            icecreamsgstentry.insert(0, f"{water_icecream_sgst:.2f}")

            icecreamcgstentry.delete(0, END)
            icecreamcgstentry.insert(0, f"{water_icecream_cgst:.2f}")

            drinkssgstentry.delete(0, END)
            drinkssgstentry.insert(0, f"{cold_drinks_sgst:.2f}")

            drinkscgstentry.delete(0, END)
            drinkscgstentry.insert(0, f"{cold_drinks_cgst:.2f}")

            return {
                'water_icecream_subtotal': water_icecream_subtotal,
                'cold_drinks_subtotal': cold_drinks_subtotal,
                'water_icecream_sgst': water_icecream_sgst,
                'water_icecream_cgst': water_icecream_cgst,
                'cold_drinks_sgst': cold_drinks_sgst,
                'cold_drinks_cgst': cold_drinks_cgst,
                'total_tax': total_tax,
                'total_bill': totalbill
            }

        BG_COLOR = "#f5f5f5"
        PRIMARY_COLOR = "#2c5fde"  # More vibrant blue
        SECONDARY_COLOR = "#6c757d"
        SUCCESS_COLOR = "#28a745"  # Brighter green
        DANGER_COLOR = "#dc3545"
        LIGHT_COLOR = "#f8f9fc"
        DARK_COLOR = "#343a40"  # Darker for better contrast

        # Font sizes for HD display
        LARGE_FONT = ("Segoe UI", 18)
        XL_FONT = ("Segoe UI", 28)
        HEADER_FONT = ("Segoe UI", 20, "bold")
        TITLE_FONT = ("Segoe UI", 24, "bold")
        BUTTON_FONT = ("Segoe UI", 14)

        def center_window(window, width, height):
            """Center the window on screen"""
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)
            window.geometry(f'{width}x{height}+{x}+{y}')

        def show_subtotal_for_date(date_str, result_window):
            """Display billing summary with improved file handling"""
            try:
                # Clear previous widgets
                for widget in result_window.winfo_children():
                    widget.destroy()

                daily_folder = os.path.abspath(os.path.join("bills", date_str))
                subtotal_sum = 0.0
                bill_count = 0
                bill_details = []

                # Configure window
                result_window.configure(bg=BG_COLOR)
                result_window.attributes('-fullscreen', True)
                center_window(result_window, 1000, 800)



                if not os.path.exists(daily_folder):
                    # No bills found UI
                    no_bills_frame = tk.Frame(result_window, bg=BG_COLOR)
                    no_bills_frame.pack(expand=True, fill="both", padx=40, pady=40)

                    # Message section
                    message_frame = tk.Frame(no_bills_frame, bg=BG_COLOR)
                    message_frame.pack(expand=True, fill="both")

                    tk.Label(message_frame,
                             text="📁 No Bills Found",
                             font=TITLE_FONT,
                             fg=SECONDARY_COLOR,
                             bg=BG_COLOR).pack(pady=(60, 20))

                    tk.Label(message_frame,
                             text=f"Date: {date_str}",
                             font=LARGE_FONT,
                             fg=DARK_COLOR,
                             bg=BG_COLOR).pack()

                    # Close button only
                    close_btn = tk.Button(no_bills_frame,
                                          text="Close",
                                          command=result_window.destroy,
                                          font=BUTTON_FONT,
                                          bg=DANGER_COLOR,
                                          fg="white",
                                          padx=30,
                                          pady=10)
                    close_btn.pack(pady=40)

                    return

                # Process bills with better error handling
                for filename in sorted(os.listdir(daily_folder)):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(daily_folder, filename)
                        bill_number = filename.replace(".txt", "")

                        try:
                            with open(file_path, "r", encoding='utf-8') as f:
                                content = f.read()

                                # More flexible total amount extraction
                                matches = re.findall(
                                    r"(?:TOTAL|AMOUNT|BILL)\s*[:\-]?\s*(\d+\.?\d*)",
                                    content,
                                    re.IGNORECASE
                                )

                                if matches:
                                    bill_amount = float(matches[-1])
                                    bill_details.append((bill_number, bill_amount))
                                    subtotal_sum += bill_amount
                                    bill_count += 1
                                else:
                                    print(f"No amount found in {filename}")  # Debug
                        except Exception as e:
                            print(f"Error reading {filename}: {e}")  # Debug
                            continue

                # Main container
                main_frame = tk.Frame(result_window, bg=BG_COLOR)
                main_frame.pack(fill="both", expand=True, padx=40, pady=20)

                # Header
                header_frame = tk.Frame(main_frame, bg=BG_COLOR)
                header_frame.pack(fill="x", pady=(0, 20))

                tk.Label(header_frame,
                         text=f"📅 Daily Billing Report - {date_str}",
                         font=TITLE_FONT,
                         fg=DARK_COLOR,
                         bg=BG_COLOR).pack(side="left")

                # Stats cards
                cards_frame = tk.Frame(main_frame, bg=BG_COLOR)
                cards_frame.pack(fill="x", pady=20)

                # Bill Count Card
                count_card = tk.Frame(cards_frame, bg="white", bd=2, relief="groove", padx=20, pady=20)
                count_card.pack(side="left", expand=True, fill="both", padx=10, ipadx=20, ipady=20)

                tk.Label(count_card,
                         text="📋 Total Bills",
                         font=LARGE_FONT,
                         fg=SECONDARY_COLOR,
                         bg="white").pack(pady=(10, 20))

                tk.Label(count_card,
                         text=str(bill_count),
                         font=XL_FONT,
                         fg=PRIMARY_COLOR,
                         bg="white").pack(pady=(0, 10))

                # Total Amount Card
                total_card = tk.Frame(cards_frame, bg="white", bd=2, relief="groove", padx=20, pady=20)
                total_card.pack(side="left", expand=True, fill="both", padx=10, ipadx=20, ipady=20)

                tk.Label(total_card,
                         text="💰 Total Amount",
                         font=LARGE_FONT,
                         fg=SECONDARY_COLOR,
                         bg="white").pack(pady=(10, 20))

                tk.Label(total_card,
                         text=f"₹{subtotal_sum:.2f}",
                         font=XL_FONT,
                         fg=SUCCESS_COLOR,
                         bg="white").pack(pady=(0, 10))

                # Bill Details Section with Scrollbar
                details_frame = tk.Frame(main_frame, bg=BG_COLOR)
                details_frame.pack(fill="both", expand=True, pady=(20, 0))

                tk.Label(details_frame,
                         text="📄 Bill Details",
                         font=HEADER_FONT,
                         fg=DARK_COLOR,
                         bg=BG_COLOR).pack(anchor="w", pady=(0, 10))

                canvas = tk.Canvas(details_frame, bg="white", bd=0, highlightthickness=0)
                scrollbar = tk.Scrollbar(details_frame, orient="vertical", command=canvas.yview)
                scrollable_frame = tk.Frame(canvas, bg="white")

                scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)

                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")

                # Add bill details
                for bill_number, amount in sorted(bill_details, key=lambda x: x[0]):
                    bill_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief="groove")
                    bill_frame.pack(fill="x", pady=2, padx=2)

                    tk.Label(bill_frame,
                             text=f"Bill #{bill_number}",
                             font=("Segoe UI", 12),
                             bg="white",
                             width=15).pack(side="left", padx=10)

                    tk.Label(bill_frame,
                             text=f"₹{amount:.2f}",
                             font=("Segoe UI", 12, "bold"),
                             bg="white",
                             fg=SUCCESS_COLOR).pack(side="right", padx=10)

                # Buttons
                btn_frame = tk.Frame(main_frame, bg=BG_COLOR)
                btn_frame.pack(pady=(20, 0))

                export_btn = tk.Button(btn_frame,
                                       text="Export to PDF",
                                       command=lambda: export_daily_report(date_str, bill_details, subtotal_sum,
                                                                           bill_count),
                                       font=BUTTON_FONT,
                                       bg=PRIMARY_COLOR,
                                       fg="white",
                                       padx=20,
                                       pady=10)
                export_btn.pack(side="left", padx=10)

                close_btn = tk.Button(btn_frame,
                                      text="Close",
                                      command=result_window.destroy,
                                      font=BUTTON_FONT,
                                      bg=DANGER_COLOR,
                                      fg="white",
                                      padx=20,
                                      pady=10)
                close_btn.pack(side="left", padx=10)

            except Exception as e:
                print(f"Error in show_subtotal_for_date: {e}")
                error_frame = tk.Frame(result_window, bg=DANGER_COLOR)
                error_frame.pack(expand=True, fill="both")

                tk.Label(error_frame,
                         text="⚠️ Error",
                         font=TITLE_FONT,
                         fg="white",
                         bg=DANGER_COLOR).pack(pady=40)

                tk.Label(error_frame,
                         text=str(e),
                         font=LARGE_FONT,
                         fg="white",
                         bg=DANGER_COLOR).pack(pady=20)

        def export_daily_report(date_str, bill_details, total_amount, bill_count):
            """Export daily report to PDF with robust font handling"""
            try:
                from fpdf import FPDF
                from datetime import datetime
                from fpdf.enums import XPos, YPos
                import os
                from tkinter import messagebox
                import traceback

                # Create PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_title(f"Daily Report - {date_str}")

                # Font setup with multiple fallbacks
                font_configured = False
                rupee_symbol = "Rs."  # Default fallback symbol

                # Try built-in helvetica first (will always work)
                try:
                    pdf.set_font("helvetica", size=14)
                    # Test if we can use Unicode rupee symbol (may work on some systems)
                    try:
                        pdf.write(8, "₹")  # Test rupee symbol
                        rupee_symbol = "₹"
                        font_configured = True
                    except:
                        pass
                except:
                    pass

                if not font_configured:
                    # Final fallback to standard built-in font
                    pdf.set_font("helvetica", size=14)
                    rupee_symbol = "Rs."

                # Color scheme (keep your original colors)
                PRIMARY_COLOR = (44, 95, 222)
                SECONDARY_COLOR = (108, 117, 125)
                SUCCESS_COLOR = (40, 167, 69)
                HEADER_COLOR = (30, 60, 120)
                TABLE_HEADER_COLOR = (230, 230, 230)

                # Title with colored header bar
                pdf.set_fill_color(*HEADER_COLOR)
                pdf.set_text_color(255, 255, 255)
                pdf.set_font(style="B", size=20)
                pdf.cell(0, 15, f"Daily Report - {date_str}",
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", fill=True)
                pdf.ln(5)

                # Report metadata
                pdf.set_text_color(*SECONDARY_COLOR)
                pdf.set_font_size(12)
                pdf.cell(0, 8, f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
                pdf.ln(8)

                # Summary section
                pdf.set_font(style="B", size=14)
                pdf.set_text_color(*PRIMARY_COLOR)
                pdf.cell(0, 8, "SUMMARY", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
                pdf.ln(4)

                # Total Bills
                pdf.set_font(style="", size=12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(40, 8, "Total Bills:", new_x=XPos.RIGHT)
                pdf.set_text_color(*PRIMARY_COLOR)
                pdf.set_font(style="B", size=12)
                pdf.cell(0, 8, str(bill_count), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

                # Total Amount
                pdf.set_font(style="", size=12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(40, 8, "Total Amount:", new_x=XPos.RIGHT)
                pdf.set_text_color(*SUCCESS_COLOR)
                pdf.set_font(style="B", size=12)
                pdf.cell(0, 8, f"{rupee_symbol}{total_amount:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.ln(10)

                # Bill Details section
                pdf.set_font(style="B", size=14)
                pdf.set_text_color(*PRIMARY_COLOR)
                pdf.cell(0, 8, "BILL DETAILS", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
                pdf.ln(5)

                # Table Header
                pdf.set_fill_color(*TABLE_HEADER_COLOR)
                pdf.set_text_color(0, 0, 0)
                pdf.set_font(style="B", size=12)
                col_widths = [60, 40]
                pdf.cell(col_widths[0], 10, "Bill Number", border=1, align="C", fill=True)
                pdf.cell(col_widths[1], 10, f"Amount ({rupee_symbol})", border=1,
                         new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", fill=True)

                # Table Data
                pdf.set_font(style="", size=12)
                for i, (bill_number, amount) in enumerate(bill_details):
                    fill_color = (245, 245, 245) if i % 2 == 0 else (255, 255, 255)
                    pdf.set_fill_color(*fill_color)
                    pdf.cell(col_widths[0], 10, bill_number, border=1, align="C", fill=True)
                    pdf.cell(col_widths[1], 10, f"{amount:.2f}", border=1,
                             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C", fill=True)

                # Footer
                pdf.set_y(-20)
                pdf.set_font(style="I", size=10)
                pdf.set_text_color(*SECONDARY_COLOR)
                pdf.cell(0, 10, "Generated by Retail Billing System", align="C")

                # Save PDF
                try:
                    # 1. Get the executable's directory
                    if getattr(sys, 'frozen', False):
                        base_dir = os.path.dirname(sys.executable)
                    else:
                        base_dir = os.path.dirname(os.path.abspath(__file__))

                    # 2. Create reports directory if it doesn't exist
                    reports_dir = os.path.join(base_dir, "reports")
                    os.makedirs(reports_dir, exist_ok=True)

                    # 3. Generate filename
                    filename = f"Daily_Report_{date_str.replace('-', '_')}.pdf"
                    pdf_output = os.path.join(reports_dir, filename)
                    pdf.output(pdf_output)

                    # Show success message
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Success", f"Daily report saved as:\n{pdf_output}", parent=root)
                    root.destroy()

                    return pdf_output

                except Exception as e:
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Error", f"Failed to save PDF: {str(e)}", parent=root)
                    root.destroy()
                    return None

                except Exception as e:
                    traceback.print_exc()
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showerror("Error", f"Failed to generate PDF report: {str(e)}", parent=root)
                root.destroy()

            except Exception as e:
                # Show detailed error message
                root = tk.Tk()
                root.withdraw()
                error_msg = f"Failed to export daily report:\n{str(e)}"
                if hasattr(e, 'message'):
                    error_msg += f"\n\n{e.message}"
                messagebox.showerror("Error", error_msg, parent=root)
                root.destroy()

        def subtotal():
            """Create HD-optimized calendar window with daily/monthly report options"""
            try:
                # Create calendar window with HD dimensions
                top = tk.Toplevel(root)
                top.title("Select Date")
                top.geometry("800x600")  # Larger initial size
                top.configure(bg=BG_COLOR)
                top.resizable(False, False)

                # Set icon for the toplevel window
                try:
                    icon_path = resource_path("favicon.ico")
                    top.wm_iconbitmap(icon_path)
                except tk.TclError as e:
                    print(f"Error loading icon for calendar window: {e}")

                # Center window
                def center_window():
                    top.update_idletasks()
                    width = top.winfo_width()
                    height = top.winfo_height()
                    x = (top.winfo_screenwidth() // 2) - (width // 2)
                    y = (top.winfo_screenheight() // 2) - (height // 2)
                    top.geometry(f'+{x}+{y}')

                center_window()
                top.grab_set()
                top.focus_force()

                # Header with larger text
                header_frame = tk.Frame(top, bg=PRIMARY_COLOR)
                header_frame.pack(fill="x")

                tk.Label(header_frame,
                         text="Select Billing Date",
                         font=TITLE_FONT,
                         fg="white",
                         bg=PRIMARY_COLOR,
                         padx=20,
                         pady=20).pack()

                # Calendar widget with larger font
                cal_frame = tk.Frame(top, bg=BG_COLOR)
                cal_frame.pack(pady=40, padx=40, fill="both", expand=True)

                cal = Calendar(cal_frame,
                               selectmode='day',
                               date_pattern="dd-mm-yyyy",
                               font=("Segoe UI", 16),
                               background="white",
                               foreground="black",
                               selectbackground=PRIMARY_COLOR,
                               selectforeground="white",
                               normalbackground=LIGHT_COLOR,
                               weekendbackground=LIGHT_COLOR,
                               headersbackground=SECONDARY_COLOR,
                               headersforeground="white",
                               bordercolor=SECONDARY_COLOR)
                cal.pack(fill="both", expand=True, padx=20, pady=20)

                # Button frame with larger buttons
                btn_frame = tk.Frame(top, bg=BG_COLOR)
                btn_frame.pack(pady=(0, 40))

                # Generate Daily Report button
                # Change this line in your subtotal() function:
                gen_btn = tk.Button(btn_frame,
                                    text="Daily Report",
                                    command=lambda: on_date_select(cal.get_date(), top, root),  # Added root here
                                    font=BUTTON_FONT,
                                    bg=SUCCESS_COLOR,
                                    fg="white",
                                    activebackground="#218838",
                                    relief="flat",
                                    padx=30,
                                    pady=12)
                gen_btn.pack(side="left", padx=10)

                # Generate Monthly Report button
                month_btn = tk.Button(btn_frame,
                                      text="Monthly Report",
                                      command=lambda: on_month_select(cal.get_date(), top),
                                      font=BUTTON_FONT,
                                      bg="#6c757d",
                                      fg="white",
                                      activebackground="#5a6268",
                                      relief="flat",
                                      padx=30,
                                      pady=12)
                month_btn.pack(side="left", padx=10)

                # Cancel button
                cancel_btn = tk.Button(btn_frame,
                                       text="Cancel",
                                       command=top.destroy,
                                       font=BUTTON_FONT,
                                       bg=DANGER_COLOR,
                                       fg="white",
                                       activebackground="#c82333",
                                       relief="flat",
                                       padx=30,
                                       pady=12)
                cancel_btn.pack(side="left", padx=10)

                # Tooltips for buttons
                def create_tooltip(widget, text):
                    tooltip = tk.Toplevel(widget)
                    tooltip.wm_overrideredirect(True)
                    tooltip.wm_geometry("+0+0")
                    label = tk.Label(tooltip, text=text, bg="yellow", relief="solid", borderwidth=1)
                    label.pack()
                    widget.bind("<Enter>", lambda e: tooltip.deiconify())
                    widget.bind("<Leave>", lambda e: tooltip.withdraw())

                create_tooltip(gen_btn, "Generate report for selected day")
                create_tooltip(month_btn, "Generate report for entire month of selected date")
                create_tooltip(cancel_btn, "Close this window")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to open calendar: {str(e)}")
                if 'top' in locals():
                    top.destroy()

        def on_date_select(selected_date, top_window, root):
            """Handle date selection for report generation"""
            try:
                top_window.destroy()
                report_window = tk.Toplevel(root)
                report_window.title(f"Daily Report - {selected_date}")
                report_window.configure(bg=BG_COLOR)
                show_subtotal_for_date(selected_date, report_window)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate report: {str(e)}")

        def on_month_select(selected_date, top_window):
            """Handle monthly date selection"""
            try:
                top_window.destroy()
                # Extract month and year from selected date (format: dd-mm-yyyy)
                day, month, year = map(int, selected_date.split('-'))
                month_str = datetime.strptime(f"01-{month}-{year}", "%d-%m-%Y").strftime("%B %Y")

                report_window = tk.Toplevel(root)
                report_window.title(f"Monthly Report - {month_str}")
                report_window.attributes('-fullscreen', True)  # Make window fullscreen
                center_window(report_window, 1000, 700)  # Provide width and height for centering
                report_window.configure(bg=BG_COLOR)

                # Show monthly summary
                show_monthly_report(month, year, report_window)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate monthly report: {str(e)}")

        def export_monthly_report(month, year, month_str, daily_totals, total_amount, bill_count):
            """Export the monthly report to a stylish PDF using current fpdf2 syntax"""
            try:
                from fpdf import FPDF
                from fpdf.enums import XPos, YPos
                from datetime import datetime
                import os
                from tkinter import messagebox

                # Create a new PDF
                pdf = FPDF()

                # Use built-in helvetica font (no substitution warnings)
                pdf.set_font("helvetica", size=14)

                pdf.add_page()

                # Set document metadata
                pdf.set_title(f"Monthly Report - {month_str}")
                pdf.set_author("Billing System")

                # Title
                pdf.set_font("helvetica", style="B", size=20)
                pdf.set_text_color(44, 95, 222)  # Primary color
                pdf.cell(
                    0, 15,
                    f"Monthly Report - {month_str}",
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                    align="C"
                )

                # Summary Section
                pdf.set_font("helvetica", size=14)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(
                    0, 10,
                    f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                    align="C"
                )
                pdf.ln(5)  # Line break

                # Total Bills and Amount
                pdf.set_font("helvetica", style="B", size=16)
                pdf.set_text_color(28, 167, 69)  # Success color
                pdf.cell(
                    0, 10,
                    f"Total Bills: {bill_count}",
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                    align="L"
                )
                pdf.cell(
                    0, 10,
                    f"Total Amount: Rs.{total_amount:,.2f}",
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                    align="L"
                )
                pdf.ln(5)

                # Subheading for Daily Breakdown
                pdf.set_font("helvetica", style="B", size=16)
                pdf.set_text_color(60, 60, 60)  # Dark color for contrast
                pdf.cell(
                    0, 10,
                    "Daily Breakdown",
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                    align="L"
                )
                pdf.ln(5)

                # Table Header
                pdf.set_font("helvetica", style="B", size=12)
                pdf.set_fill_color(108, 117, 125)  # Secondary color
                pdf.set_text_color(255, 255, 255)
                pdf.cell(
                    50, 10,
                    "Date",
                    border=1, align="C", fill=True,
                    new_x=XPos.RIGHT
                )
                pdf.cell(
                    100, 10,
                    "Total Amount (Rs.)",
                    border=1, align="C", fill=True,
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT
                )

                # Table Data
                pdf.set_font("helvetica", size=12)
                pdf.set_text_color(0, 0, 0)

                for day, amount in sorted(daily_totals, key=lambda x: x[0]):
                    date_str = f"{day:02d}-{month:02d}-{year}"
                    pdf.cell(
                        50, 10,
                        date_str,
                        border=1, align="C",
                        new_x=XPos.RIGHT
                    )
                    pdf.cell(
                        100, 10,
                        f"Rs.{amount:,.2f}",
                        border=1, align="C",
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT
                    )

                # Footer
                pdf.set_y(-20)
                pdf.set_font("helvetica", style="I", size=10)
                pdf.set_text_color(100, 100, 100)
                pdf.cell(
                    0, 10,
                    "Generated by Retail Billing System",
                    align="C"
                )

                # Save the PDF to the "reports" folder
                if not os.path.exists("reports"):
                    os.makedirs("reports")
                pdf_output = f"reports/Monthly_Report_{month:02d}_{year}.pdf"
                pdf.output(pdf_output)

                messagebox.showinfo("Success", f"Monthly report saved as {pdf_output}")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to export monthly report: {str(e)}")

        def show_monthly_report(month, year, window):
            """Display monthly billing summary with all bills"""
            try:
                month_str = datetime.strptime(f"01-{month}-{year}", "%d-%m-%Y").strftime("%B %Y")
                total_amount = 0
                bill_count = 0
                daily_details = []  # Will store (day, [(bill_number, amount), ...])

                # Scan all days in month
                for day in range(1, 32):  # Will handle months with <31 days automatically
                    try:
                        date_str = f"{day:02d}-{month:02d}-{year}"
                        date_folder = os.path.join("bills", date_str)
                        day_bills = []

                        if os.path.exists(date_folder):
                            for filename in os.listdir(date_folder):
                                if filename.endswith(".txt"):
                                    try:
                                        bill_number = filename.replace(".txt", "")
                                        with open(os.path.join(date_folder, filename), 'r', encoding='utf-8') as f:
                                            content = f.read()
                                            # More flexible amount extraction
                                            matches = re.findall(
                                                r"(?:TOTAL|AMOUNT|BILL)\s*[:\-]?\s*(\d+\.?\d*)",
                                                content,
                                                re.IGNORECASE
                                            )
                                            if matches:
                                                amount = float(matches[-1])
                                                day_bills.append((bill_number, amount))
                                                total_amount += amount
                                                bill_count += 1
                                    except Exception as e:
                                        print(f"Error processing {filename}: {e}")
                                        continue

                            if day_bills:
                                daily_details.append((day, day_bills))
                    except Exception as e:
                        print(f"Error processing day {day}: {e}")
                        continue

                # Create UI
                for widget in window.winfo_children():
                    widget.destroy()

                # Header
                header_frame = tk.Frame(window, bg=PRIMARY_COLOR)
                header_frame.pack(fill="x", pady=(0, 20))

                tk.Label(header_frame,
                         text=f"Monthly Report - {month_str}",
                         font=TITLE_FONT,
                         fg="white",
                         bg=PRIMARY_COLOR).pack(pady=20)

                # Summary cards
                cards_frame = tk.Frame(window, bg=BG_COLOR)
                cards_frame.pack(fill="x", pady=10)

                # Total Bills card
                total_bills_card = tk.Frame(cards_frame, bg="white", bd=2, relief="groove", padx=20, pady=20)
                total_bills_card.pack(side="left", expand=True, fill="both", padx=10)

                tk.Label(total_bills_card,
                         text="Total Bills",
                         font=LARGE_FONT,
                         fg=SECONDARY_COLOR,
                         bg="white").pack()

                tk.Label(total_bills_card,
                         text=str(bill_count),
                         font=XL_FONT,
                         fg=PRIMARY_COLOR,
                         bg="white").pack()

                # Total Amount card
                total_amount_card = tk.Frame(cards_frame, bg="white", bd=2, relief="groove", padx=20, pady=20)
                total_amount_card.pack(side="left", expand=True, fill="both", padx=10)

                tk.Label(total_amount_card,
                         text="Total Amount",
                         font=LARGE_FONT,
                         fg=SECONDARY_COLOR,
                         bg="white").pack()

                tk.Label(total_amount_card,
                         text=f"₹{total_amount:,.2f}",
                         font=XL_FONT,
                         fg=SUCCESS_COLOR,
                         bg="white").pack()

                # Main content area with notebook for days
                main_frame = tk.Frame(window, bg=BG_COLOR)
                main_frame.pack(fill="both", expand=True, padx=20, pady=10)

                # Create a notebook (tabbed interface)
                notebook = ttk.Notebook(main_frame)
                notebook.pack(fill="both", expand=True)

                # Add a tab for each day with bills
                for day, bills in daily_details:
                    day_str = f"{day:02d}-{month:02d}-{year}"
                    day_frame = tk.Frame(notebook, bg=BG_COLOR)
                    notebook.add(day_frame, text=f"Day {day}")

                    # Day summary
                    day_total = sum(amount for _, amount in bills)
                    summary_frame = tk.Frame(day_frame, bg=BG_COLOR)
                    summary_frame.pack(fill="x", pady=(0, 10))

                    tk.Label(summary_frame,
                             text=f"📅 {day_str} - {len(bills)} bills - Total: ₹{day_total:.2f}",
                             font=HEADER_FONT,
                             bg=BG_COLOR).pack(side="left")

                    # Bills list with scrollbar
                    bill_list_frame = tk.Frame(day_frame, bg=BG_COLOR)
                    bill_list_frame.pack(fill="both", expand=True)

                    canvas = tk.Canvas(bill_list_frame, bg="white", bd=0, highlightthickness=0)
                    scrollbar = tk.Scrollbar(bill_list_frame, orient="vertical", command=canvas.yview)
                    scrollable_frame = tk.Frame(canvas, bg="white")

                    scrollable_frame.bind(
                        "<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
                    )

                    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                    canvas.configure(yscrollcommand=scrollbar.set)

                    canvas.pack(side="left", fill="both", expand=True)
                    scrollbar.pack(side="right", fill="y")

                    # Add bills to the scrollable frame
                    for bill_number, amount in sorted(bills, key=lambda x: x[0]):
                        bill_item = tk.Frame(scrollable_frame, bg="white", bd=1, relief="groove")
                        bill_item.pack(fill="x", pady=2, padx=2)

                        tk.Label(bill_item,
                                 text=f"Bill #{bill_number}",
                                 font=("Segoe UI", 12),
                                 bg="white",
                                 width=15).pack(side="left", padx=10)

                        tk.Label(bill_item,
                                 text=f"₹{amount:.2f}",
                                 font=("Segoe UI", 12, "bold"),
                                 bg="white",
                                 fg=SUCCESS_COLOR).pack(side="right", padx=10)

                # Export and Close buttons
                btn_frame = tk.Frame(window, bg=BG_COLOR)
                btn_frame.pack(pady=20)

                export_btn = tk.Button(btn_frame,
                                       text="Export to PDF",
                                       command=lambda: export_monthly_report(month, year, month_str,
                                                                             [(day, sum(amt for _, amt in bills))
                                                                              for day, bills in daily_details],
                                                                             total_amount, bill_count),
                                       font=BUTTON_FONT,
                                       bg=PRIMARY_COLOR,
                                       fg="white",
                                       padx=30,
                                       pady=10)
                export_btn.pack(side="left", padx=10)

                close_btn = tk.Button(btn_frame,
                                      text="Close",
                                      command=window.destroy,
                                      font=BUTTON_FONT,
                                      bg=DANGER_COLOR,
                                      fg="white",
                                      padx=30,
                                      pady=10)
                close_btn.pack(side="left", padx=10)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate monthly report: {str(e)}")
                print(f"Error in show_monthly_report: {traceback.format_exc()}")

        # Create main window
        from tkinter import ttk
        import tkinter as tk
        import os

        def resource_path(relative_path):
            """Get absolute path to resource, works for dev and for PyInstaller"""
            try:
                base_path = sys._MEIPASS  # If running from a PyInstaller bundle
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        root = tk.Tk()
        root.title("Retail Billing System")
        root.state('zoomed')

        # Set icon
        try:
            icon_path = resource_path("favicon.ico")
            root.wm_iconbitmap(icon_path)
        except tk.TclError as e:
            print(f"Error loading icon: {e}")

        # Configure root grid
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Main Container Frame
        main_frame = tk.Frame(root, padx=20, pady=20, bg="#FFF8F0")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # Heading Section
        heading_label = tk.Label(
            main_frame,
            text="Retail Billing System",
            font=("Times New Roman", 30, "bold"),
            bg="gray20", fg="gold", bd=12, relief=tk.RIDGE
        )
        heading_label.grid(row=0, column=0, columnspan=6, sticky="ew", pady=(0, 10))

        # Customer Details Section
        customer_details_frame = tk.LabelFrame(
            main_frame,
            text="Customer Details",
            font=("times new roman", 15, "bold"),
            fg="gold", bd=8, relief=tk.GROOVE, bg="gray20"
        )
        customer_details_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Company Data
        companies = {
            "TEXIZALABORATORIES LIMITED":"27AAJCT4577F127",
            "SADGURU NAMKEN ULHASNAGAR":"27AFC582714",
            "TAND TINFRA LIMITED PUNE":"27AAECT390H126",
            "REGENCY NIRMAN LTD. REGENCY AVANA MHARAL": "27AADC5058B12"
        }

        # Create StringVars
        company_var = tk.StringVar(root)
        gst_var = tk.StringVar(root)

        # Company Name Combobox with improved placeholder handling
        tk.Label(customer_details_frame, text="Company Name",
                 font=("times new roman", 15, "bold"),
                 bg="Gray20", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky='e')

        company_combobox = ttk.Combobox(customer_details_frame,
                                        textvariable=company_var,
                                        font=("Segoe UI", 12),  # HD Font for combobox text
                                        state='normal',
                                        values=list(companies.keys()))
        company_combobox.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        # Update the font for the dropdown list using ttk.Style
        style = ttk.Style()
        style.configure("TCombobox",
                        font=("Segoe UI", 14))  # HD font for the combobox itself

        style.map("TCombobox",
                  fieldbackground=[("readonly", "gray20")],
                  foreground=[("readonly", "white")])

        # Now, set the font for the dropdown list as well
        style.configure("TCombobox",
                        selectbackground="gray20",  # Background color
                        selectforeground="white",  # Text color
                        font=("Segoe UI", 14))  # HD font for the combobox dropdown

        company_combobox.config(style="TCombobox")

        # Placeholder functionality
        def on_focus_in(event):
            if company_var.get() == 'Type company name':
                company_var.set('')
                company_combobox.configure(foreground='black')

        def on_focus_out(event):
            if not company_var.get():
                company_var.set('Type company name')
                company_combobox.configure(foreground='grey')

        # Set initial placeholder
        company_var.set('Type company name')
        company_combobox.configure(foreground='grey')
        company_combobox.bind('<FocusIn>', on_focus_in)
        company_combobox.bind('<FocusOut>', on_focus_out)

        # GST Entry with uppercase enforcement
        tk.Label(customer_details_frame, text="GST No.",
                 font=("times new roman", 15, "bold"),
                 bg="Gray20", fg="white").grid(row=0, column=2, padx=10, pady=5, sticky='e')

        def force_uppercase(*args):
            current = gst_var.get()
            uppercase = current.upper()
            if current != uppercase:
                gst_var.set(uppercase)

        def validate_gst(char):
            return char.isupper() or char.isdigit() or char == ""

        validate_cmd = customer_details_frame.register(validate_gst)

        gst_entry = tk.Entry(customer_details_frame,
                             font=("Segoe UI", 12),
                             textvariable=gst_var,
                             bd=3, width=20,
                             relief=tk.SOLID,
                             validate="key",
                             validatecommand=(validate_cmd, '%S'))
        gst_entry.grid(row=0, column=3, padx=10, pady=5, sticky='ew')

        # Update GST when company selected
        def update_gst(event=None):
            selected = company_var.get()
            if selected in companies:
                gst_var.set(companies[selected])
            else:
                gst_var.set("")

        # Bind events
        company_combobox.bind("<<ComboboxSelected>>", update_gst)
        company_combobox.bind("<KeyRelease>", update_gst)  # Update as user types
        gst_var.trace_add("write", force_uppercase)

        # Name Entry
        tk.Label(customer_details_frame, text="Vehicle no.",
                 font=("times new roman", 15, "bold"),
                 bg="Gray20", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky='e')

        name_entry = tk.Entry(customer_details_frame,
                              font=("Segoe UI", 12),
                              bd=3, width=20,
                              relief=tk.SOLID)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        # Phone Entry
        tk.Label(customer_details_frame, text="Place of supply",
                 font=("times new roman", 15, "bold"),
                 bg="Gray20", fg="white").grid(row=1, column=2, padx=10, pady=5, sticky='e')

        phone_entry = tk.Entry(customer_details_frame,
                               font=("Segoe UI", 12),
                               bd=3, width=20,
                               relief=tk.SOLID)
        phone_entry.grid(row=1, column=3, padx=10, pady=5, sticky='ew')

        # Serial Number Entry
        tk.Label(customer_details_frame, text="Invoice No.",
                 font=("times new roman", 15, "bold"),
                 bg="Gray20", fg="white").grid(row=0, column=4, padx=10, pady=5, sticky='e')


        serial_entry = tk.Entry(customer_details_frame,
                                font=("Segoe UI", 12),
                                bd=3, width=20,
                                relief=tk.SOLID)
        serial_entry.grid(row=0, column=5, padx=10, pady=5, sticky='ew')

        # Bill Number Entry
        tk.Label(customer_details_frame, text="Search Invoice",
                 font=("times new roman", 15, "bold"),
                 bg="Gray20", fg="white").grid(row=1, column=4, padx=10, pady=5, sticky='e')

        billno_entry = tk.Entry(customer_details_frame,
                                font=("Segoe UI", 12),
                                bd=3, width=20,
                                relief=tk.SOLID)
        billno_entry.grid(row=1, column=5, padx=10, pady=5, sticky='ew')

        # Search Button
        search_btn = tk.Button(customer_details_frame,
                               text="SEARCH",
                               font=("Segoe UI", 12, "bold"),
                               bd=3,
                               relief=tk.RAISED,
                               command=search_bill)  # Directly connect to the function
        search_btn.grid(row=1, column=6, padx=10, pady=1, sticky='ew')

        # Configure column weights
        for i in range(7):
            customer_details_frame.grid_columnconfigure(i, weight=1 if i % 2 == 1 else 0)


        def create_quantity_control(parent_frame, row, label_text, entry_var=None):
            # Label
            label = Label(
                parent_frame,
                text=label_text,
                font=("times new roman", 15, "bold"),
                bg="gray20", fg="white"
            )
            label.grid(row=row, column=0, pady=9, padx=10, sticky='w')

            # Quantity control frame
            quantity_frame = Frame(parent_frame, bg="gray20")
            quantity_frame.grid(row=row, column=1, pady=9, padx=10)

            # Entry field
            entry_var = entry_var or StringVar()
            entry = Entry(
                quantity_frame,
                font=("times new roman", 15, "bold"),
                width=5, bd=5,
                justify="center",
                textvariable=entry_var,
                validate="key",
                validatecommand=(parent_frame.register(lambda char: char.isdigit() or char == ""), "%S")
            )
            entry.grid(row=0, column=1, padx=5, sticky="nsew")
            entry.insert(0, "0")

            # Update value function
            def update_value(change):
                try:
                    current_value = int(entry.get())
                    new_value = max(0, current_value + change)
                    entry.delete(0, END)
                    entry.insert(0, str(new_value))
                    if entry_var is not None:
                        entry_var.set(new_value)
                except ValueError:
                    entry.delete(0, END)
                    entry.insert(0, "0")

            # Minus button
            minus_btn = Button(
                quantity_frame,
                text="-", font=("Arial", 12, "bold"),
                command=lambda: update_value(-1),
                width=2, height=1
            )
            minus_btn.grid(row=0, column=0, sticky="nsew")

            # Plus button
            plus_btn = Button(
                quantity_frame,
                text="+", font=("Arial", 12, "bold"),
                command=lambda: update_value(1),
                width=2, height=1
            )
            plus_btn.grid(row=0, column=2, sticky="nsew")

            return entry

        # =============================================
        # Products Section
        # =============================================
        product_frame = Frame(main_frame, bg="gray20")
        product_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=10)
        product_frame.grid_columnconfigure(0, weight=1)
        product_frame.grid_columnconfigure(2, weight=1)
        product_frame.grid_columnconfigure(3, weight=2)

        # Water Products Frame
        icecreamframe = LabelFrame(
            product_frame,
            text="Water",
            font=("times new roman", 15, "bold"),
            fg="gold", bd=8, relief=GROOVE, bg="Gray20"
        )
        icecreamframe.grid(row=0, column=0, sticky="nsew")

        # Water products entries
        chocolateentry = create_quantity_control(icecreamframe, 0, "Package drinking water")
        butterscotchentry = create_quantity_control(icecreamframe, 1, "Bislery 250 ml")
        vanillaentry = create_quantity_control(icecreamframe, 2, "Bislery 500 ml")
        strawberryentry = create_quantity_control(icecreamframe, 3, "Bislery 1l")
        caramelentry = create_quantity_control(icecreamframe, 4, "Bislery 2l")
        mangoentry = create_quantity_control(icecreamframe, 5, "Bislery 5l")

        # Drinks Products Frame
        drinksframe = LabelFrame(
            product_frame,
            text="Cold Drinks",
            font=("times new roman", 15, "bold"),
            fg="gold", bd=8, relief=GROOVE, bg="Gray20"
        )
        drinksframe.grid(row=0, column=2, sticky="nsew")


        # Drink products entries
        maazaentry = create_quantity_control(drinksframe, 0, "Limca")
        pepsientry = create_quantity_control(drinksframe, 1, "Sprite")
        spriteentry = create_quantity_control(drinksframe, 2, "Jira soda")
        dewentry = create_quantity_control(drinksframe, 3, "Sting")
        frootientry = create_quantity_control(drinksframe, 4, "Thums Up")
        cocacolaentry = create_quantity_control(drinksframe, 5, "CocaCola")

        # =============================================
        # Bill Area Section
        # =============================================
        billFrame = Frame(product_frame, bd=8, relief=GROOVE, bg="gray20")
        billFrame.grid(row=0, column=3, sticky="nsew", padx=10)

        billarealabel = Label(
            billFrame,
            text='Bill Area',
            font=("times new roman", 15, "bold"),
            bd=7, relief=GROOVE,
            bg="gray20", fg="gold"
        )
        billarealabel.pack(fill=X)

        scrollbar = Scrollbar(billFrame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        textarea = Text(
            billFrame,
            height=18, width=55,
            yscrollcommand=scrollbar.set,
            font=("courier", 12),
            bg="white", fg="black",
            bd=5, relief=GROOVE
        )
        textarea.pack(fill=BOTH, expand=True)
        scrollbar.config(command=textarea.yview)

        billmenuframe = LabelFrame(
            main_frame,
            text="Bill Menu",
            font=("times new roman", 15, "bold"),
            fg="gold", bd=8, relief=GROOVE, bg="Gray20"
        )
        billmenuframe.grid(row=3, column=0, sticky="ew", padx=10, pady=10)

        # Configure grid columns
        for i in range(7):
            billmenuframe.grid_columnconfigure(i, weight=1 if i < 6 else 2)

        # Price Entries
        icecreampricelabel = Label(
            billmenuframe,
            text="Water Price",
            font=("times new roman", 14, "bold"),
            bg="gray20", fg="white"
        )
        icecreampricelabel.grid(row=0, column=0, pady=3, padx=8, sticky='e')

        icecreampriceentry = Entry(
            billmenuframe,
            font=("times new roman", 14, "bold"),
            width=10, bd=5
        )
        icecreampriceentry.grid(row=0, column=1, pady=3, padx=(0, 8), sticky='w')

        drinkspricelabel = Label(
            billmenuframe,
            text="ColdDrinks Price",
            font=("times new roman", 14, "bold"),
            bg="gray20", fg="white"
        )
        drinkspricelabel.grid(row=2, column=0, pady=3, padx=8, sticky='e')

        drinkspriceentry = Entry(
            billmenuframe,
            font=("times new roman", 14, "bold"),
            width=10, bd=5
        )
        drinkspriceentry.grid(row=2, column=1, pady=3, padx=(0, 8), sticky='w')

        # GST Entries
        icecreamsgstlabel = Label(
            billmenuframe,
            text="Water SGST",
            font=("times new roman", 14, "bold"),
            bg="gray20", fg="white"
        )
        icecreamsgstlabel.grid(row=0, column=2, pady=3, padx=8, sticky='e')

        icecreamsgstentry = Entry(
            billmenuframe,
            font=("times new roman", 14, "bold"),
            width=8, bd=5
        )
        icecreamsgstentry.grid(row=0, column=3, pady=3, padx=(0, 8), sticky='w')

        drinkssgstlabel = Label(
            billmenuframe,
            text="ColdDrinks SGST",
            font=("times new roman", 14, "bold"),
            bg="gray20", fg="white"
        )
        drinkssgstlabel.grid(row=2, column=2, pady=3, padx=8, sticky='e')

        drinkssgstentry = Entry(
            billmenuframe,
            font=("times new roman", 14, "bold"),
            width=8, bd=5
        )
        drinkssgstentry.grid(row=2, column=3, pady=3, padx=(0, 8), sticky='w')

        icecreamcgstlabel = Label(
            billmenuframe,
            text="Water CGST",
            font=("times new roman", 14, "bold"),
            bg="gray20", fg="white"
        )
        icecreamcgstlabel.grid(row=0, column=4, pady=3, padx=8, sticky='e')

        icecreamcgstentry = Entry(
            billmenuframe,
            font=("times new roman", 14, "bold"),
            width=8, bd=5
        )
        icecreamcgstentry.grid(row=0, column=5, pady=3, padx=(0, 8), sticky='w')

        drinkscgstlabel = Label(
            billmenuframe,
            text="ColdDrinks CGST",
            font=("times new roman", 14, "bold"),
            bg="gray20", fg="white"
        )
        drinkscgstlabel.grid(row=2, column=4, pady=3, padx=8, sticky='e')

        drinkscgstentry = Entry(
            billmenuframe,
            font=("times new roman", 14, "bold"),
            width=8, bd=5
        )
        drinkscgstentry.grid(row=2, column=5, pady=3, padx=(0, 8), sticky='w')

        # Buttons Frame
        buttonframe = Frame(billmenuframe, bd=0, bg="gray20")
        buttonframe.grid(row=0, column=6, rowspan=3, sticky='e')

        # Action Buttons
        totalbutton = Button(
            buttonframe,
            text="Total", font=("arial", 14, "bold"),
            bg="Gray20", fg="white", bd=4,
            width=8, height=2, pady=6,
            command=Total
        )
        totalbutton.grid(row=0, column=0, padx=5, pady=5)

        billbutton = Button(
            buttonframe,
            text="Bill", font=("arial", 14, "bold"),
            bg="Gray20", fg="white", bd=4,
            width=8, height=2, pady=6,
            command=bill_area
        )
        billbutton.grid(row=0, column=1, padx=5, pady=5)

        emailbutton = Button(
            buttonframe,
            text="PDF", font=("arial", 14, "bold"),
            bg="Gray20", fg="white", bd=4,
            width=8, height=2, pady=6,
            command=lambda: create_invoice(serial_entry)
        )
        emailbutton.grid(row=0, column=2, padx=5, pady=5)

        subtotalbutton = Button(
            buttonframe,
            text="Report", font=("arial", 14, "bold"),
            bg="Gray20", fg="white", bd=4,
            width=8, height=2, pady=6,
            command=subtotal
        )
        subtotalbutton.grid(row=0, column=3, padx=5, pady=5)

        clearbutton = Button(
            buttonframe,
            text="Clear", font=("arial", 14, "bold"),
            bg="Gray20", fg="white", bd=4,
            width=8, height=2, pady=6,
            command=clear
        )
        clearbutton.grid(row=0, column=4, padx=5, pady=5)

        import os
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.lib.units import inch
        from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, Image
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib import colors

        from pathlib import Path
        from datetime import datetime
        import sys

        def create_invoice(serial_entry=None):
            try:
                # 1. Get the executable's directory
                if getattr(sys, 'frozen', False):
                    base_dir = os.path.dirname(sys.executable)
                else:
                    base_dir = os.path.dirname(os.path.abspath(__file__))

                # 2. Create invoice_bills directory if it doesn't exist
                output_dir = os.path.join(base_dir, "invoice_bills")
                os.makedirs(output_dir, exist_ok=True)

                # 3. Generate filename with fallback
                invoice_number = (serial_entry.get() if serial_entry and serial_entry.get()
                                  else datetime.now().strftime('%Y%m%d_%H%M%S'))
                filename = f"Haresh_Gaykar_Invoice_{invoice_number}.pdf"
                filepath = os.path.join(output_dir, filename)

                # Create PDF document
                doc = SimpleDocTemplate(
                    filepath,
                    pagesize=letter,
                    leftMargin=0.5 * inch,
                    rightMargin=0.5 * inch,
                    topMargin=0.00 * inch,
                    bottomMargin=0.5 * inch
                )

                elements = []

                logo_path = "bappa_img-removebg-preview.png"
                second_logo_path = "coldrink_main_img.png"

                try:
                    logo = Image(logo_path, width=1.3 * inch, height=1.3 * inch)
                    second_logo = Image(second_logo_path, width=0.9 * inch, height=0.9 * inch)
                except:
                    logo = Paragraph("<b>[LOGO1]</b>", ParagraphStyle(name="LogoFallback", fontSize=12))
                    second_logo = Paragraph("<b>[LOGO2]</b>", ParagraphStyle(name="LogoFallback", fontSize=12))

                company_data = [
                    [Paragraph("<font color='orange'><b>HARESH GAYKAR ENTERPRISES</b></font>",
                               ParagraphStyle(name="CompanyName", fontName="Helvetica-Bold", fontSize=23.5,
                                              alignment=0))],
                    [Paragraph("Add:- Flat No. 102 A Wing, 1st Floor, Madhuban Sahakari",
                               ParagraphStyle(name="Address", fontName="Helvetica-Bold", fontSize=12, alignment=0,
                                              leftIndent=23))],
                    [Paragraph("Ghruh Nirman Cos. Tondlikar Nagar, Murbad",
                               ParagraphStyle(name="Address2", fontName="Helvetica-Bold", fontSize=12, alignment=0,
                                              leftIndent=58))],
                    [Paragraph("<font color='red'>Contact: 7744097686 / 8850013208</font>",
                               ParagraphStyle(name="Contact", fontName="Helvetica-Bold", fontSize=12, alignment=0,
                                              leftIndent=80))],
                    [Paragraph("<font color='purple'>Email: gaykar.harish@gmail.com</font>",
                               ParagraphStyle(name="Email", fontName="Helvetica-Bold", alignment=0, fontSize=12,
                                              leftIndent=83))]
                ]

                company_table = Table(company_data, colWidths=[5 * inch])
                company_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (-1, -1), -26),
                    ('BOTTOMPADDING', (0, 0), (0, 0), 10),
                    ('TOPPADDING', (0, 1), (0, 2), 5),
                    ('BOTTOMPADDING', (0, 1), (0, 2), 0),
                    ('TOPPADDING', (0, 3), (0, 4), 1),
                    ('BOTTOMPADDING', (0, 3), (0, 4), 1),
                ]))

                header_table = Table([
                    [logo, Spacer(0.1 * inch, 0.1 * inch), company_table, Spacer(0.1 * inch, 0.1 * inch), second_logo]
                ], colWidths=[1.3 * inch, 0.1 * inch, 4.5 * inch, 0.1 * inch, 1.3 * inch])

                header_table.setStyle(TableStyle([
                    ('VALIGN', (0, 0), (-1, -6), 'TOP'),
                    ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                    ('ALIGN', (4, 0), (4, 0), 'RIGHT'),
                    ('LEFTPADDING', (0, 0), (0, 0), -2),
                    ('RIGHTPADDING', (4, 0), (4, 0), -5),
                    ('BOTTOMPADDING', (0, 0), (0, 0), -16),
                    ('BOTTOMPADDING', (0, 3), (-1, -1), 0),
                ]))

                elements.append(header_table)
                elements.append(Spacer(1, 0.1 * inch))

                # GST Table
                gst_data = [
                    ["GSTIN 27AKOPG8754D1ZV", "State : Maharashtra", "State Code : 27"]
                ]

                gst_table = Table(gst_data, colWidths=[doc.width / 3] * 3)
                gst_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(gst_table)

                new_row_data = [
                    [
                        Paragraph(f"<b>&nbsp;Invoice No : {serial_entry.get()}</b>",
                                  ParagraphStyle(name="InvoiceNo", fontName="Helvetica-Bold", fontSize=11,
                                                 leftIndent=10)),
                        Paragraph(f"<b>Party GST No. {gst_entry.get()}</b>",
                                  ParagraphStyle(name="Date", fontName="Helvetica-Bold", fontSize=11, leftIndent=1))
                    ]
                ]

                new_row_table = Table(new_row_data,
                                      colWidths=[doc.width * 0.58, doc.width * 0.42],
                                      rowHeights=[0.3 * inch])

                new_row_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(new_row_table)

                today_date = datetime.now().strftime("%d-%m-%Y")

                company_info = company_combobox.get().replace('\n', '\n    ')
                consignee_text = f"    Detail of Consignee : {company_info}"

                transport_text = f"""<b>    Mode of Transport : Road<br/>  Vehicle No. : {name_entry.get()} <br/> Date : {today_date} <br/> Place of Supply : {phone_entry.get()}</b>"""

                consignee_style = ParagraphStyle(
                    'ConsigneeStyle',
                    fontName='Helvetica-Bold',
                    fontSize=11,
                    leading=14,
                    leftIndent=0,
                    spaceBefore=0,
                    spaceAfter=0
                )

                transport_style = ParagraphStyle(
                    'TransportStyle',
                    fontName='Helvetica-Bold',
                    fontSize=11,
                    leading=14,
                    leftIndent=0,
                    spaceBefore=0,
                    spaceAfter=0
                )

                main_data = [
                    [
                        Paragraph(consignee_text, consignee_style),
                        Paragraph(transport_text, transport_style)
                    ]
                ]

                main_table = Table(main_data,
                                   colWidths=[doc.width * 0.58, doc.width * 0.42],
                                   rowHeights=[0.9 * inch])

                main_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('BOX', (0, 0), (-1, -1), 1, colors.black),
                    ('LINEAFTER', (0, 0), (0, 0), 1, colors.black),
                ]))
                elements.append(main_table)

                item_header = ["Sr.No.", "DESCRIPTION OF GOODS", "HSN CODE", "Qty", "Rate", "Total", "Total Amount"]

                products = [
                    ("Package drinking water", int(chocolateentry.get()), 29, 220110),
                    ("Bislery 250 ml", int(butterscotchentry.get()), 240, 220110),
                    ("Bislery 500 ml", int(vanillaentry.get()), 340, 220110),
                    ("Bislery 1l", int(strawberryentry.get()), 240, 220110),
                    ("Bislery 2l", int(mangoentry.get()), 270, 220110),
                    ("Bislery 5l", int(caramelentry.get()), 75, 220110),
                    ("Pepsi", int(maazaentry.get()), 45, 220110),
                    ("Sprite", int(pepsientry.get()), 35, 220110),
                    ("Jira Soda", int(spriteentry.get()), 15, 220110),
                    ("Sting", int(dewentry.get()), 15, 220110),
                    ("Thums Up", int(frootientry.get()), 45, 220110),
                    ("CocaCola", int(cocacolaentry.get()), 45, 220110)
                ]

                item_rows = []
                for idx, (product, qty, rate, hsn) in enumerate(products):
                    if qty > 0:
                        total = qty * rate
                        item_rows.append([
                            str(len(item_rows) + 1).zfill(2),
                            product,
                            str(hsn),
                            str(qty),
                            f"{rate:.2f}",
                            f"{total:.2f}",
                            f"{total:.2f}"
                        ])

                item_data = [item_header] + item_rows

                col_widths = [
                    0.06 * doc.width,
                    0.33 * doc.width,
                    0.11 * doc.width,
                    0.08 * doc.width,
                    0.12 * doc.width,
                    0.14 * doc.width,
                    0.16 * doc.width
                ]

                items_table = Table(item_data, colWidths=col_widths)

                items_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 11),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 1), (-1, -1), 11),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('LINEAFTER', (0, 0), (5, -1), 1, colors.black),
                    ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
                    ('BOX', (0, 0), (-1, -1), 1, colors.black),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
                ]))

                elements.append(items_table)

                total_amount = sum(float(row[-1]) for row in item_rows)
                totalbill = f"{total_amount:.2f}"

                # Calculate total GST for both Water and ColdDrinks
                try:
                    water_cgst = float(icecreamcgstentry.get() or 0)
                    water_sgst = float(icecreamsgstentry.get() or 0)
                    drinks_cgst = float(drinkscgstentry.get() or 0)
                    drinks_sgst = float(drinkssgstentry.get() or 0)

                    total_cgst = water_cgst + drinks_cgst
                    total_sgst = water_sgst + drinks_sgst
                except ValueError:
                    total_cgst = 0
                    total_sgst = 0

                def number_to_words(num):
                    try:
                        if isinstance(num, str):
                            num = float(num.replace(',', ''))
                        num = float(num)
                    except (ValueError, TypeError):
                        return "Could not convert amount to words"

                    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
                    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                             "Seventeen", "Eighteen", "Nineteen"]
                    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                            "Seventy", "Eighty", "Ninety"]

                    if num == 0:
                        return "Zero Rupees"

                    def convert_less_than_hundred(n):
                        if n < 10:
                            return units[n]
                        elif 10 <= n < 20:
                            return teens[n - 10]
                        else:
                            return tens[n // 10] + (" " + units[n % 10] if n % 10 != 0 else "")

                    def convert_less_than_thousand(n):
                        if n < 100:
                            return convert_less_than_hundred(n)
                        hundred = units[n // 100] + " Hundred"
                        remainder = n % 100
                        if remainder == 0:
                            return hundred
                        return hundred + " and " + convert_less_than_hundred(remainder)

                    rupees = int(num)
                    paise = round((num - rupees) * 100)

                    parts = []
                    if rupees == 0:
                        parts.append("Zero")
                    else:
                        for scale, word in [(10000000, "Crore"), (100000, "Lakh"), (1000, "Thousand"),
                                            (100, "Hundred")]:
                            if rupees >= scale:
                                part = convert_less_than_thousand(rupees // scale)
                                if part:
                                    parts.append(part + " " + word)
                                rupees %= scale

                        if rupees > 0:
                            parts.append(convert_less_than_thousand(rupees))

                    words = " ".join(parts) + " Rupees"

                    if paise > 0:
                        words += " and " + convert_less_than_hundred(paise) + " Paise"

                    return words

                total_in_words = number_to_words(grand_total)
                left_text = f"""<b>Invoice Total in Words: {total_in_words}</b><br/>"""

                left_style = ParagraphStyle(
                    'LeftStyle',
                    fontName='Helvetica-Bold',
                    fontSize=12,
                    leading=14,
                    leftIndent=13,
                    spaceBefore=0,
                    spaceAfter=0,
                    alignment=0
                )

                right_style = ParagraphStyle(
                    'RightStyle',
                    fontName='Helvetica-Bold',
                    fontSize=11,
                    leading=14,
                    leftIndent=10,
                    spaceBefore=0,
                    spaceAfter=0
                )

                # Updated total table data to include both Water and ColdDrinks GST
                total_table_data = [
                    [
                        Paragraph(left_text, left_style),
                        Paragraph("<b>Total CGST</b>", right_style),
                        Paragraph(f"{total_cgst:.2f}", right_style)
                    ],
                    [
                        "",
                        Paragraph("<b>Total SGST</b>", right_style),
                        Paragraph(f"{total_sgst:.2f}", right_style)
                    ],
                    [
                        "",
                        Paragraph("<b>IGST</b>", right_style),
                        Paragraph("", right_style)
                    ],
                    [
                        "",
                        Paragraph("<b>Total Amount</b>", right_style),
                        Paragraph(f"{grand_total}", right_style)
                    ],
                    [
                        "",
                        Paragraph("<b>Transport Charge</b>", right_style),
                        Paragraph("", right_style)
                    ],
                    [
                        "",
                        Paragraph("<b>Loading Charge</b>", right_style),
                        Paragraph("", right_style)
                    ],
                    [
                        "",
                        Paragraph("<b>Invoice Total:</b>", right_style),
                        Paragraph(f"{grand_total}", right_style)
                    ]
                ]




                col_widths = [
                    0.58 * doc.width,  # Invoice Total in Words
                    0.26 * doc.width,  # Labels column
                    0.16 * doc.width  # Values column
                ]

                # Row heights
                row_heights = [0.26 * inch] * 7

                # Create the table
                total_table = Table(total_table_data, colWidths=col_widths, rowHeights=row_heights)

                # Style the table
                total_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                    ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Outer border
                    ('GRID', (1, 0), (-1, -1), 1, colors.black),  # Inner grid for right side
                    ('LINEAFTER', (0, 0), (0, -1), 1, colors.black),  # Vertical line after left column
                    ('LINEAFTER', (1, 0), (1, -1), 1, colors.black),  # Vertical line between labels and values
                        ('VALIGN', (0, 0), (0, 0), 'TOP'),  # Align Invoice Total in Words to top
                        ('VALIGN', (1, 0), (-1, -1), 'MIDDLE'),
                        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),  # Right align values
                        ('SPAN', (0, 0), (0, -1)),  # Merge Invoice Total in Words cells
                    ]))

                elements.append(total_table)

                elements.append(Spacer(1, 0.3 * inch))

                # 7. Add certification text on left and signature on right
                # 7. Add certification text on left and signature on right
                certification_text = """<b>Certified That The Particulars Given Above Are<br/>
                             True And Correct And Amount Indicate<br/>
                             A) Represent The Price Actually Charged And That <br/>
                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There Is No Additional
                             Considerations Directly From<br/>
                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Buyer Or Terms Of Sale<br/>
                             1) Goods Once Sold Will Not Be Taken Back Or Exchange<br/>
                             2) Seller is Not Responsible For Any Loss Or Damaged <br/>
                             &nbsp;&nbsp;&nbsp;&nbsp;in Transit</b>"""

                signature_text = """<b><font color=red>For Haresh Gaykar Enterprises</font><br/><br/><br/><br/><br/>
                             Authorized Signatory</b>"""

                # Create styles with adjusted alignment
                certification_style = ParagraphStyle(
                    'CertificationStyle',
                    fontName='Helvetica-Bold',
                    fontSize=12,
                    leading=13,
                    leftIndent=2.5,
                    spaceBefore=0,
                    spaceAfter=0,
                    alignment=0  # Left align
                )

                signature_style = ParagraphStyle(
                    'SignatureStyle',
                    fontName='Helvetica-Bold',
                    fontSize=13,
                    leading=14,
                    leftIndent=0,  # Added left indent to move signature left
                    spaceBefore=0,
                    spaceAfter=0,
                    alignment=1  # Right align
                )

                # Create a two-column table with adjusted column widths
                footer_data = [
                    [
                        Paragraph(certification_text, certification_style),
                        Paragraph(signature_text, signature_style)
                    ]
                ]

                # Adjust column widths to shift signature left
                footer_table = Table(footer_data,
                                     colWidths=[doc.width * 0.70, doc.width * 0.30 - 30],  # Adjusted widths
                                     hAlign='LEFT')

                # Set style with adjusted padding
                footer_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('LEFTPADDING', (0, 0), (0, 0), 0),
                    ('RIGHTPADDING', (1, 0), (1, 0), 5),  # Reduced right padding
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                ]))

                elements.append(footer_table)

                def on_first_page(canvas, doc):
                    canvas.saveState()
                    canvas.setStrokeColorRGB(0, 0, 0)
                    canvas.setLineWidth(1.5)

                    # Page border coordinates (0.5 inch margins)
                    left = 0.5 * inch
                    right = left + doc.width
                    top = doc.height + 0.5 * inch  # 0.5 inch from top (topMargin=0)
                    bottom = 0.5 * inch

                    # Draw main page borders (left, top, right)
                    canvas.line(left, bottom, left, top)  # Left
                    canvas.line(left, top, right, top)  # Top
                    canvas.line(right, top, right, bottom)  # Right

                    canvas.line(left, bottom, right, bottom)  # Bottom border

                    canvas.restoreState()

                # Generate PDF
                doc.build(elements, onFirstPage=on_first_page)
                messagebox.showinfo("Success", f"Invoice saved successfully at:\n{filepath}")

                return filepath

            except Exception as e:
                messagebox.showerror("Error", f"Failed to create invoice:\n{str(e)}")
                return None


    def on_click(self):

        if self.inputs.info2():
            self.fName = self.inputs.get_first_name()
            self.lName = self.inputs.get_last_name()
            self.gender = self.inputs.get_gender()
            self.age = self.inputs.get_age()
            self.gmail = self.inputs.get_gmail()
            self.mobile = self.inputs.get_mobile()
            self.username = self.inputs.get_username()
            self.password = self.inputs.get_password()
            self.confirmP = self.inputs.get_confirm_password()

            if not self.inputs.check_mail(self.gmail):
                return

            password_error = self.inputs.validate_password_strength(self.password)
            if password_error:
                messagebox.showwarning("Notice", password_error)
                return

            response = messagebox.askyesno("Notice", "Are you sure to continue this form?")
            if response:
                self.abc()
                self.open_verification_window()
            else:
                messagebox.showwarning("Notice", "Form submission was cancelled")


buttons = Buttons(root)
root.mainloop()
