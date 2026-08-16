from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker
Base=declarative_base()
#this will recognizes class as Table
class Student(Base):
    __tablename__='Students'
    id=Column(Integer,primary_key=True)
    name=Column(String) 
class course(Base):
    __tablename__='Courses'
    id=Column(Integer,primary_key=True)
    cname=Column(String)
    student_id=Column(Integer,ForeignKey('Students.id'))
class StudentCourse(Base):
    __tablename__ = 'StudentCourses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #autoincrement is “Let the database automatically generate a unique ID for each row.”
    student_id = Column(Integer)
    student_name = Column(String)
    course_id = Column(Integer)
    course_name = Column(String)
engine=create_engine('sqlite:///FilteringAfterJoin.db')
Base.metadata.create_all(engine)
#students table data
s1=Student(id=1,name='Sai')
s2=Student(id=2,name='Ram')
s3=Student(id=3,name='John')
#courses table data
c1=course(id=1,cname='Python',student_id=1)
c2=course(id=2,cname='Java',student_id=1)
c3=course(id=3,cname='C++',student_id=2)
c4=course(id=4,cname='SQL')
#now let's create a session for it
Session=sessionmaker(bind=engine)
session=Session()
#session.add_all([s1,s2,s3,c1,c2,c3,c4])
session.commit()
#let me display me the content of the student table
SD=session.query(Student).all()
print('Student Table')
for i in SD:
    print(i.id,i.name)
#let me display me the content of the Course table
CD=session.query(course).all()
print('======'*3)
print('Course Table')
for i in CD:
    print(i.id,i.cname,i.student_id)
print('======'*3)
#now let's perform Left join
#.outerjoin(Course) → LEFT JOIN
#filtering applying here
result=session.query(Student,course)\
.outerjoin(course)\
.filter(
    course.cname=='Python'
)\
.all()
for s,c in result:
    print(s.id,s.name, c.id if c else None, c.cname if c else None)
    # c.id if c else None -> “If c exists (not None), return c.id, otherwise return None”
    record=StudentCourse(
        student_id=s.id,
        student_name=s.name,
        course_id=c.id if c else None,
        course_name=c.cname if c else None
    )
    session.add(record)
session.commit()