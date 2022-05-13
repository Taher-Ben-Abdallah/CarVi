
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ErrorInterface():
    def __init__(self,type=None,detail=None):

        self.window = Tk()

        self.window.geometry("360x160")
        self.window.configure(bg = "#FFFFFF")

        self.window.title('Erreur')
        #self.window.iconphoto(False, PhotoImage(file='./media/window_icon.png'))

        canvas = Canvas(
            self.window,
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
            48.0,
            anchor="nw",
            text=type if type is not None else "Erreur!",
            fill="#777777",
            font=("Ubuntu Bold", 21 * -1)
        )

        canvas.create_text(
            125.0,
            86.0,
            anchor="nw",
            text=detail if detail is not None else "Erreur!",
            fill="#999999",
            font=("Ubuntu Regular", 14 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"),master=self.window)
        image_1 = canvas.create_image(
            71.0,
            80.0,
            image=image_image_1
        )
        self.window.resizable(False, False)
        self.window.mainloop()
