
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

from model.DB import add_sos
from model.Users import Users, Sos

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



class SosContactInterface():
    def __init__(self,user:Users):
        self.top = Toplevel()
        self.top.geometry("360x360")
        self.top.configure(bg = "#FFFFFF")

        self.top.title('Contact de Secours')
        #self.top.iconphoto(False,PhotoImage(file='./media/top_icon.png'))

        canvas = Canvas(
            self.top,
            bg = "#FFFFFF",
            height = 360,
            width = 360,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        save_button = Button(self.top,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_contact(user, name_entry.get(), email_entry.get(), phone_entry.get()),
            relief="flat"
        )
        save_button.place(
            x=105.0,
            y=291.0,
            width=156.0,
            height=42.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            187.5,
            198.5,
            image=entry_image_1
        )
        email_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        email_entry.place(
            x=99.5,
            y=185.0,
            width=176.0,
            height=29.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            187.5,
            245.5,
            image=entry_image_2
        )
        phone_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        phone_entry.place(
            x=99.5,
            y=232.0,
            width=176.0,
            height=29.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            187.5,
            152.5,
            image=entry_image_3
        )
        name_entry = Entry(self.top,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        name_entry.place(
            x=99.5,
            y=139.0,
            width=176.0,
            height=29.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        name_icon = canvas.create_image(
            63.0,
            153.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        email_icon = canvas.create_image(
            63.0,
            199.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        phone_icon = canvas.create_image(
            63.0,
            246.0,
            image=image_image_3
        )

        canvas.create_text(
            56.0,
            64.0,
            anchor="nw",
            text="Ajouter un contact",
            fill="#666666",
            font=("Ubuntu Bold", 28 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        return_button = Button(self.top,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.top.destroy(),
            relief="flat"
        )
        return_button.place(
            x=18.0,
            y=18.0,
            width=26.0,
            height=26.0
        )
        self.top.resizable(False, False)
        self.top.mainloop()

    def add_contact(self,user:Users,sos_name, sos_email, sos_phone):
        sos = Sos()
        sos.name = sos_name
        sos.email = sos_email
        sos.phone = sos_phone

        if add_sos(user, sos):
            print('edited')
            #TODO show success msg
            self.top.destroy()
        # TODO show error msg
        print(sos_name, sos_email, sos_phone)
