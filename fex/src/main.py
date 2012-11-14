#! python

from elixir import *
from model import *
import datetime

class Hub(object):
    def __init__(self, name):
        self.name  = name

    def pop_entite(self):
        ## SRA la racine
        e = Entite()
        e.codent = u"SRA"
        e.nom = u"SRA INFORMATIQUE"
        e.typ = u'ROOT'
        session.commit()

        ## Un Client 
        e = Entite()
        e.codent = u"CLIENT1"
        e.nom = u"CLIENT No 1"
        e.typ = u'CLIENT'
        session.commit()

        ## Un autre client
        e = Entite()
        e.codent = u"CLIENT2"
        e.nom = u"CLIENT No 2"
        e.typ = u'CLIENT'
        session.commit()

    def pop_user(self):
        SRA = Entite.get_by(codent=u"SRA")
        ## Admin SRA
        u = User()
        u.codusr = u"SRA_ADM1"
        u.name = u"Admin SRA"
        u.entite = SRA
        u.IsAdmin = True
        session.commit()
        ## User SRA
        u = User()
        u.codusr = u"SRA_USR1"
        u.name = u"USER SRA"
        u.entite = SRA
        u.IsAdmin = False
        session.commit()
        ## User CLIENT1
        CLI1 = Entite.get_by(codent=u"CLIENT1")
        u = User()
        u.codusr = u"CLI1_ADM"
        u.name = u"Admin CLIENT1"
        u.entite = CLI1
        u.IsAdmin = True
        session.commit()
        u = User()
        u.codusr = u"CLI1_USR1"
        u.name = u"USER1 CLIENT1"
        u.entite = CLI1
        u.IsAdmin = False
        session.commit()
        u = User()
        u.codusr = u"CLI1_USR2"
        u.name = u"USER2 CLIENT1"
        u.entite = CLI1
        u.IsAdmin = False
        session.commit()
        ## User CLIENT2
        CLI2 = Entite.get_by(codent=u"CLIENT2")
        u = User()
        u.codusr = u"CLI2_ADM"
        u.name = u"Admin CLIENT2"
        u.entite = CLI2
        u.IsAdmin = True
        session.commit()
        u = User()
        u.codusr = u"CLI2_USR1"
        u.name = u"USER2 CLIENT2"
        u.entite = CLI2
        u.IsAdmin = False
        session.commit()

    def pop_fex(self):
        f = Fex()
        f.nom = u"FEX1"
        f.description = u"1er echange de fichier"
        f.status = u"CREE"
        f.expediteur = User.get_by(codusr=u'SRA_USR1')
        f.destinataire = User.get_by(codusr=u'CLI1_USR1')
        session.commit()

        f = Fex()
        f.nom = u"FEX2"
        f.description = u"2eme echange de fichier"
        f.status = u"CREE"
        f.expediteur = User.get_by(codusr=u'CLI2_USR1')
        f.destinataire = User.get_by(codusr=u'SRA_USR1')
        session.commit()

    def populate(self):
        self.pop_entite()
        self.pop_user()
        self.pop_fex()

    def init_base(self):
        setup_all(True)
        create_all()
        self.populate()

def test():
    H = Hub('HUB1')
    H.init_base()


if __name__ == '__main__':
    test()
