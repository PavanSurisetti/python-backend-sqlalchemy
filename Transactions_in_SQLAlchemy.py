from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.orm import declarative_base,sessionmaker
Base=declarative_base()
class company(Base):
    __tablename__='EmpDetails'
    eid=Column(Integer,primary_key=True)
    ename=Column(String)
    esalary=Column(Float)
engine=create_engine('sqlite:///employees.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
e1=company(eid=1,ename='Ganesha',esalary=1900000)
e2=company(eid=2,ename='Satya',esalary=1800000)
e3=company(eid=3,ename='Pavan',esalary=1700000)
session.add_all([e1,e2,e3])
session.commit()#this is the first safe point
try:
    t=session.query(company).filter(company.eid==3).first()
    # t=session.query(company).filter(company.eid==4).first()
    if t:
         t.esalary+=500000
         session.commit()
    else:
        raise Exception('Record not Found')
except Exception as ex:
    session.rollback()
    print('Failed due to:',ex)