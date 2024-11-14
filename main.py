import tkinter as tk


def calculate_balance(income, expenses):
    return income + expenses


def on_calculate():
    income = float(entry_income.get())
    expenses = float(entry_expenses.get())
    balance = calculate_balance(income, expenses)
    label_result.config(text=f"баланс1: {balance}")


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Калькулятор финансов")

    tk.Label(app, text="Доходы:").pack()
    entry_income = tk.Entry(app)
    entry_income.pack()

    tk.Label(app, text="Расходы:").pack()
    entry_expenses = tk.Entry(app)
    entry_expenses.pack()

    tk.Button(app, text="Подсчитать", command=on_calculate).pack()
    label_result = tk.Label(app, text="")
    label_result.pack()

    app.mainloop()
