from enum import auto
import sqlalchemy as sa
import datetime
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase

class Poem(SqlAlchemyBase):
    __tablename__ = 'poems'

    id = sa.Column(sa.Integer, autoincrement=True)
    title = sa.Column(sa.String, primary_key=True)
    author = sa.Column(sa.String, index=True)
    date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    description = sa.Column(sa.String)
    pf_link = sa.Column(sa.String)
    tags = sa.Column(sa.String, index=True)
    popularity = sa.Column(sa.Integer, index=True)

    poet_id = sa.Column(sa.Integer, sa.ForeignKey("poets.id"))
    poet = orm.relation("Poet")

    def __repr__(self) -> str:
        return f'<poem: {self.title} by {self.author}>'
