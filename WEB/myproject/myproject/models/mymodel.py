#описание таблиц базы данных#
from sqlalchemy import (
    Column,
    Index,
    Integer,
	Text,
	ForeignKey,
    
)

from .meta import Base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    relationship,
    scoped_session,
    sessionmaker,
    )

from pyramid.security import (
    Allow,
    Everyone,
    )


from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(Text, primary_key=True)

    def __repr__(self):
        return self.name or ''
		
class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    name = Column(Text, primary_key=True)
    info = Column(Text)
    parent_id = Column(Integer, ForeignKey(id))
    parent_collection = relationship("Collection", remote_side="Collection.id")

    def __repr__(self):
        return self.name or ''

class Book(Base):
	__tablename__ = 'book'
	author = Column(Text, primary_key=True)
	title = Column(Text, primary_key=True)
	year = Column(Integer) 	
	collection_id = Column(Integer,ForeignKey('collection.id'))
	collection = relationship("Collection", backref='book')
        def __repr__(self):
            return self.author + ' - ' + self.title or ''


class Film(Base):
	__tablename__ = 'film'
	title = Column(Text, primary_key=True)
	year = Column(Integer)		
	collection = relationship("Collection", backref='film')
        def __repr__(self):
            return self.author + ' - ' + self.title or ''
			
class History(Base):
	__tablename__ = 'history'
	title = Column(Text, primary_key=True)
	data = Column(Integer)		
        def __repr__(self):
            return self.author + ' - ' + self.title or ''			

#права для пользователей			
class Access(object):
    __acl__ = [ (Allow, 'group:editors', ('pyramid_sacrud_home', 'pyramid_sacrud_create', 'pyramid_sacrud_update', 'pyramid_sacrud_delete', 'pyramid_sacrud_list')),]
    def __init__(self, request):
        pass			



