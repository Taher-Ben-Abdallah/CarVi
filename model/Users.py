from mongoengine import Document,StringField,EmailField, EmbeddedDocument, EmbeddedDocumentListField

class Sos(EmbeddedDocument):
    name= StringField(max_length=50)
    phone= StringField(max_length=50)
    email= StringField(max_length=50)

class Users(Document):
    email = EmailField(required=True,unique=True)
    name = StringField(max_length=50)
    car = StringField(max_length=50)
    password = StringField(max_length=50)
    phone = StringField(max_length=50)
    sos_contacts = EmbeddedDocumentListField(Sos)

