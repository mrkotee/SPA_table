
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String)
    amount = Column(Float)  # amount in kilograms
    distance = Column(Integer)  # distance in meters

    def __init__(self, date, name, amount, distance):
        self.date = date
        self.name = name
        self.amount = amount
        self.distance = distance


def create_session(user, password, dbname, host, port):
    # engine = create_engine(
    #     f'postgresql+psycopg2://{user}:{password}@/{dbname}?host={host}:{port}')
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    session = sessionmaker(bind=engine)()

    return session


def create_table(dec_base, user, password, dbname, host, port):
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    dec_base.metadata.create_all(engine)
