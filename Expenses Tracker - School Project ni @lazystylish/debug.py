from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, OptionMenu, Listbox, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets")

print(f"Looking for assets in: {Path(__file__).parent / 'assets'}")
