from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from decimal import Decimal

Base = declarative_base()

# Define the Employee table
class Employee(Base):
    __tablename__ = 'employee'
    
    employee_id = Column("EmployeeID", Integer, primary_key=True)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    salary = Column("Salary", Integer)
    
    def __init__(self,employee_id, first_name, last_name, salary):
        self.employee_id= employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
                
    def __repr__(self):
        return f"({self.employee_id}) Full Name: {self.firstname} {self.lastname}, Salary: {self.salary}" 

    
# Define the Department table
class Department(Base):
    __tablename__ = 'department'
    
    department_id = Column("DepartmentID", Integer, primary_key=True)
    department_name = Column("DepartmentName", String)
    
    def __init__(self, department_id, department_name):
        self.department_id = department_id
        self.department_name = department_name
        
    def __repr__(self):
        return f"(DepartmentID:{self.department_id}) Department Name:{self.department_name}"     
    

        
# Create an engine
engine = create_engine("sqlite:///mydb.db", echo=True)
# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)
# Create a Session
session = Session()


emp1 = Employee( 121, "Jason", "Smith", 10000)
session.add(emp1)
emp2 = Employee( 141, "Emma", "Tonks", 20000)
session.add(emp2)
emp3 = Employee( 151, "David", "Thompson", 30000)
session.add(emp3)
session.commit()


department1 = Department( 12, "Finance")
session.add(department1)
department2 = Department( 13, "Human Resource")
session.add(department2)
department3 = Department( 14, "Marketing")
session.add(department3)
session.commit()

# # Create a relationship
# emp_dept = EmployeeDepartment(employee_id=employee1.employee_id, department_id=department1.department_id)
# session.add(emp_dept)
# session.commit()

# Query and print results
employees = session.query(Employee).all()
departments = session.query(Department).all()
# employee_departments = session.query(EmployeeDepartment).all()

print(employees)
print(departments)
# print(employee_departments)