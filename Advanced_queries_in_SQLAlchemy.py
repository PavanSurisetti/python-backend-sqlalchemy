from sqlalchemy import create_engine,String,Integer,Column,Float,and_,desc
from sqlalchemy.orm import declarative_base,sessionmaker
#imported necessary libraries for the creation of table and insertion of data
Base=declarative_base()
class Employee(Base):#created a employ table
    __tablename__='Employ_Details'
    eid=Column(Integer,primary_key=True)
    ename=Column(String)
    esalary=Column(Float)
    eage=Column(Integer)
    ecity=Column(String)
engine=create_engine('sqlite:///employees.db')
Base.metadata.create_all(engine)
#table and engine are created successfully
Session=sessionmaker(bind=engine)
session=Session()
e1=Employee(eid=101,ename='Ganesha',esalary=100000,eage=22,ecity='Banglore')
e2=Employee(eid=102,ename='Satya',esalary=200000,eage=23,ecity='Hyderabad')
e3=Employee(eid=103,ename='Surya',esalary=150000,eage=24,ecity='Gurugram')
e4=Employee(eid=104,ename='Pavan',esalary=195000,eage=21,ecity='Banglore')
e5=Employee(eid=105,ename='Jackie',esalary=150000,eage=28,ecity='Hyderabad')
session.add_all([e1,e2,e3,e4,e5])
session.commit()
#data added successfully 
#let's apply the query and filtering features
employees=session.query(Employee).all()#it fetches all the employes details
print('using the feature \'ALL\'')
for i in employees:
    print(i.eid,i.ename,i.eage,i.esalary,i.ecity)
print('using the feature \'LIKE\'')
names=session.query(Employee).filter(Employee.ename.like('%a')).all()
for i in names:
    print(i.eid,i.ename)
print('using the feature \'IN\'')
city=session.query(Employee).filter(Employee.ecity.in_(['Hyderabad'])).all()
for i in city:
    print(i.eid,i.ename,i.ecity)
print('using the feature \'Order By\'')
low_to_high_salary=session.query(Employee).order_by(Employee.esalary)
for i in low_to_high_salary:
    print(i.eid,i.ename,i.esalary)
print('using the feature \'Descending order by\'')
high_to_low_salary=session.query(Employee).order_by(desc(Employee.esalary))
for i in high_to_low_salary:
    print(i.eid,i.ename,i.esalary)
print('using the feature \'Limit\'')
highest_salary=session.query(Employee).order_by(desc(Employee.esalary)).limit(2).all()
for i in highest_salary:
    print(i.eid,i.ename,i.esalary)
print('using the feature \'First\'')
first_record=session.query(Employee).first()
#if u directly print the first record u may get like <__main__.Employee object at 0x...> to avoid and fetch data we use first_record.colname
print(first_record.eid,first_record.ename,first_record.eage,first_record.esalary,first_record.ecity)