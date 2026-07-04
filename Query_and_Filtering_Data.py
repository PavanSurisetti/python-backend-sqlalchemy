from sqlalchemy import create_engine,String,Integer,Column,Float,and_
from sqlalchemy.orm import declarative_base,sessionmaker
#imported necessary libraries for the creation of table and insertion of data
Base=declarative_base()
class Employee(Base):#created a employ table
    __tablename__='Employ_Data'
    eid=Column(Integer,primary_key=True)
    ename=Column(String)
    esalary=Column(Float)
    eage=Column(Integer)
    exp=Column(Float)
engine=create_engine('sqlite:///employees.db')
Base.metadata.create_all(engine)
#table and engine are created successfully
Session=sessionmaker(bind=engine)
session=Session()
e1=Employee(eid=101,ename='Ganesha',esalary=100000,eage=22,exp=3)
e2=Employee(eid=102,ename='Satya',esalary=200000,eage=23,exp=3)
e3=Employee(eid=103,ename='Sai',esalary=150000,eage=24,exp=4)
session.add_all([e1,e2,e3])
session.commit()
#data added successfully 
#let's apply the query and filtering features
employees=session.query(Employee).all()#it fetches all the employes details
print(' all data:')
for i in employees:
    print(i.eid,i.ename,i.eage,i.esalary,i.exp)
print('only name column')
ename=session.query(Employee.ename).all()
for i in ename:
    print(i.ename)
filtering=session.query(Employee).filter(and_((Employee.eage>22),(Employee.esalary>=150000))).all()
print('filtering age>22 and salary>=150000')
for i in filtering:
    print(i.ename)