import sqlalchemy as sa

from thepoetrypharmacy_com.data.modelbase import SqlAlchemyBase

class Poem(SqlAlchemyBase):
    __tablename__ = 'poems'

    title = sa.Column(sa.String, primary_key=True)
    author = sa.Column(sa.String)
    date_written = sa.Column(sa.DateTime)
    description = sa.Column(sa.String)
    pf_link = sa.Column(sa.String)

    def __repr__(self) -> str:
        return f'<poem: {self.title} by {self.author}>'
