from sqlalchemy import create_engine,Column,Integer,Float,String,func
from sqlalchemy.orm import declarative_base,sessionmaker
Base=declarative_base()
#this will helps to recognize classes as tables
engine=create_engine('sqlite:///GroupBy_Having.db')
class employ(Base):
    __tablename__='Employee_details'
    id=Column(Integer,primary_key=True)#this will identify each employ uniquely
    name=Column(String)#this is the name of the employ
    dept=Column(String)#this is the dept of employees
    salary=Column(Float)#this is the salary of the employees
Base.metadata.create_all(engine)#this will creates the table in the database
#let me create session for adding data
Session=sessionmaker(bind=engine)
session=Session()
#this creates session successfully
#now let's create the data that to be inserted into the database
e1=employ(id=1,name='John',dept='IT',salary=50000)
e2=employ(id=2,name='Alice',dept='IT',salary=60000)
e3=employ(id=3,name='Bob',dept='HR',salary=40000)
e4=employ(id=4,name='Carol',dept='HR',salary=45000)
e5=employ(id=5,name='David',dept='IT',salary=70000)
e6=employ(id=6,name='Eva',dept='Sales',salary=30000)
e7=employ(id=7,name='Frank',dept='Sales',salary=35000)
session.add_all([e1,e2,e3,e4,e5,e6,e7])
session.commit()
print('Count employees in each department')
result=session.query(employ.dept,func.count(employ.id)).group_by(employ.dept).all()
for dept,count in result:
    print(dept,'->',count)
print('Average Salary in each department')
result=session.query(employ.dept,func.avg(employ.salary)).group_by(employ.dept).all()
for dept,avgsal in result:
    print(dept,'->',avgsal)
print('Departments with more than 2 employees')
result=session.query(employ.dept,func.count(employ.id)).group_by(employ.dept)\
.having(func.count(employ.id)>2)\
.all()
for dept,count in result:
    print(dept,'->',count)
print('Departments with avg salary > 45000')
result=session.query(employ.dept,func.avg(employ.salary)).group_by(employ.dept)\
.having(func.avg(employ.salary)>45000)\
.all()
for dept,avgsal in result:
    print(dept,'->',avgsal)