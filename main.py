from model import DB
from model.Users import Users
from views.login.gui import LoginInterface


if __name__ == "__main__":
    DB.create_conn()
    vol= LoginInterface()


