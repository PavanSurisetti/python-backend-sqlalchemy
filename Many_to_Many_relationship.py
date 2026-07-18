from sqlalchemy import Column,Integer,String,Table,ForeignKey,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
Base=declarative_base()#this is used to recognize the classes as tables
#this will creates an association table between the students and courses
Student_Course_assoc=Table('Student_Course_Table', Base.metadata,
                           Column('SID',Integer,ForeignKey('Students_Table.sid')),
                           Column('CID',Integer,ForeignKey('Course_Table.cid'))

)
class student(Base):
    __tablename__='Students_Table'
    sid=Column(Integer,primary_key=True)
    sname=Column(String)
    course_relation=relationship('course',secondary=Student_Course_assoc,back_populates='student_relation')
class course(Base):
    __tablename__='Course_Table'
    cid=Column(Integer,primary_key=True)
    cname=Column(String)
    #relationship('class name',secondary=association table name,)
    student_relation=relationship('student',secondary=Student_Course_assoc,back_populates='course_relation')
engine=create_engine('sqlite:///Many_To_Many_relation_Concept.db')
Base.metadata.create_all(engine)
#list of students
s1=student(sid=1,sname='Ganesha')
s2=student(sid=2,sname='Satya')
s3=student(sid=3,sname='Pavan')
s4=student(sid=4,sname='Ram')
s5=student(sid=5,sname='Sai')
#list of courses
c1=course(cid=101,cname='Python')
c2=course(cid=102,cname='DSA')
c3=course(cid=103,cname='C++')
c4=course(cid=104,cname='C')
c5=course(cid=105,cname='C#')
c6=course(cid=106,cname='DVC')
c7=course(cid=107,cname='Data Science')
c8=course(cid=108,cname='SQL')
c9=course(cid=109,cname='SQLAlchemy')
c10=course(cid=110,cname='FastAPI')
Session=sessionmaker(bind=engine)
session=Session()
session.add_all([s1,s2,s3,s4,s5,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])
session.commit()
#now the insertion of the data into association table using the any relation variable in the tables
'''
Ganesha->DSA,Python,SQL
Satya->C,C++,C#
Pavan->Python,SQL,FastAPI,SQLAlchemy
Ram->C,DVC
Sai->DSA,Data Science,Python
'''
s1.course_relation.append(c1)
s1.course_relation.append(c2)
s1.course_relation.append(c8)
s2.course_relation.append(c3)
s2.course_relation.append(c4)
s2.course_relation.append(c5)
s3.course_relation.append(c1)
s3.course_relation.append(c8)
s3.course_relation.append(c9)
s3.course_relation.append(c10)
s4.course_relation.append(c4)
s4.course_relation.append(c6)
s5.course_relation.append(c2)
s5.course_relation.append(c7)
s5.course_relation.append(c1)
session.commit()
#data added successfully
# now let's access the data from student table
SD=session.query(student).all()
print("Student Table Contents")
for i in SD:#student data
    print(i.sid,i.sname)
CD=session.query(course).all()
for i in CD:#course data
    print(i.cid,i.cname)
#now lets access the Students-> courses 
studentdata=session.query(student).all()
print('Students->Courses')
for i in studentdata:
    for j in i.course_relation:
        print(f'Sid:{i.sid},Sname:{i.sname},Cid:{j.cid},Cname:{j.cname}')
#now lets access the courses -> Students
coursedata=session.query(course).all()
print('courses -> Students')
for i in coursedata:
    for j in i.student_relation:
        print(f'Sid:{j.sid},Sname:{j.sname},Cid:{i.cid},Cname:{i.cname}')