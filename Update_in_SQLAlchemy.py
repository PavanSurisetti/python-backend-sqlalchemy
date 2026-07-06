from sqlalchemy import create_engine,String,Integer,Float,Column
from sqlalchemy.orm import declarative_base,sessionmaker
Base=declarative_base()
class Student(Base):
    __tablename__='StudentDetails'
    sid=Column(Integer,primary_key=True)
    sname=Column(String)
    sage=Column(Integer)
    sper=Column(Float)
engine=create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)#this will creates the table in the Database
s1=Student(sid=1,sname='Ganesha',sage=19,sper=99.9)
s2=Student(sid=2,sname='Satya',sage=20,sper=98.9)
s3=Student(sid=3,sname='Pavan',sage=20,sper=95.43)
s4=Student(sid=4,sname='Surya',sage=21,sper=96.98)
s5=Student(sid=5,sname='Charles',sage=23,sper=81.9)
Session=sessionmaker(bind=engine)
session=Session()
session.add_all([s1,s2,s3,s4,s5])
session.commit()
print('DataBase Contains Before Update:')
print('Sid \t Sname \t Sage \t sper')
data=session.query(Student).all()
for i in data:
    print(i.sid,'\t',i.sname,'\t',i.sage,'\t',i.sper)
#updating the data
temp=session.query(Student).filter(Student.sid==5).first()
temp.sname='Charles Xavier'
session.commit()
print('DataBase Contains After Update:')
print('Sid \t Sname \t Sage \t sper')
data=session.query(Student).all()
for i in data:
    print(i.sid,'\t',i.sname,'\t',i.sage,'\t',i.sper)
print('Mulitple Updates')
session.query(Student).filter(Student.sage==20).update({Student.sage:25})
session.commit()
print('DataBase Contains After Multiple Updates:')
print('Sid \t Sname \t Sage \t sper')
data=session.query(Student).all()
for i in data:
    print(i.sid,'\t',i.sname,'\t',i.sage,'\t',i.sper)
