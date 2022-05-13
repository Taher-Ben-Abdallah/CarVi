
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import time


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SuccessInterface():
    def __init__(self,msg):
        top = Toplevel()

        top.geometry("360x160")
        top.configure(bg = "#FFFFFF")


        canvas = Canvas(
            top,
            bg = "#FFFFFF",
            height = 160,
            width = 360,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            120.0,
            51.0,
            anchor="nw",
            text="Succes!",
            fill="#777777",
            font=("Ubuntu Bold", 28 * -1)
        )

        canvas.create_text(
            122.0,
            84.0,
            anchor="nw",
            text=msg if msg is not None else "Operation faite avec succés",
            fill="#999999",
            font=("Ubuntu Regular", 16 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            68.0,
            80.0,
            image=image_image_1
        )
        top.mainloop()

