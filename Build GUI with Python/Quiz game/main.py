import tkinter as tk
from tkinter import messagebox


# Define the questions and answer options
questions = [
    {
        "question": "What is the purpose of the Tkinter library?",
        "options": ["To create GUI applications", "To create web applications", "For database management", "For file handling"],
        "answer": "To create GUI applications"
    },
    {
        "question": "Which widget is used to display text in Tkinter?",
        "options": ["Label", "Entry", "Button", "Listbox"],
        "answer": "Label"
    },
    {
        "question": "Which widget allows user to input text?",
        "options": ["Label", "Text", "Entry", "Button"],
        "answer": "Entry"
    },
    {
        "question": "Which widget is used to create a text area in Tkinter?",
        "options": ["Label", "Text", "Button", "Canvas"],
        "answer": "Text"
    },
    {
        "question": "Which layout manager is used to arrange widgets in rows and columns?",
        "options": ["pack", "grid", "place", "frame"],
        "answer": "grid"
    },
    {
        "question": "Which layout manager allows you to specify exact placement of widgets?",
        "options": ["grid", "pack", "place", "frame"],
        "answer": "place"
    },
    {
        "question": "Which layout manager is used to place widgets one after another in a given space?",
        "options": ["pack", "grid", "place", "canvas"],
        "answer": "pack"
    },
    {
        "question": "How can you display a simple message box in Tkinter?",
        "options": ["messagebox.show()", "messagebox.showinfo()", "messagebox.alert()", "messagebox.warning()"],
        "answer": "messagebox.showinfo()"
    },
    {
        "question": "Which of the following is used to get user input from a dropdown list?",
        "options": ["Spinbox", "OptionMenu", "Button", "Entry"],
        "answer": "OptionMenu"
    },
    {
        "question": "What method is used to get the value of an Entry widget?",
        "options": ["get()", "set()", "value()", "entry()"],
        "answer": "get()"
    },
    {
        "question": "Which widget is used to create radio buttons?",
        "options": ["Checkbutton", "RadioButton", "Button", "Entry"],
        "answer": "RadioButton"
    },
    {
        "question": "Which method is used to add a menu to the main window?",
        "options": ["add()", "menu_add()", "add_cascade()", "add_item()"],
        "answer": "add_cascade()"
    },
    {
        "question": "Which method is used to place widgets in a frame?",
        "options": ["place()", "pack()", "grid()", "add_widget()"],
        "answer": "pack()"
    },
    {
        "question": "Which of the following is the default widget used to display messages?",
        "options": ["Label", "Button", "Canvas", "Message"],
        "answer": "Label"
    },
    {
        "question": "How do you create a frame in Tkinter?",
        "options": ["tk.Frame()", "tk.Widget()", "tk.Label()", "tk.Entry()"],
        "answer": "tk.Frame()"
    },
    {
        "question": "What is the purpose of the `window.attributes('-topmost', 1)` method?",
        "options": ["Keeps the window always on top", "Sets the window size", "Sets window transparency", "None of the above"],
        "answer": "Keeps the window always on top"
    },
    {
        "question": "Which of the following is used to create a menu bar in Tkinter?",
        "options": ["Menu", "Menubar", "menu()", "MenuBar"],
        "answer": "Menu"
    },
    {
        "question": "Which of these widgets is used to display text?",
        "options": ["Text", "Label", "Entry", "Button"],
        "answer": "Text"
    },
    {
        "question": "What is the purpose of `window.geometry()` in Tkinter?",
        "options": ["Sets window size", "Sets window title", "Sets window position", "All of the above"],
        "answer": "Sets window size"
    },
    {
        "question": "Which widget is used to create a checkbox in Tkinter?",
        "options": ["Checkbutton", "RadioButton", "Button", "Entry"],
        "answer": "Checkbutton"
    },
    {
        "question": "Which method is used to set the text of a Label widget?",
        "options": ["set()", "config()", "setText()", "configure()"],
        "answer": "config()"
    },
    {
        "question": "Which method is used to update the Tkinter window with new content?",
        "options": ["update()", "redraw()", "refresh()", "refresh_window()"],
        "answer": "update()"
    },
    {
        "question": "What method is used to show an error message in Tkinter?",
        "options": ["messagebox.showerror()", "messagebox.showinfo()", "messagebox.showwarning()", "messagebox.alert()"],
        "answer": "messagebox.showerror()"
    },
    {
        "question": "Which of these widgets can be used to create a scrollbar?",
        "options": ["Scrollbar", "Listbox", "Text", "Button"],
        "answer": "Scrollbar"
    },
    {
        "question": "How to change the font of a Label widget?",
        "options": ["Label.config(font='Arial 12')", "Label.set(font='Arial 12')", "Label.configure(font='Arial 12')", "Label.font = 'Arial 12'"],
        "answer": "Label.config(font='Arial 12')"
    },
    {
        "question": "Which method is used to display a confirmation dialog in Tkinter?",
        "options": ["messagebox.askquestion()", "messagebox.askyesno()", "messagebox.askokcancel()", "messagebox.confirm()"],
        "answer": "messagebox.askyesno()"
    },
    {
        "question": "Which of the following widgets can be used to create a listbox?",
        "options": ["Listbox", "Canvas", "Frame", "Text"],
        "answer": "Listbox"
    },
    {
        "question": "How do you set the initial value of a Spinbox?",
        "options": ["spinbox.set()", "spinbox.get()", "spinbox.configure()", "spinbox.insert()"],
        "answer": "spinbox.set()"
    },
    {
        "question": "Which widget is used to display a menu bar?",
        "options": ["Menu", "Menubar", "MenuBar", "Frame"],
        "answer": "Menu"
    },
    {
        "question": "Which widget is used to create a text input field?",
        "options": ["Entry", "Label", "Text", "Button"],
        "answer": "Entry"
    }
]

# Define the GUI
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Quiz")
        self.root.geometry("600x500")
        
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", font=('Arial', 16), wraplength=500)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()

        self.option_1 = tk.Radiobutton(self.root, text="", variable=self.options_var, value="Option 1", font=('Arial', 12), command=self.check_answer)
        self.option_1.pack(anchor='w')

        self.option_2 = tk.Radiobutton(self.root, text="", variable=self.options_var, value="Option 2", font=('Arial', 12), command=self.check_answer)
        self.option_2.pack(anchor='w')

        self.option_3 = tk.Radiobutton(self.root, text="", variable=self.options_var, value="Option 3", font=('Arial', 12), command=self.check_answer)
        self.option_3.pack(anchor='w')

        self.option_4 = tk.Radiobutton(self.root, text="", variable=self.options_var, value="Option 4", font=('Arial', 12), command=self.check_answer)
        self.option_4.pack(anchor='w')

        self.next_button = tk.Button(self.root, text="Next", font=('Arial', 14), command=self.next_question)
        self.next_button.pack(pady=20)

        self.update_question()

    def update_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            self.option_1.config(text=question_data["options"][0], value=question_data["options"][0])
            self.option_2.config(text=question_data["options"][1], value=question_data["options"][1])
            self.option_3.config(text=question_data["options"][2], value=question_data["options"][2])
            self.option_4.config(text=question_data["options"][3], value=question_data["options"][3])
        else:
            self.display_score()

    def next_question(self):
        if self.current_question < len(questions):
            self.current_question += 1
            self.update_question()
        else:
            self.display_score()

    def check_answer(self):
        selected_answer = self.options_var.get()
        correct_answer = questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

    def display_score(self):
        messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}")
        self.root.quit()

# Main function to run the quiz
def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
