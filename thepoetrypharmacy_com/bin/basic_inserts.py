import sys

from flask import session

from thepoetrypharmacy_com.data import poem
sys.path.append('../')
import os 
import thepoetrypharmacy_com.data.db_session as db_session
from thepoetrypharmacy_com.data.poet import Poet
from thepoetrypharmacy_com.data.poem import Poem


def insert_poem():
    pt = Poet()
    pt.name = input("Poet's Name: ")
    pt.country = input("Poet's Country at Birth: ")

    pm1 = Poem()
    pm1.title = input("Poem Title: ")
    pm1.description = input("Poem Body: ")
    pt.poems.append(pm1)

    pm2 = Poem()
    pm2.title = input("Poem Title: ")
    pm2.description = input("Poem Body: ")
    pt.poems.append(pm2)

    session = db_session.create_session()
    session.add(pt)
    session.commiti()



def db_init():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..','db', 'pharm.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


def main():
    db_init()
    while True:
        insert_poem()


if __name__ == '__main__':
    main()