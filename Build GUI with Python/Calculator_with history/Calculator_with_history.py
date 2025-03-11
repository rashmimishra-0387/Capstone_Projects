"""
Scenario 1: Simple Calculator with History
Objective: Create a two-window application where one window serves as a calculator, and the second window displays the history of calculations.
Requirements:
Window 1: A calculator with buttons for numbers (0-9), basic operators (+, -, *, /), and an =, C button.
Use ttk.Button, ttk.Entry for input/output.
Window 2: A history window that shows previous calculations.
Each time the user clicks =, the result is stored and displayed in this second window.
Use ttk.Label or ttk.Treeview to display the history.
Flow:
The user interacts with Window 1 (calculator) and presses the =, which calculates the result.
The result is sent to Window 2, where it appears in a history list.
Include the ability to clear the history in Window 2 with a "Clear History" button.
"""


import tkinter as tk
from tkinter import ttk

# Window 1: Calculator
class CalculatorWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        # Create the Entry widget for displaying results
        self.result_entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), width=15, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Button grid layout for the calculator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons for the calculator
        for (text, row, col) in buttons:
            button = ttk.Button(self.root, text=text, width=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

        # Open history window when history button is clicked
        self.history_button = ttk.Button(self.root, text="History", command=self.open_history_window)
        self.history_button.grid(row=5, column=0, columnspan=4)

        self.history_window = None
        self.history = []

    def on_button_click(self, button_text):
        """Handle button click events."""
        if button_text == 'C':
            # Clear the entry
            self.result_var.set("")
        elif button_text == '=':
            try:
                # Evaluate the expression and show result, limit to 3 decimal places
                result = eval(self.result_var.get())
                result = round(result, 3)  # Round the result to 3 decimal places
                self.result_var.set(result)
                # Store the calculation in the history
                self.history.append(f"{self.result_var.get()} = {result}")
                if self.history_window:
                    self.history_window.update_history(self.history)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Append the clicked button text to the entry
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

    def open_history_window(self):
        """Open the history window."""
        if not self.history_window:
            self.history_window = HistoryWindow(self, self.history)


# Window 2: History Window
class HistoryWindow:
    def __init__(self, calculator_window, history):
        self.calculator_window = calculator_window
        self.history = history
        self.history_window = tk.Toplevel(self.calculator_window.root)
        self.history_window.title("Calculation History")

        # Create a Treeview to display history
        self.treeview = ttk.Treeview(self.history_window, columns=("Calculation"), show="headings")
        self.treeview.heading("Calculation", text="Calculation")
        self.treeview.pack(expand=True, fill=tk.BOTH)

        self.update_history(history)

        # Button to clear history
        self.clear_button = ttk.Button(self.history_window, text="Clear History", command=self.clear_history)
        self.clear_button.pack(pady=10)

    def update_history(self, history):
        """Update the history Treeview."""
        # Clear the current Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Insert new history items
        for item in history:
            self.treeview.insert("", tk.END, values=(item,))

    def clear_history(self):
        """Clear the history."""
        self.history = []
        self.update_history(self.history)


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    calculator_window = CalculatorWindow(root)
    root.mainloop()
