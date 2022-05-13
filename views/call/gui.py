
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

from model.Users import Sos

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CallerInterface():
    def __init__(self,name=None,phone=None,email=None):
        self.window = Toplevel()
        self.window.geometry("400x240")
        self.window.configure(bg = "#FFFFFF")

        self.window.title('Appel')
        #self.window.iconphoto(False,PhotoImage(file='./media/window_icon.png'))

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 240,
            width = 400,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            93.0,
            19.0,
            anchor="nw",
            text="Appel en cours ...",
            fill="#6C88B2",
            font=("Ubuntu Bold", 24 * -1)
        )

        canvas.create_text(
            157.0,
            88.0,
            anchor="nw",
            text=name if name is not None else "Unknown",
            fill="#777777",
            font=("Ubuntu Bold", 20 * -1)
        )

        canvas.create_text(
            157.0,
            118.0,
            anchor="nw",
            text=phone if phone is not None else "Unknown Phone number",
            fill="#666666",
            font=("Ubuntu Regular", 16 * -1)
        )

        canvas.create_text(
            157.0,
            138.0,
            anchor="nw",
            text=email if email is not None else "Unknown email",
            fill="#888888",
            font=("Ubuntu Regular", 14 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"),master=self.window)
        image_1 = canvas.create_image(
            81.0,
            124.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"), master=self.window)
        button_1 = Button(self.window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.destroy(),
            relief="flat"
        )
        button_1.image = button_image_1
        button_1.place(
            x=240.0,
            y=190.0,
            width=138.0,
            height=31.0
        )


        self.window.resizable(False, False)
        self.window.mainloop()
