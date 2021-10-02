import sqlalchemy as sa
import datetime

from data.modelbase import SqlAlchemyBase

class Poet(SqlAlchemyBase):
    __tablename__ = 'poets'

    name = sa.Column(sa.String, primary_key=True)
    year_born = sa.Column(sa.String, index=True)
    year_died = sa.Column(sa.String, index=True)
    country = sa.Column(sa.String, index=True)
    summary = sa.Column(sa.String)
    pf_link = sa.Column(sa.String)
    poet_image_url = sa.Column(sa.String)

    def __repr__(self) -> str:
        return f'<poet: {self.name}>'