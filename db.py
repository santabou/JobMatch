from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer,create_engine
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
connection_string="sqlite:///"+os.path.join(BASE_DIR,'DATA.db')
Base=declarative_base()
engine=create_engine(connection_string,echo=True)
Session=sessionmaker()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(String)
    position = Column(String)
    phone_number = Column(String)
    skill=Column(String)
    gender=Column(String)
    experience=Column(String)
    education=Column(String)
    chat=Column(String)
    def __repr__(self):
        return self.username+"&*&"+self.firstname+"&*&"+self.lastname+"&*&"+self.email+"&*&"+self.dob+"&*&"+self.position+"&*&"+self.phone_number+"&*&"+self.skill+"&*&"+self.education+"&*&"+self.gender+"&*&"+self.experience

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    companyname = Column(String)
    location = Column(String)
    chat=Column(String)
    def __repr__(self):
        return self.comname+"&*&"+self.position+"&*&"+self.salary+"&*&"+self.avaliable+"&*&"+self.due+"&*&"+self.email+"&*&"+self.phone+"&*&"+self.location+"&*&"+self.education+"&*&"+self.requirement

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    jobid=Column(String)
    username=Column(String)
    comname=Column(String)
    position=Column(String)
    salary=Column(String)
    available=Column(String)
    due=Column(String)
    email=Column(String)
    phone=Column(String)
    location=Column(String)
    education=Column(String)
    requirement=Column(String)
    apply=Column(String)

    def __repr__(self):
        return self.comname+"&*&"+self.position+"&*&"+self.salary+"&*&"+self.available+"&*&"+self.due+"&*&"+self.email+"&*&"+self.phone+"&*&"+self.location+"&*&"+self.education+"&*&"+self.requirement
    
class Message(Base):
    __tablename__ = 'messages'
    id= Column(Integer, primary_key=True)
    roomNo=Column(String)
    mess=Column(String)
    password=Column(String)

