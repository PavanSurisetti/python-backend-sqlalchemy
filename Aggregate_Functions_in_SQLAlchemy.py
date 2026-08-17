from sqlalchemy import create_engine,Column,Integer,Float,String,func
from sqlalchemy.orm import sessionmaker,declarative_base
Base=declarative_base()
#this will helps to recognize classes as tables
engine=create_engine('sqlite:///Aggregate_Function.db')
class data(Base):
    __tablename__='Student_Details'
    sid=Column(Integer,primary_key=True)#this will identify each student uniquely
    sname=Column(String)#this is the name of the student
    sage=Column(Integer)#this is the age of the students
    sper=Column(Float)
Base.metadata.create_all(engine)#this will creates the table in the database
#let me create session for adding data
Session=sessionmaker(bind=engine)
session=Session()
#this creates session successfully
#now let's create the data that to be inserted into the database
s1=data(sid=101,sname='Ganesha',sage=20,sper=100)
s2=data(sid=102,sname='Satya',sage=22,sper=99)
s3=data(sid=103,sname='Pavan',sage=20,sper=95)
s4=data(sid=104,sname='Vikram',sage=23,sper=94)
s5=data(sid=105,sname='Alex',sage=23,sper=92)
s6=data(sid=106,sname='Charles',sage=25,sper=91)
s7=data(sid=107,sname='Edith',sage=27,sper=89)
s8=data(sid=108,sname='Roshith',sage=21,sper=90)
s9=data(sid=109,sname='Lucy',sage=22,sper=92)
s10=data(sid=110,sname='Benjiman',sage=27,sper=85)
s11=data(sid=111,sname='Butcher',sage=23,sper=92)
s12=data(sid=112,sname='Billy',sage=28,sper=80)
#session.add_all([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12])
session.commit()
#data is added successfully to the database
print('Aggregate Functions:\nCount() Function:',end='')#end=''is used to get in the same line
count=session.query(func.count(data.sid)).scalar()#without scalar u will get a tuple
print(count)#to get a single value we will use the .scalar()
print(f'Sum():{session.query(func.sum(data.sage)).scalar()}')
print(f'Avg():{session.query(func.avg(data.sper)).scalar()}')
print(f'Min():{session.query(func.min(data.sper)).scalar()}')
print(f'Max():{session.query(func.max(data.sper)).scalar()}')