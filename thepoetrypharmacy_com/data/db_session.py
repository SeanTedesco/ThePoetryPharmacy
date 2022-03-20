import sqlalchemy as sa
import sqlalchemy.orm as orm
from thepoetrypharmacy_com.data.modelbase import SqlAlchemyBase

factory = None 

def global_init(db_file: str):
    global factory
    
    if factory: return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a database (db) file.")

    
    connection_str = 'sqlite:///' + db_file.strip()
    print(f'Connecting to DB with {connection_str}')
    engine = sa.create_engine(connection_str, echo=False)
    factory = orm.sessionmaker(bind=engine)

    import thepoetrypharmacy_com.data.__all_models 
    SqlAlchemyBase.metadata.create_all(engine)
