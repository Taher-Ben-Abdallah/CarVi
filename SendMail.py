import smtplib


mail_sender = "med.taher.benabdallah@gmail.com"
mail_pwd = "TestTest123"


def sendMail(to , categ , pwd=None):


    if categ == "REGISTER":

        msg = "Bienvenue a votre vehicule,\nvotre mot de passe est: " + pwd
        subj= "Bienvenue a CarVi"
    elif categ == "THEFT":
        msg = "Attention! Une personne inconnue est detectee dans votre vehicule !"
        subj = "Vol!"
    elif categ == "SOS":
        msg = "Alerte! la personne dans la vehicule est en danger !!"
        subj = "SOS !"
    elif categ == "CHANGE_PASSWORD":
        msg = "Vous venez de changer de mot de passe pour votre voiture \nVotre nouveau mot de passe est: "+pwd
        subj = "Changement de mot de passe"

    body = "Subject: {}\n\n{}".format(subj, msg)

    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(mail_sender, mail_pwd)
        smtp.sendmail(mail_sender, to, body)
        smtp.quit()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong....", ex)

