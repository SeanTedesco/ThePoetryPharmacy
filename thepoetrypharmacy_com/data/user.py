import sqlalchemy as sa
import datetime

from sqlalchemy.sql.expression import null

from data.modelbase import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, index=True, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    def __repr__(self) -> str:
        return f'<poet: {self.name}>'