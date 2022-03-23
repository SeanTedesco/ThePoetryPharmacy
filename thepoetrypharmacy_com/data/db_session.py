from flask import session
import sqlalchemy as sa
import sqlalchemy.orm as orm
from thepoetrypharmacy_com.data.modelbase import SqlAlchemyBase
from sqlalchemy.orm.session import Session

__factory = None 

def global_init(db_file: str):
    global __factory
    
    if __factory: return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a database (db) file.")

    
    connection_str = 'sqlite:///' + db_file.strip()
    print(f'Connecting to DB with {connection_str}')
    engine = sa.create_engine(connection_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    import thepoetrypharmacy_com.data.__all_models 
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()