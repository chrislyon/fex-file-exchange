from elixir import *
import datetime

metadata.bind = "sqlite:///fex.dbf"
metadata.bind.echo = False

class Entite(Entity):
    using_options(tablename=u'ENTITE')
    codent = Field(Unicode(10))
    nom = Field(Unicode(30))
    description = Field(UnicodeText, default=u"" )
    typ = Field(Unicode(10), default=u'CLIENT')
    parent = ManyToOne(u'Entite')
    def __repr__(self):
        return '<Entite : %s : %s : %s>' % (self.codent, self.typ, self.parent)

class User(Entity):
    using_options(tablename=u'USER')
    codusr = Field(Unicode(10))
    name = Field(Unicode(30))
    entite = ManyToOne(u'Entite')
    email = Field(Unicode(20))
    IsAdmin = Field(Boolean, default=False)
    def __repr__(self):
        return '<User : %s : %s : %s>' % (self.codusr, self.entite, self.IsAdmin)

class Fex(Entity):
    using_options(tablename=u'FEX')
    nom = Field(Unicode(30))
    description = Field(UnicodeText)
    status = Field(Unicode(10))
    expediteur = ManyToOne(u'User')
    destinataire = ManyToOne(u'User')
    date_creation = Field(DateTime, default=datetime.datetime.now)
    date_modif = Field(DateTime)
    date_depot = Field(DateTime)
    date_retrait = Field(DateTime)

    def __repr__(self):
        return '<File Exchange %s %s %s %s>' % (self.nom, self.status, self.expediteur, self.destinataire) 

