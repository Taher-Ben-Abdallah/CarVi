import sys
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter.messagebox import askokcancel, WARNING

from model import Users
from model.DB import delete_user
from views.error.gui import ErrorInterface
from views.register import gui
from views.sos.gui import SosContactInterface
from views.success.gui import SuccessInterface
from views.user_data.gui import UserDataInterface

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ParametresInterface():
    def __init__(self,user:Users,window:Tk):

        self.top = Toplevel()

        self.top.geometry("320x340")
        self.top.configure(bg="#FFFFFF")
        self.top.title('Parametres')

        # top.iconphoto(False, PhotoImage(file='media/top_icon.png'))

        canvas = Canvas(
            self.top,
            bg="#FFFFFF",
            height=340,
            width=320,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            74.0,
            51.99999999999997,
            anchor="nw",
            text="Parametres",
            fill="#666666",
            font=("Ubuntu Bold", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"), master=self.top)
        user_data_button = Button(self.top,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_user_data(user),
            relief="flat"
        )
        user_data_button.place(
            x=66.0,
            y=129.99999999999997,
            width=190.0,
            height=42.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"), master=self.top)
        sos_button = Button(self.top,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_sos(user),
            relief="flat"
        )
        sos_button.place(
            x=66.0,
            y=181.99999999999997,
            width=190.0,
            height=42.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"), master=self.top)
        deactivate_button = Button(self.top,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.make_deactivate(user,window),
            relief="flat"
        )
        deactivate_button.place(
            x=66.0,
            y=254.99999999999997,
            width=190.0,
            height=42.0
        )

        canvas.create_rectangle(
            93.0,
            239.99999999999997,
            233.0,
            240.99999999999997,
            fill="#C4C4C4",
            outline="")

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"), master=self.top)
        return_button = Button(self.top,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.top.destroy(),
            relief="flat"
        )
        return_button.place(
            x=18.0,
            y=17.99999999999997,
            width=26.0,
            height=26.0
        )
        self.top.resizable(False, False)
        self.top.mainloop()

    def make_deactivate(self, user: Users,window:Tk):
        # TODO  show interface to confirm
        answer = askokcancel(
            title='Confirmation',
            message='Veuillez confirmer cette operation',
            icon=WARNING)
        if answer:
            #try:
                delete_user(user)
                #SuccessInterface("Utilisateur effacé")
                self.top.destroy()
                window.destroy()
                gui.RegisterInterface()

            #except:
             #   ErrorInterface('Desactivation echouee', 'Impossible de desactiver le compte')



    def open_user_data(self,user:Users):
        UserDataInterface(user)

    def open_sos(self,user):
        SosContactInterface(user)