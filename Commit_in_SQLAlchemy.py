from sqlalchemy import create_engine,String,Integer,Float,Column
from sqlalchemy.orm import declarative_base,sessionmaker
Base=declarative_base()#this will recognize class as table
class Student(Base):
    __tablename__='Student_details'#this is actual table name that u will see in the database
    sid=Column(Integer,primary_key=True)
    sname=Column(String)
    sage=Column(Integer)
    sper=Column(Float)
engine=create_engine('sqlite:///students.db')#creates a connection to sqlite
Base.metadata.create_all(engine)#this will creates a table
s1=Student(sid=1,sname='Ganesha',sage=19,sper=99.98)
s2=Student(sid=2,sname='Satya',sage=20,sper=97.97)
s3=Student(sid=3,sname='Pavan',sage=21,sper=95.98)
s4=Student(sid=4,sname='Alex',sage=26,sper=83)
s5=Student(sid=5,sname='Maeve',sage=29,sper=89)
Session=sessionmaker(bind=engine)#session enable us to add the data or access the data or performing the manipulation
session=Session()
session.add_all([s1,s2,s3,s4,s5])
session.commit()#this will save the data permanently in the database
data=session.query(Student).all()
for i in data:
    print(i.sid,i.sname)
print('data fetched successfully!')