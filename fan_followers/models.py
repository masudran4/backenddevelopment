from sqlalchemy import Column, Integer, ForeignKey,String

from database import Base


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    follower_username = Column(String, ForeignKey('users.username'), nullable=False)
    following_username = Column(String, ForeignKey('users.username'), nullable=False)
