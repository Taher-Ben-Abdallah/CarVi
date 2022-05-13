
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

from model.DB import login
from views.error.gui import ErrorInterface
from views.main.gui import MainInterface
from views.register import gui

'''TODO ###########"
LOGIN USER PASSING TO MAIN FRAME OR CHECK HOW TO MAKE USER DATA SHARED FOR OTHER MODULES
##############################
'''


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginInterface():

    def __init__(self):
        self.window = Tk()

        self.window.geometry("420x280")
        self.window.configure(bg = "#FFFFFF")

        self.window.title('Login')
        self.window.iconphoto(True,PhotoImage(file='./media/window_icon.png'))


        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 280,
            width = 420,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            149.0,
            27.0,
            anchor="nw",
            text="CarVi",
            fill="#4F95D6",
            font=("Ubuntu Bold", 38 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            220.5,
            125.5,
            image=entry_image_1
        )
        email_entry = Entry(
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        email_entry.place(
            x=132.5,
            y=112.0,
            width=176.0,
            height=29.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            220.5,
            174.5,
            image=entry_image_2
        )
        pwd_entry = Entry(
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            show="•",
            width=10
        )
        pwd_entry.place(
            x=132.5,
            y=161.0,
            width=176.0,
            height=29.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        login_button = Button(self.window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.make_login(email_entry.get(),pwd_entry.get()),
            relief="flat"
        )
        login_button.place(
            x=154.0,
            y=218.0,
            width=124.0,
            height=34.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        register_button = Button(self.window,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.send_to_reg(),
            relief="flat"
        )
        register_button.place(
            x=286.0,
            y=214.0,
            width=38.0,
            height=38.0
        )


        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        email_icon = canvas.create_image(
            91.0,
            125.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        pwd_icon = canvas.create_image(
            91.0,
            174.0,
            image=image_image_2
        )

        self.window.resizable(False, False)

        self.window.mainloop()

    def send_to_reg(self):
        self.window.destroy()
        gui.RegisterInterface()

    def make_login(self,email, pwd):
        user = login(email, pwd)
        if user is None:
            ErrorInterface('Login impossible', 'Mot de passe ou Email incorrectes')
        else:

            self.window.destroy()
            MainInterface(user)



