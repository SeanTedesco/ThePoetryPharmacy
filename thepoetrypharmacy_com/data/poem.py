import sqlalchemy as sa
import datetime

from data.modelbase import SqlAlchemyBase

class Poem(SqlAlchemyBase):
    __tablename__ = 'poems'

    title = sa.Column(sa.String, primary_key=True)
    author = sa.Column(sa.String, index=True)
    date_written = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    description = sa.Column(sa.String)
    pf_link = sa.Column(sa.String)
    tags = sa.Column(sa.String, index=True)

    def __repr__(self) -> str:
        return f'<poem: {self.title} by {self.author}>'
