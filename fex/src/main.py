#! python

from elixir import *
from model import *
import datetime

def pop_entite():
    ## SRA la racine
    e = Entite()
    e.codent = "SRA"
    e.nom = "SRA INFORMATIQUE"
    e.typ = 'ROOT'
    session.commit()

    ## Un Client 
    e = Entite()
    e.codent = "CLIENT1"
    e.nom = "CLIENT No 1"
    e.typ = 'CLIENT'
    session.commit()

    ## Un autre client
    e = Entite()
    e.codent = "CLIENT2"
    e.nom = "CLIENT No 2"
    e.typ = 'CLIENT'
    session.commit()

def pop_user():
    SRA = Entite.get_by(codent="SRA")
    ## Admin SRA
    u = User()
    u.codusr = "SRA_ADM1"
    u.name = "Admin SRA"
    u.entite = SRA
    u.IsAdmin = True
    session.commit()
    ## User CLIENT1
    CLI1 = Entite.get_by(codent="CLIENT1")
    u = User()
    u.codusr = "CLI1_ADM"
    u.name = "Admin CLIENT1"
    u.entite = CLI1
    u.IsAdmin = True
    session.commit()
    u = User()
    u.codusr = "CLI1_USR1"
    u.name = "USER1 CLIENT1"
    u.entite = CLI1
    u.IsAdmin = False
    session.commit()
    u = User()
    u.codusr = "CLI1_USR2"
    u.name = "USER2 CLIENT1"
    u.entite = CLI1
    u.IsAdmin = False
    session.commit()
    ## User CLIENT2
    CLI2 = Entite.get_by(codent="CLIENT2")
    u = User()
    u.codusr = "CLI2_ADM"
    u.name = "Admin CLIENT2"
    u.entite = CLI2
    u.IsAdmin = True
    session.commit()
    u = User()
    u.codusr = "CLI2_USR2"
    u.name = "USER2 CLIENT2"
    u.entite = CLI2
    u.IsAdmin = False
    session.commit()

def populate():
    pop_entite()
    pop_user()
    #pop_fex()

setup_all(True)
create_all()

populate()
