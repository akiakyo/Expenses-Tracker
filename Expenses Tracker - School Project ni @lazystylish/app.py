from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, OptionMenu, Listbox, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")

def newWindow():
    global transaction_id
    transaction_id = 1
    income = 0
    expenses = 0
    balance = 0
    def relative_to_assets(path: str) -> Path:
        return Path(__file__).parent / "assets" / path

    # Initialize main window
    window = Tk()
    window.geometry("800x700")  
    window.configure(bg="#FFFFFF")

    # Global variables for finances
    income = 0
    expenses = 0
    balance = income - expenses
    transactions = []  # Store transactions as a list of dictionaries
    transaction_id = 1  # Start with ID 1

    # Function to update totals
    def update_totals():
        global income, expenses, balance
        income = sum(t["Amount"] for t in transactions if t["Type"] == "Income")
        expenses = sum(t["Amount"] for t in transactions if t["Type"] == "Expense")
        balance = income - expenses

        canvas.itemconfig(income_text, text=f"${income:,.2f}")
        canvas.itemconfig(expenses_text, text=f"${expenses:,.2f}")
        canvas.itemconfig(balance_text, text=f"${balance:,.2f}")


    def delete_transaction():
        global transaction_id
        try:
            delete_id = int(delete_entry.get())
            for idx, transaction in enumerate(transactions):
                if transaction["ID"] == delete_id:
                    transactions.pop(idx)
                    transaction_listbox.delete(idx + 1)  # Adjusted to delete the correct entry
                    update_totals()

                    # Optionally renumber the remaining transactions to avoid gaps in IDs
                    for i, trans in enumerate(transactions):
                        trans["ID"] = i + 1  # Renumber remaining transactions

                    print(f"Transaction ID {delete_id} deleted.")
                    return
            print(f"Transaction ID {delete_id} not found.")
        except ValueError:
            print("Invalid ID. Please enter a valid number.")

    def reset_all():
        global income, expenses, balance, transactions, transaction_id
        income = 0
        expenses = 0
        balance = 0
        transactions = []
        transaction_id = 1
        transaction_listbox.delete(0, END)
        # Re-add headers
        transaction_listbox.insert(END, "ID    | Category       | Amount       | Type        | Date")
        print("All data reset.")
        update_totals()

    def submit_handler():
        global transaction_id  # Declare transaction_id as global to modify it inside this function
        try:
            transaction_amt = float(entry_2.get())  # Get transaction amount from the entry widget
            transaction_type = transaction_type_var.get()  # Get transaction type (Income/Expense)
            transaction_date = entry_date.get()  # Get transaction date
            category = entry_1.get()  # Get category for the transaction

            if not transaction_date or not category:
                print("Category and Date are required!")
                return

            # Add transaction to the list of transactions
            transactions.append({
                "ID": transaction_id,
                "Category": category,
                "Amount": transaction_amt,
                "Type": transaction_type,
                "Date": transaction_date
            })

            # Update the display (totals)
            update_totals()

            # Add transaction to the Listbox with a formatted display
            transaction_listbox.insert(
                END,
                f"{transaction_id:<5} | {category:<15} | ${transaction_amt:<10.2f} | {transaction_type:<10} | {transaction_date}"
            )
            
            # Increment the transaction_id for the next transaction
            transaction_id += 1

            print(f"Transaction added: {transaction_type} of ${transaction_amt:.2f} in category '{category}' on {transaction_date}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


    # Canvas setup
    canvas = Canvas(
        window,
        bg="#0d0e16",
        height=700,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_rectangle(0.0, 0.0, 800.0, 85.0, fill="#11114E", outline="")

    canvas.create_text(
        34.0, 17.0, anchor="nw",
        text="Hello, lazy",
        fill="#FFFFFF",
        font=("MontserratRoman Bold", 32 * -1)
    )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(192.0, 146.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(358.0, 229.0, image=image_image_2)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(523.0, 146.0, image=image_image_3)

    # Income, balance, and expenses labels and values
    canvas.create_text(
        57.0, 122.0, anchor="nw",
        text="Income",
        fill="#5F4500",
        font=("MontserratRoman Bold", 12 * -1)
    )

    canvas.create_text(
        57.0, 205.0, anchor="nw",
        text="Balance",
        fill="#0A4A00",
        font=("MontserratRoman Bold", 12 * -1)
    )

    canvas.create_text(
        388.0, 122.0, anchor="nw",
        text="Expenses",
        fill="#660000",
        font=("MontserratRoman Bold", 12 * -1)
    )

    income_text = canvas.create_text(
        57.0, 139.0, anchor="nw",
        text=f"${income:,.2f}",
        fill="#5F4500",
        font=("MontserratRoman Bold", 24 * -1)
    )

    balance_text = canvas.create_text(
        57.0, 222.0, anchor="nw",
        text=f"${balance:,.2f}",
        fill="#0A4A00",
        font=("MontserratRoman Bold", 24 * -1)
    )

    expenses_text = canvas.create_text(
        388.0, 139.0, anchor="nw",
        text=f"${expenses:,.2f}",
        fill="#660000",
        font=("MontserratRoman Bold", 24 * -1)
    )

    # Labels and fields for adding transactions
    canvas.create_text(36.0, 285.0, anchor="nw", text="Add Transaction", fill="#fff", font=("MontserratRoman Bold", 16 * -1))
    canvas.create_text(36.0, 317.0, anchor="nw", text="Category :", fill="#fff", font=("MontserratRoman Bold", 12 * -1))
    canvas.create_text(37.0, 392.0, anchor="nw", text="Amount ($)", fill="#fff", font=("MontserratRoman Bold", 12 * -1))
    canvas.create_text(37.0, 467.0, anchor="nw", text="Type of Transaction :", fill="#fff", font=("MontserratRoman Bold", 12 * -1))
    canvas.create_text(37.0, 542.0, anchor="nw", text="Date :", fill="#fff", font=("MontserratRoman Bold", 12 * -1))
    # Entry fields
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(215.5, 362.0, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#E3E3E3", fg="#000716", highlightthickness=0)
    entry_1.place(x=51.0, y=343.0, width=329.0, height=36.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(215.5, 437.0, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#E3E3E3", fg="#000716", highlightthickness=0)
    entry_2.place(x=51.0, y=418.0, width=329.0, height=36.0)

    transaction_type_var = StringVar(value="Income")
    transaction_type_dropdown = OptionMenu(window, transaction_type_var, "Income", "Expense")
    transaction_type_dropdown.place(x=51.0, y=493.0, width=329.0, height=36.0)

    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(215.5, 587.0, image=entry_image_4)
    entry_date = Entry(bd=0, bg="#E3E3E3", fg="#000716", highlightthickness=0)
    entry_date.place(x=51.0, y=568.0, width=329.0, height=36.0)

    # Submit button
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,bg='#0d0e16',
        command=submit_handler,
        relief="flat"
    )
    button_1.place(x=37.0, y=640.0, width=358.0, height=53.0)

    # Reset button
    reset_button = Button(
        text="Reset All", bg="#FFA500", fg="#FFFFFF", relief="flat", command=reset_all
    )

    reset_button.place(x=600, y=580, width=80, height=30)

    # Transaction listbox
    transaction_listbox = Listbox(window, bg="#FFFFFF", fg="#000000", font=("MontserratRoman", 10), height=15, width=50)
    transaction_listbox.place(x=420, y=300)

    # Add headers inside the listbox
    transaction_listbox.insert(END, "ID    | Category       | Amount       | Type        | Date")

    # Delete transaction
    delete_entry = Entry(bd=0, bg="#E3E3E3", fg="#000716", highlightthickness=0)
    delete_entry.place(x=420, y=580, width=100, height=30)

    delete_button = Button(
        text="Delete", command=delete_transaction, bg="#FF0000", fg="#FFFFFF", relief="flat"
    )
    delete_button.place(x=530, y=580, width=60, height=30)

    # Label for Transaction ID to delete
    canvas.create_text(
        420, 560, anchor="nw", text="Transaction ID :", fill="#002689", font=("MontserratRoman Bold", 12 * -1)
    )

    window.resizable(False, False)
    window.mainloop()
