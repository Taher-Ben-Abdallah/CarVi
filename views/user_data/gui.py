from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

from model import Users
from model.DB import change_pwd, update_user
from views.error.gui import ErrorInterface
from views.success.gui import SuccessInterface

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class UserDataInterface():
    def __init__(self, user: Users):
        self.user = user
        self.top = Toplevel()

        self.top.geometry("380x450")
        self.top.configure(bg="#FFFFFF")

        canvas = Canvas(
            self.top,
            bg="#FFFFFF",
            height=450,
            width=380,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        save_button = Button(self.top,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.make_update(name_entry.get(), email_entry.get(), phone_entry.get(), car_entry.get()),
            relief="flat"
        )
        save_button.place(
            x=108.99999999999997,
            y=367.0,
            width=174.0,
            height=44.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry.png"))
        entry_bg_4 = canvas.create_image(
            200.49999999999997,
            179.5,
            image=entry_image_4
        )
        name_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        name_entry.place(
            x=112.49999999999997,
            y=166.0,
            width=176.0,
            height=29.0
        )
        name_entry.insert(0,user.name)


        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry.png"))
        entry_bg_1 = canvas.create_image(
            199.49999999999997,
            226.5,
            image=entry_image_1
        )
        email_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        email_entry.place(
            x=111.49999999999997,
            y=213.0,
            width=176.0,
            height=29.0
        )
        email_entry.insert(0,user.email)


        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry.png"))
        entry_bg_2 = canvas.create_image(
            200.49999999999997,
            273.5,
            image=entry_image_2
        )
        phone_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        phone_entry.place(
            x=112.49999999999997,
            y=260.0,
            width=176.0,
            height=29.0
        )
        phone_entry.insert(0,user.phone)


        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry.png"))
        entry_bg_3 = canvas.create_image(
            200.49999999999997,
            320.5,
            image=entry_image_3
        )
        car_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        car_entry.place(
            x=112.49999999999997,
            y=307.0,
            width=176.0,
            height=29.0
        )
        car_entry.insert(0,user.car)


        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        name_icon = canvas.create_image(
            75.99999999999997,
            180.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        email_icon = canvas.create_image(
            74.99999999999997,
            227.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        phone_icon = canvas.create_image(
            76.99999999999997,
            275.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        car_icon = canvas.create_image(
            77.99999999999997,
            322.0,
            image=image_image_4
        )

        canvas.create_text(
            64.0,
            92.0,
            anchor="nw",
            text="Donnees Utilisateur",
            fill="#666666",
            font=("Ubuntu Bold", 26 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        changepass_button = Button(self.top,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.make_new_pass(),
            relief="flat"
        )
        changepass_button.place(
            x=241.99999999999997,
            y=25.0,
            width=115.20001220703125,
            height=28.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(self.top,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.top.destroy(),
            relief="flat"
        )
        button_3.place(
            x=24.99999999999997,
            y=26.0,
            width=26.0,
            height=26.0
        )
        self.top.resizable(False, False)
        self.top.mainloop()

    def make_update(self, name, email, phone, car):
        if update_user(self.user, name, email, phone, car):
            SuccessInterface("Donnees utilisateur changes")
            self.top.destroy()
        else:
            ErrorInterface("Echec de modification", "La modification n'est pas effectuee")
        print(name, email, phone, car)

    def make_new_pass(self):
        if change_pwd(self.user):
            SuccessInterface("Mot de passe changé,\nconsultez votre email")
            self.top.destroy()
        else:
            ErrorInterface("Echec de modification","La modification n'est pas effectuee")