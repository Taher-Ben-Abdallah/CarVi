from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

from Calls import Calls
from HandCounter import HandCounter
from HandGestures import HandGestures
from HandVolume import HandVolume
from model import Users
from views.parametres.gui import ParametresInterface

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MainInterface():

    def __init__(self, user: Users):
        window = Tk()
        window.geometry("640x480")
        window.configure(bg="#FFFFFF")

        window.title('Tableau de Bord')
        # window.iconphoto(False,PhotoImage(file='./media/window_icon.png'))

        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=480,
            width=640,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            128.0,
            246.0,
            image=image_image_1
        )

        canvas.create_text(
            334.0,
            77.0,
            anchor="nw",
            text="Bienvenue",
            fill="#555555",
            font=("Ubuntu Bold", 40 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        stop_button = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        stop_button.place(
            x=343.0,
            y=165.0,
            width=210.0,
            height=61.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        settings_button = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ParametresInterface(user,window),
            relief="flat"
        )
        settings_button.place(
            x=575.0,
            y=24.0,
            width=30.0,
            height=30.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        start_button = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('start'),  # toggle buttons start and stop
            relief="flat"
        )
        start_button.place(
            x=343.0,
            y=165.0,
            width=210.0,
            height=61.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        volume_button = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: HandVolume(),
            relief="flat"
        )
        volume_button.place(
            x=352.0,
            y=266.0,
            width=190.0,
            height=42.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        gesture_button = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: HandGestures(),
            relief="flat"
        )
        gesture_button.place(
            x=350.0,
            y=324.0,
            width=190.0,
            height=44.0
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        calls_button = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Calls(user.sos_contacts),
            relief="flat"
        )
        calls_button.place(
            x=350.0,
            y=380.0,
            width=190.0,
            height=42.0
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        '''login_button = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        login_button.place(
            x=579.0,
            y=20.0,
            width=35.0,
            height=35.0
        )'''
        window.resizable(False, False)
        window.mainloop()
