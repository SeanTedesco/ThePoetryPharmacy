import json
import os
from re import U
import sys
import time
from typing import List, Optional, Dict
from flask import session
import progressbar
from dateutil.parser import parse

from thepoetrypharmacy_com.data import poet

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from thepoetrypharmacy_com.data import db_session
from thepoetrypharmacy_com.data.poem import Poem
from thepoetrypharmacy_com.data.poet import Poet
from thepoetrypharmacy_com.data.user import User

def do_summary():
    pass

def do_import_poems():
    pass

def do_import_poets():
    pass

def do_find_poets(file_data: List[Dict]) -> List[str]:
    imported = set()
    print('Importing Poets...', flush=True)
    with progressbar.ProgressBar(max_value=len(file_data)) as bar:
        for idx, entry in enumerate(file_data):
            name = entry.get('author')
            imported.add(name)
            bar.update(idx)

            session = db_session.create_session()
            poet = Poet()
            poet.name = name
            session.add(poet)
            session.commit(poet)
    return list(imported)

def do_load_files(data_file: str) -> List[Dict]:

    path_name = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + '/' + data_file
    print('Loading data from: ' + path_name, flush=True)

    with open(path_name, 'r') as json_file:
        data = list()
        for json_str in json_file:
            result = json.loads(json_str)
            data.append(result)
    return data

def init_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        '..',
        'db',
        'pharm.sqlite'
    )
    db_session.global_init(db_file)

def main():
    init_db()
    session = db_session.create_session()
    user_count = session.query(User).count()
    session.close()
    if user_count == 0:
        file_data = do_load_files('poems.jsonl')
        poets = do_find_poets(file_data)
        print(poets)

        do_import_poets(poets)
        do_import_poems(file_data, poets)
    
    do_summary()

if __name__ == '__main__':
    main()