import sqlalchemy as sa
import sqlalchemy.orm as orm
from thepoetrypharmacy_com.data.modelbase import SqlAlchemyBase
from thepoetrypharmacy_com.data.poem import Poem

class Poet(SqlAlchemyBase):
    __tablename__ = 'poets'

    id = sa.Column(sa.Integer, autoincrement=True)
    name = sa.Column(sa.String, primary_key=True)
    year_born = sa.Column(sa.String, index=True)
    year_died = sa.Column(sa.String, index=True)
    country = sa.Column(sa.String, index=True)
    summary = sa.Column(sa.String)
    pf_link = sa.Column(sa.String)
    poet_image_url = sa.Column(sa.String)
    popularity = sa.Column(sa.Integer, index=True)
    tags = sa.Column(sa.String, index=True)

    poems = orm.relation("Poem", order_by=[
        Poem.title.desc(),
        Poem.date.desc(),
        Poem.tags.desc(),
    ], back_populates='poet')

    def __repr__(self) -> str:
        return f'<poet: {self.name}>'