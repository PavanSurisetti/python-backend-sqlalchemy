from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.orm import declarative_base
#declarative base is used to identify the class as table 
Base=declarative_base()
#any class that inherit from base is treated as table in the database
engine=create_engine('sqlite:///students.db')
class Student(Base):
    __tablename__='students'#this is the actual name that will be named to a table in the database
    id=Column(Integer,primary_key=True)# this is the id which is a primary key
    name=Column(String)
    age=Column(Integer)
Base.metadata.create_all(engine)
print('Table created successfully')