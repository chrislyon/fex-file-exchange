from elixir import *
import datetime

metadata.bind = "sqlite:///fex.dbf"
metadata.bind.echo = True

class Entite(Entity):
    using_options(tablename='ENTITE')
    codent = Field(Unicode(10))
    nom = Field(Unicode(30))
    description = Field(UnicodeText, default=u"" )
    typ = Field(Unicode(10), default='CLIENT')

class User(Entity):
    using_options(tablename='USER')
    codusr = Field(Unicode(10))
    name = Field(Unicode(30))
    entite = ManyToOne('Entite')
    email = Field(Unicode(20))
    IsAdmin = Field(Boolean, default=False)

class Fex(Entity):
    using_options(tablename='FEX')
    nom = Field(Unicode(30))
    description = Field(UnicodeText)
    status = Field(Unicode(10))
    emetteur = ManyToOne('User')
    destinataire = ManyToOne('User')
    date_creation = Field(DateTime, default=datetime.datetime.now)
    date_modif = Field(DateTime)
    date_depot = Field(DateTime)
    date_reception = Field(DateTime)

def __repr__(self):
    return '<File Exchange %s %s>' % (self.nom, self.status)

