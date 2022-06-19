"""
    DB entities.
"""

from turtle import title
import typing as t
import json

from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, text
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()
_engine = create_engine('sqlite:///data/app.db')
_session = sessionmaker(bind = _engine)()

class DataBaseEntry():
    def add(self):
        _session.add(self)
        _session.commit()

    @classmethod
    def query_all(cls):
        return _session.query(cls).all()

class FeedItemDB(Base, DataBaseEntry):
    """
        DB feed entity.
    """

    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True, autoincrement='ignore_fk')
    post_id = Column(Integer)
    title = Column(String)
    subtitle = Column(String)
    preview = Column(String)

    def to_json(self) -> t.Dict[str, t.Any]:
        return {
            'id': self.id,
            'post_id': self.post_id,
            'title': self.title,
            'subtitle': self.subtitle,
            'preview': self.preview,
        }

class PostDB(Base, DataBaseEntry):
    """
        DB post entity.
    """

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement='ignore_fk')
    payload = Column(LargeBinary)

    def to_json(self) -> t.Dict[str, t.Any]:
        return {
            'id': self.id,
            'widgets': json.loads(self.payload.decode('utf-8')),
        }

Base.metadata.create_all(_engine)