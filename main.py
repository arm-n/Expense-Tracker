import tkinter as tk
from tkinter import messagebox
import json


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x400")

        self.expenses = self.load_expenses()

        tk.Label(root, text="Expense Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.pack()

        self.clear_button = tk.Button(root, text="Clear Expenses", command=self.clear_expenses)
        self.clear_button.pack()

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        name = self.name_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not name or not amount:
            messagebox.showerror("Error", "Please enter both expense name and amount.")
            return

        try:
            amount = float(amount)  # Ensure the amount is a valid number
        except ValueError:
            messagebox.showerror("Error", "Amount must be a numeric value.")
            return

        self.expenses.append({"name": name, "amount": amount})
        self.save_expenses()
        messagebox.showinfo("Success", "Expense added successfully.")

        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def view_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Expenses", "No expenses recorded.")
            return

        expense_list = "\n".join([f"{exp['name']}: ₹{exp['amount']}" for exp in self.expenses])
        messagebox.showinfo("Expenses", expense_list)

    def clear_expenses(self):
        self.expenses = []
        self.save_expenses()
        messagebox.showinfo("Success", "All expenses cleared.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()