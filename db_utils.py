from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from config import DB_URL

def get_engine():
    return create_engine(DB_URL)

def init_db(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
