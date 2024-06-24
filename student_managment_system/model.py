from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    roll_no = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    class_name = Column(String(50), nullable=False)
    subjects = Column(String(200), nullable=False)
    gender = Column(String(10), nullable=False)
    dob = Column(Date, nullable=False)
    mobile_no = Column(String(15), nullable=False)
    address = Column(String(100), nullable=False)
