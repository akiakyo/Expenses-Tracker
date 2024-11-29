
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x700")#canvas should be same size
window.configure(bg = "#FFFFFF")

expenses = 1400

def submit_handler():
    global expenses
    new_expense_amt = float(entry_2.get())
    expenses += new_expense_amt
    canvas.itemconfig(tagOrId=expenses_text, text=f"${expenses}")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    85.0,
    fill="#002689",
    outline="")

canvas.create_text(
    34.0,
    17.0,
    anchor="nw",
    text="Budget Tracker",
    fill="#FFFFFF",
    font=("MontserratRoman Bold", 32 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    192.0,
    146.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    358.0,
    229.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    523.0,
    146.0,
    image=image_image_3
)

canvas.create_text(
    57.0,
    122.0,
    anchor="nw",
    text="Income",
    fill="#5F4500",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text(
    57.0,
    205.0,
    anchor="nw",
    text="Balance",
    fill="#0A4A00",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text(
    388.0,
    122.0,
    anchor="nw",
    text="Expenses",
    fill="#660000",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text(
    57.0,
    139.0,
    anchor="nw",
    text="$5,689",
    fill="#5F4500",
    font=("MontserratRoman Bold", 24 * -1)
)

canvas.create_text(
    57.0,
    222.0,
    anchor="nw",
    text="$4,289",
    fill="#0A4A00",
    font=("MontserratRoman Bold", 24 * -1)
)

expenses_text = canvas.create_text(
    388.0,
    139.0,
    anchor="nw",
    text="$1,400",
    fill="#660000",
    font=("MontserratRoman Bold", 24 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    534.0,
    600.0,
    image=image_image_4
)

canvas.create_text( # Add Transaction
    36.0,
    285.0,
    anchor="nw",
    text="Add Transaction",
    fill="#002689",
    font=("MontserratRoman Bold", 16 * -1)
)

canvas.create_text( # Cathegory
    36.0,
    317.0,
    anchor="nw",
    text="Cathegory :",
    fill="#002689",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text( #Amount ($)
    37.0,
    392.0,
    anchor="nw",
    text="Amount ($)",
    fill="#002689",
    font=("MontserratRoman Bold", 12 * -1)
)
canvas.create_text( #type of transaction LABEL
    37.0,
    467.0,
    anchor="nw",
    text="Type of Transaction :",
    fill="#002689",
    font=("MontserratRoman Bold", 12 * -1)
)
canvas.create_text( #date
    37.0,
    542.0,
    anchor="nw",
    text="Date :",
    fill="#002689",
    font=("MontserratRoman Bold", 12 * -1)
)


entry_image_1 = PhotoImage(
file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    214.5,
    362.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E3E3E3",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=50.0,
    y=343.0,
    width=329.0,
    height=36.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    215.5,
    437.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E3E3E3",
    fg="#000716",
    highlightthickness=0
)

entry_2.place(
    x=51.0,
    y=418.0,  # Adjusted to match the visual alignment
    width=329.0,
    height=36.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    216.5,
    512.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E3E3E3",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=51.0,
    y=493.0,
    width=329.0,
    height=36.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    215.5,
    587.0,
    image=entry_image_3
)
entry_4 = Entry(
    bd=0,
    bg="#E3E3E3",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=51.0,
    y=568.0,
    width=329.0,
    height=36.0
)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit_handler,
    relief="flat"
    
    
    
)
button_1.place(
    x=37.0,
    y=640.0,
    width=358.0,
    height=53.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    660.0,
    43.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
