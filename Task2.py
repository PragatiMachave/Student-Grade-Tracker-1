import tkinter as tk
from tkinter import messagebox

class GradeTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Student Grade Tracker")

        # Create input fields
        self.name_label = tk.Label(self.window, text="Student Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        self.subjects = ["Math", "Science", "English", "History", "Geography"]
        self.marks_entries = []
        for i, subject in enumerate(self.subjects):
            label = tk.Label(self.window, text=f"{subject} Marks (out of 100):")
            label.grid(row=i+1, column=0)
            entry = tk.Entry(self.window)
            entry.grid(row=i+1, column=1)
            self.marks_entries.append(entry)

        # Create buttons
        self.calculate_button = tk.Button(self.window, text="Calculate Grades", command=self.calculate_grades)
        self.calculate_button.grid(row=6, column=0, columnspan=2)

        # Create output field
        self.result_label = tk.Label(self.window, text="Results:")
        self.result_label.grid(row=7, column=0)
        self.result_text = tk.Text(self.window, height=10, width=40)
        self.result_text.grid(row=8, column=0, columnspan=2)

    def calculate_grades(self):
        try:
            name = self.name_entry.get()
            results = []

            for i, subject in enumerate(self.subjects):
                marks = float(self.marks_entries[i].get())
                if marks < 0 or marks > 100:
                    messagebox.showerror("Invalid Marks", f"Please enter valid marks for {subject}")
                    return

                if marks >= 80:
                    grade = "A"
                elif marks >= 60:
                    grade = "B"
                elif marks >= 40:
                    grade = "C"
                else:
                    grade = "F"

                result = f"{subject}: {marks} - {grade}"
                if grade == "F":
                    result += " - Fail"
                else:
                    result += " - Pass"
                results.append(result)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Student Name: {name}\n\n" + "\n".join(results))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid marks for all subjects")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    tracker = GradeTracker()
    tracker.run()