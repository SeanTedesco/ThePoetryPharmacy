import sys

from thepoetrypharmacy_com.data import poem
sys.path.append('../')
import os 
import thepoetrypharmacy_com.data.db_session as db_session
from thepoetrypharmacy_com.data.poem import Poem

def main():
    db_init()
    while True:
        insert_poem()

def insert_poem():
    p = Poem()

def db_init():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..','db', 'pharm.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)

if __name__ == '__main__':
    main()