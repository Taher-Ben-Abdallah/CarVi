from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from model.DB import register
from views.error.gui import ErrorInterface
from views import login
from views.main import gui

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class RegisterInterface():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x400")
        self.window.configure(bg="#FFFFFF")

        self.window.title('Register')
        self.window.iconphoto(False, PhotoImage(file='./media/window_icon.png'))

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=400,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            106.99999999999997,
            33.0,
            anchor="nw",
            text="CarVi",
            fill="#4F95D6",
            font=("Ubuntu Bold", 46 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            196.49999999999997,
            138.5,
            image=entry_image_1
        )
        user_entry = Entry(
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        user_entry.place(
            x=108.49999999999997,
            y=125.0,
            width=176.0,
            height=29.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            196.49999999999997,
            187.5,
            image=entry_image_2
        )
        email_entry = Entry(
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        email_entry.place(
            x=108.49999999999997,
            y=174.0,
            width=176.0,
            height=29.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            195.49999999999997,
            236.5,
            image=entry_image_3
        )
        phone_entry = Entry(
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        phone_entry.place(
            x=107.49999999999997,
            y=223.0,
            width=176.0,
            height=29.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            196.49999999999997,
            285.5,
            image=entry_image_4
        )
        car_entry = Entry(
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        car_entry.place(
            x=108.49999999999997,
            y=272.0,
            width=176.0,
            height=29.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(self.window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.make_register(user_entry.get(), email_entry.get(), phone_entry.get(), car_entry.get()),
            relief="flat"
        )
        button_1.place(
            x=183.99999999999997,
            y=330.0,
            width=116.0,
            height=36.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        to_login_button = Button(self.window,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.send_to_login(),
            relief="flat"
        )
        to_login_button.place(
            x=270.0,
            y=42.0,
            width=33.0,
            height=33.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        car_icon = canvas.create_image(
            65.99999999999997,
            286.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        email_icon = canvas.create_image(
            66.99999999999997,
            188.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        user_icon = canvas.create_image(
            65.99999999999997,
            138.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        phone_icon = canvas.create_image(
            65.99999999999997,
            237.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            476.0,
            200.0,
            image=image_image_5
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def make_register(self, user, email, phone, car):
        user= register(user , email , phone , car)
        if user is not False:
            self.window.destroy()
            gui.MainInterface(user)
        else:
            ErrorInterface("Register Error","Inscription echouée")

    def send_to_login(self):
        self.window.destroy()
        login.gui.LoginInterface()