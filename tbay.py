from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ec2-user:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    seller_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    auctioned_items = relationship('Item', backref='seller')
    bidding = relationship('Bid', backref='bidder')
    
class Bid(Base):
    __tablename__ = 'bids'
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
    bid_item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
Base.metadata.create_all(engine)