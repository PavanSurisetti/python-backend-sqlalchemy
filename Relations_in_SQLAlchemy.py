from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
Base=declarative_base()
engine=create_engine('sqlite:///Realtion_Concept_DB.db')
class student(Base):
    __tablename__='Students'
    sid=Column(Integer,primary_key=True)
    sname=Column(String)
    #relationship-> first argument should be class name of other table and backpopulates should have name of the relationship variable on the opposite side
    course_relation=relationship('course',back_populates='student_relation')
class course(Base):
    __tablename__='Courses'
    cid=Column(Integer,primary_key=True)
    cname=Column(String)
    stu_id=Column(Integer,ForeignKey('Students.sid'))
    student_relation=relationship('student',back_populates='course_relation')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
#list  of students 
s1=student(sid=1,sname='Ganesha')
s2=student(sid=2,sname='Satya')
s3=student(sid=3,sname='Pavan')
session.add_all([s1,s2,s3])
session.commit()
#list  of courses
c1=course(cid=101,cname='Python',stu_id=1)
c2=course(cid=102,cname='Java',stu_id=1)
c3=course(cid=103,cname='Data Science',stu_id=3)
c4=course(cid=104,cname='Machine Learning',stu_id=2)
c5=course(cid=105,cname='Artificial Intelligence',stu_id=2)
session.add_all([c1,c2,c3,c4,c5])
session.commit()
#now lets see the original data 
sData=session.query(student).all()
print('List out of Students:')
for i in sData:
    print(i.sid,i.sname)
print('List out of Courses:')
cData=session.query(course).all()
for i in cData:
    print(i.cid,i.cname,i.stu_id)
#now let's access the data of second table using the first table 
print('accessing  the data of second table using the first table')
temp1 = session.query(student).all()
for i in temp1:
    for c in i.course_relation:   # LOOP is required here for 1-M relationship
        print(f'Student ID:{i.sid}, Student Name:{i.sname}, Course ID:{c.cid}, Course Name:{c.cname}')
#now let's access the data of first table using the second table 
print('accessing  the data of first table using the second table')
temp2=session.query(course).all()
for i in temp2:
    print(f'Student ID:{i.student_relation.sid}, Student Name:{i.student_relation.sname},Course ID:{i.cid},Course Name={i.cname}')