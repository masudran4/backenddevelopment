from sqlalchemy import Column, Integer, ForeignKey

from database import Base


class Followers(Base):
    __tablename__ = 'fan_followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    follower_id = Column(Integer, ForeignKey('users.id'), nullable=False)
