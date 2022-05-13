from mongoengine import connect, disconnect
from pymongo import MongoClient

from SendMail import sendMail
from model.Users import Users,Sos
import random, string

DB_URI = "mongodb+srv://TaherEmploy:Carvi123@cluster0.efeu7.mongodb.net/carvi?retryWrites=true&w=majority"


def create_conn():
    connect(host=DB_URI)
    print('conn')


def close_conn():
    disconnect()


def login(u_email, u_pwd):
    u=Users.objects(email=u_email)
    if u:
        user = u[0]
        if user.password == u_pwd:
            #Test: if update_user(user,'n','n@gmail.com','354434','nc' ): print('updated')
            return user
    return None


def register(name,email,phone,car):
    user = Users()
    user.name = name
    user.email = email
    user.phone = phone
    user.car = car

    pwd = generate_pwd()
    user.password = pwd
    if user.save():
        sendMail(user.email, "REGISTER", pwd)
        return user

    return False


def add_sos(user: Users, sos: Sos):
    user.sos_contacts.append(sos)

    if user.save():
        return True
    return False


def update_user(user: Users,name=None, email=None, phone=None, car=None):
    if email: user.email = email
    if name: user.name = name
    if phone: user.phone = phone
    if car: user.car = car
    if user.save():
        return True
    return False
    # user.modify(name=name,email=email,phone=phone,car=car)


def delete_user(user: Users):
    user.delete()



def change_pwd(user: Users):
    pwd = generate_pwd()
    user.password = pwd
    if user.save():
        sendMail(user.email, "CHANGE_PASSWORD", pwd)
        return True
    return False


def generate_pwd():
    chars = string.ascii_letters + string.digits
    pwd = ''
    for index in range(10):
        pwd = pwd + random.choice(chars)

    return pwd
