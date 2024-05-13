import tkinter as tk
from tkinter import messagebox

def calculate_payment():
    try:
        job = job_var.get()
        loan_amount = float(loan_amount_entry.get())
        years = int(years_entry.get())

        if loan_amount <= 0 or years <= 0:
            raise ValueError("Loan amount and years must be positive numbers.")

        #calculate fixed interest based on years
        if years == 1:
            interest_rate = 13.76
        elif years == 3:
            interest_rate = 14.06
        elif years == 5:
            interest_rate = 14.87
        elif years == 7:
            interest_rate = 15.71
        else:
            raise ValueError("Invalid number of years. Please choose 1, 3, 5, or 7 years.")

        interest_in_one_year = loan_amount * (interest_rate / 100)
        total_interest = interest_in_one_year * years
        total_loan = loan_amount + total_interest
        pay_per_month = total_loan / (years * 12)

        result_text = f"Total Interests: {total_interest:.2f}\nTotal Loan: {total_loan:.2f}\nPay per Month: {pay_per_month:.2f}"
        result_label.config(text=result_text)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

def clear_fields():
    loan_amount_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    window.destroy()

#main window
window = tk.Tk()
window.title('Bank Misr - Plan Your Loan')
window.geometry("800x500+400+200")

image_path = 'bmp-logo.png'
image = tk.PhotoImage(file='bmp-logo.png')
image_label = tk.Label(window, image=image)
image_label.pack()


job_var = tk.StringVar()
tk.Label(window, text="Choose your Job:").pack()
tk.OptionMenu(window, job_var, "Doctor", "Engineer", "Teacher").pack()

tk.Label(window, text="Loan Amount:").pack()
loan_amount_entry = tk.Entry(window)
loan_amount_entry.pack(pady=5)

tk.Label(window, text="Number of Years:").pack()
years_entry = tk.Entry(window)
years_entry.pack(pady=5)

#buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate_payment, bg="gold")
calculate_button.pack()

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=exit_app, fg="red")
exit_button.pack(pady=5)


result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()



window.mainloop()
