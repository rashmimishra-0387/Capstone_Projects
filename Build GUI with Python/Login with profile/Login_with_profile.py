"""
Signup Window: Allow users to create an account and save their details to a file.
Login Window: When a user logs in, read from the file and display the profile of the user matching the entered credentials.
File Storage: Save user data in a file (e.g., user_data.txt).
Display Profile: After login, show the user's profile details (like Name, Email, Address) on the Profile Screen.
"""


import tkinter as tk
from tkinter import ttk
import os

# File to store user credentials and profile data
USER_DATA_FILE = "user_data.txt"


def save_user_data(username, password, name, email, address):
    """Save the user details into a file."""
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username},{password},{name},{email},{address}\n")


def load_user_data():
    """Load user data from the file."""
    if not os.path.exists(USER_DATA_FILE):
        return []
    
    users = []
    with open(USER_DATA_FILE, "r") as file:
        for line in file.readlines():
            users.append(line.strip().split(","))
    return users


def find_user(username, password):
    """Find a user by username and password."""
    users = load_user_data()
    for user in users:
        if user[0] == username and user[1] == password:
            return user  # Return the full user data (username, password, name, email, address)
    return None


# Window 1: Login Screen
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")

        # Username and Password Entry widgets
        self.username_label = ttk.Label(self.root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = ttk.Label(self.root, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        self.login_button = ttk.Button(self.root, text="Login", command=self.check_credentials)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Signup button
        self.signup_button = ttk.Button(self.root, text="Sign Up", command=self.open_signup_window)
        self.signup_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Error message label (hidden by default)
        self.error_label = ttk.Label(self.root, text="Invalid credentials. Please try again.", foreground="red")
        self.error_label.grid(row=4, column=0, columnspan=2)
        self.error_label.grid_remove()

        # Reference to ProfileWindow
        self.profile_window = None

    def check_credentials(self):
        """Check if the entered credentials are correct."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = find_user(username, password)
        if user:
            # If credentials are correct, open the Profile Window
            self.open_profile_window(user)
        else:
            # Show error message if credentials are invalid
            self.error_label.grid()

    def open_profile_window(self, user_data):
        """Open the Profile Window."""
        self.profile_window = ProfileWindow(self.root, user_data)
        self.profile_window.show_profile_screen()

        # Close the login window after opening the profile window
        self.root.withdraw()  # Hide the login window

    def open_signup_window(self):
        """Open the Signup Window."""
        self.signup_window = SignupWindow(self.root)


# Window 2: Profile Screen
class ProfileWindow:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data  # User data (username, password, name, email, address)

        # Create a new Toplevel window for the profile
        self.profile_window = tk.Toplevel(self.root)
        self.profile_window.title("Profile Window")

        # Display the user's profile
        self.name_label = ttk.Label(self.profile_window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_label_value = ttk.Label(self.profile_window, text=self.user_data[2])  # Name
        self.name_label_value.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = ttk.Label(self.profile_window, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_label_value = ttk.Label(self.profile_window, text=self.user_data[3])  # Email
        self.email_label_value.grid(row=1, column=1, padx=10, pady=10)

        self.address_label = ttk.Label(self.profile_window, text="Address:")
        self.address_label.grid(row=2, column=0, padx=10, pady=10)
        self.address_label_value = ttk.Label(self.profile_window, text=self.user_data[4])  # Address
        self.address_label_value.grid(row=2, column=1, padx=10, pady=10)

        # Logout button to return to Login Screen
        self.logout_button = ttk.Button(self.profile_window, text="Logout", command=self.logout)
        self.logout_button.grid(row=3, column=0, columnspan=2, pady=10)

    def show_profile_screen(self):
        """Display the profile screen."""
        self.profile_window.deiconify()  # Show the profile window

    def logout(self):
        """Logout and return to the login window."""
        self.profile_window.destroy()  # Close profile window
        self.root.deiconify()  # Show the login window again


# Window 3: Signup Screen
class SignupWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up Window")

        # Create a new Toplevel window for the signup form
        self.signup_window = tk.Toplevel(self.root)
        self.signup_window.title("Sign Up")

        # Signup form labels and entries
        self.username_label = ttk.Label(self.signup_window, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.signup_window)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = ttk.Label(self.signup_window, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.signup_window, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.name_label = ttk.Label(self.signup_window, text="Name:")
        self.name_label.grid(row=2, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.signup_window)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.email_label = ttk.Label(self.signup_window, text="Email:")
        self.email_label.grid(row=3, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(self.signup_window)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)

        self.address_label = ttk.Label(self.signup_window, text="Address:")
        self.address_label.grid(row=4, column=0, padx=10, pady=10)
        self.address_entry = ttk.Entry(self.signup_window)
        self.address_entry.grid(row=4, column=1, padx=10, pady=10)

        self.signup_button = ttk.Button(self.signup_window, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=5, column=0, columnspan=2, pady=10)

    def signup(self):
        """Handle user sign-up."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Save the new user's data to the file
        save_user_data(username, password, name, email, address)

        # Close signup window and show login window
        self.signup_window.destroy()
        self.root.deiconify()  # Show the login window


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
