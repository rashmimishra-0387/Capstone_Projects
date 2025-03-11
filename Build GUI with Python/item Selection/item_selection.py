"""
Item Selection with Information Display
Objective: Design an app where users can select an item from a dropdown list in Window 1, and Window 2 displays detailed information about the selected item.
Requirements:
Window 1:
Use a ttk.Combobox for the user to select an item from a predefined list (e.g., different countries, products, or books).
Add a ttk.Button labeled "Show Details" that opens the second window.
Window 2: Displays detailed information about the selected item, including a description and an image if applicable.
Use ttk.Label to display the description and ttk.Treeview to show additional data about the item (e.g., price, release date).
Include an option to close the details window.

pip install Pillow

"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Predefined data for demonstration
items = {
    "Item 1": {
        "description": "This is a description of Item 1.",
        "data": {
            "Price": "$10.99",
            "Release Date": "2021-06-01"
        },
        "image": "items\bunny.jpg"  # Make sure to replace with an actual image file path
    },
    "Item 2": {
        "description": "This is a description of Item 2.",
        "data": {
            "Price": "$20.99",
            "Release Date": "2020-05-15"
        },
        "image": "items\cat_toy1.jpg"  # Replace with an actual image file path
    },
    "Item 3": {
        "description": "This is a description of Item 3.",
        "data": {
            "Price": "$15.49",
            "Release Date": "2022-01-30"
        },
        "image": "items\dog.jpg"  # Replace with an actual image file path
    }
}

# Main window (Window 1)
class ItemSelectionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Item Selection")

        # Dropdown list with predefined items
        self.item_label = ttk.Label(self.root, text="Select an item:")
        self.item_label.grid(row=0, column=0, padx=10, pady=10)

        self.item_combobox = ttk.Combobox(self.root, values=list(items.keys()), width=40)
        self.item_combobox.grid(row=0, column=1, padx=10, pady=10)

        # Show details button
        self.show_details_button = ttk.Button(self.root, text="Show Details", command=self.show_item_details)
        self.show_details_button.grid(row=1, column=0, columnspan=2, pady=10)

    def show_item_details(self):
        """Open the Item Details window for the selected item."""
        selected_item = self.item_combobox.get().strip()

        if not selected_item or selected_item not in items:
            messagebox.showerror("Selection Error", "Please select a valid item!")
            return

        item_info = items[selected_item]
        ItemDetailsWindow(self.root, selected_item, item_info)

# Item Details Window (Window 2)
class ItemDetailsWindow:
    def __init__(self, root, item_name, item_info):
        self.root = root
        self.item_name = item_name
        self.item_info = item_info

        # Create a new Toplevel window for Item Details
        self.details_window = tk.Toplevel(self.root)
        self.details_window.title(f"Details of {self.item_name}")

        # Display Item Name
        self.name_label = ttk.Label(self.details_window, text=f"Item: {self.item_name}", font=("Helvetica", 16))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        # Display Item Description
        self.description_label = ttk.Label(self.details_window, text=f"Description: {self.item_info['description']}")
        self.description_label.grid(row=1, column=0, padx=10, pady=10)

        # Treeview for additional data (e.g., Price, Release Date)
        self.treeview = ttk.Treeview(self.details_window, columns=("Attribute", "Value"), show="headings")
        self.treeview.grid(row=2, column=0, padx=10, pady=10)

        self.treeview.heading("Attribute", text="Attribute")
        self.treeview.heading("Value", text="Value")

        for attribute, value in self.item_info["data"].items():
            self.treeview.insert("", "end", values=(attribute, value))

        # Display Item Image
        image_path = self.item_info["image"]
        try:
            image = Image.open(image_path)
            image = image.resize((100, 100))  # Resize image to fit the window
            image = ImageTk.PhotoImage(image)
            self.image_label = ttk.Label(self.details_window, image=image)
            self.image_label.grid(row=0, column=1, padx=10, pady=10)
            self.image_label.image = image  # Keep a reference to the image to prevent garbage collection
        except Exception as e:
            self.image_label = ttk.Label(self.details_window, text="Image not found.")
            self.image_label.grid(row=0, column=1, padx=10, pady=10)

        # Close Button
        self.close_button = ttk.Button(self.details_window, text="Close", command=self.details_window.destroy)
        self.close_button.grid(row=3, column=0, columnspan=2, pady=10)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    item_selection_window = ItemSelectionWindow(root)
    root.mainloop()


