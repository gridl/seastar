from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship

from .database import Base

### PLATFORM COMPONENTS

class Platform(Base):
    """
    """
    __tablename__ = 'pa_platform'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Node(Base):
    """
    """
    __tablename__ = 'pa_node'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform_id = Column(Integer, ForeignKey('pa_platform.id'))

    platform = relationship(
        Platform,
        backref=backref('pa_node',
                        uselist=True,
                        cascade='delete,all'))

class Processor(Base):
    """
    """
    __tablename__ = 'pa_Processor'
    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey('pa_node.id'))

    node = relationship(
        Node,
        backref=backref('pa_Processor',
                        uselist=True,
                        cascade='delete,all'))

#
# class Core(Base):
#     __tablename__ = 'platform_core'
#     id = Column(Integer, primary_key=True)
#     Processor_id = Column(Integer, ForeignKey('platform_Processor.id'))
#
# ### APPLICATION COMPONENTS
#
# class Application(Base):
#     __tablename__ = 'application'
#     id = Column(Integer, primary_key=True)
#
# class Process(Base):
#     __tablename__ = 'application_process'
#     id = Column(Integer, primary_key=True)
#
# class Thread(Base):
#     __tablename__ = 'application_thread'
#     id = Column(Integer, primary_key=True)
#
# ### MAPPINGS
#
# class ThreadToCoreMapping(Base):
#     __tablename__ = 'mapping_thread_to_core'
#     thread_id = Column(Integer, ForeignKey('application_thread.id'))
#     core_id = Column(Integer, ForeignKey('platform_core.id'))
#     # Mapping scope
#     b = Column(DateTime, default=func.now())
#     e = Column(DateTime)
#     # Mapping properties
#
# class ProcessToProcessorMapping(Base):
#     __tablename__ = 'mapping_thread_to_core'
#     thread_id = Column(Integer, ForeignKey('thread.id'))
#     Processor_id = Column(Integer, ForeignKey('Processor.id'))
#     # Mapping scope
#     b = Column(DateTime, default=func.now())
#     e = Column(DateTime)
#     # Mapping properties





# class Department(Base):
#     __tablename__ = 'department'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
#
# class Role(Base):
#     __tablename__ = 'roles'
#     role_id = Column(Integer, primary_key=True)
#     name = Column(String)
#
#
# class Employee(Base):
#     __tablename__ = 'employee'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     # Use default=func.now() to set the default hiring time
#     # of an Employee to be the current time when an
#     # Employee record was created
#     hired_on = Column(DateTime, default=func.now())
#     department_id = Column(Integer, ForeignKey('department.id'))
#     role_id = Column(Integer, ForeignKey('roles.role_id'))
#     # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
#     department = relationship(
#         Department,
#         backref=backref('employees',
#                         uselist=True,
#                         cascade='delete,all'))
#     role = relationship(
#         Role,
#         backref=backref('roles',
#                         uselist=True,
#                         cascade='delete,all'))
