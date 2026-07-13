import tkinter as tk
from tkinter import messagebox
from bmi import calculate_bmi, get_bmi_category

window = tk.Tk()

window.title("BMI Calculator")
window.geometry("400x300")
def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0:
            messagebox.showerror("Invalid Input", "Weight must be greater than 0.")
            return

        if height <= 0:
            messagebox.showerror("Invalid Input", "Height must be greater than 0.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )

heading = tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(window, width=20)
weight_entry.pack(pady=5)

height_label = tk.Label(window, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(window, width=20)
height_entry.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    command=calculate
)
calculate_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
result_label.pack()
window.mainloop()