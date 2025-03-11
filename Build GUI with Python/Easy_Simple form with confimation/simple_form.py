"""
Simple Form with Confirmation
Objective: Create a two-window app where the first window contains a form for user input and the second window displays the entered information and asks for confirmation.
Requirements:
Window 1 (Form):
Use ttk.Entry for user input fields like Name, Email, Phone Number, etc.
Use ttk.Button labeled "Submit" to submit the form.
Window 2 (Confirmation): After submitting, open a second window displaying all the information entered in the form.
Use ttk.Label to display the submitted data and a ttk.Button for confirming or canceling the submission.
If confirmed, the app could close or proceed to another action (e.g., show a success message).
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Form Window (Window 1)
def create_form_window(root):
    root.title("Simple Form")

    # Create labels and entry fields for user input
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)

    name_entry = ttk.Entry(root, width=40)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = ttk.Label(root, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=10)

    email_entry = ttk.Entry(root, width=40)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    phone_label = ttk.Label(root, text="Phone Number:")
    phone_label.grid(row=2, column=0, padx=10, pady=10)

    phone_entry = ttk.Entry(root, width=40)
    phone_entry.grid(row=2, column=1, padx=10, pady=10)

    # Submit Button
    submit_button = ttk.Button(root, text="Submit", command=lambda: submit_form(root, name_entry, email_entry, phone_entry))
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Submit the form and open the confirmation window
def submit_form(root, name_entry, email_entry, phone_entry):
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    # Check if all fields are filled
    if not name or not email or not phone:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    # Open confirmation window with the entered details
    create_confirmation_window(root, name, email, phone)

# Confirmation Window (Window 2)
def create_confirmation_window(root, name, email, phone):
    # Create a new Toplevel window for confirmation
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmation")

    # Display the submitted data
    name_label = ttk.Label(confirmation_window, text=f"Name: {name}")
    name_label.grid(row=0, column=0, padx=10, pady=10)

    email_label = ttk.Label(confirmation_window, text=f"Email: {email}")
    email_label.grid(row=1, column=0, padx=10, pady=10)

    phone_label = ttk.Label(confirmation_window, text=f"Phone Number: {phone}")
    phone_label.grid(row=2, column=0, padx=10, pady=10)

    # Confirm and Cancel buttons
    confirm_button = ttk.Button(confirmation_window, text="Confirm", command=lambda: confirm_submission(confirmation_window, root))
    confirm_button.grid(row=3, column=0, pady=10)

    cancel_button = ttk.Button(confirmation_window, text="Cancel", command=confirmation_window.destroy)
    cancel_button.grid(row=3, column=1, pady=10)

# Confirm the submission
def confirm_submission(confirmation_window, root):
    messagebox.showinfo("Success", "Form submitted successfully!")
    confirmation_window.destroy()
    root.quit()  # Optionally, close the main window

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    create_form_window(root)
    root.mainloop()
