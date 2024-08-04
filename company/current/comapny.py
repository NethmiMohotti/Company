from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the base class
Base = declarative_base()

# Define the Employee table
class Employee(Base):
    __tablename__ = 'employee'
    
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    salary = Column(Integer)
    
    departments = relationship("Department", secondary="employee_department", back_populates="employees")
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def __repr__(self):
        return f"<Employee(employee_id={self.employee_id}, name={self.first_name} {self.last_name}, salary={self.salary})>"

# Define the Department table
class Department(Base):
    __tablename__ = 'department'
    
    department_id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String)
    
    employees = relationship("Employee", secondary="employee_department", back_populates="departments")
    
    def __init__(self, department_name):
        self.department_name = department_name
        
    def __repr__(self):
        return f"<Department(department_id={self.department_id}, name={self.department_name})>"

# Define the EmployeeDepartment table
class EmployeeDepartment(Base):
    __tablename__ = 'employee_department'
    
    employee_id = Column(Integer, ForeignKey("employee.employee_id"), primary_key=True)
    department_id = Column(Integer, ForeignKey("department.department_id"), primary_key=True)
    
    def __init__(self, employee_id, department_id):
        self.employee_id = employee_id
        self.department_id = department_id
        
    def __repr__(self):
        return f"({self.employee_id}, {self.department_id})"

# Create an engine
engine = create_engine('sqlite:///example.db')

# Recreate the database (drop all tables and create them again)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Add some data
employee1 = Employee(first_name="John", last_name="Doe", salary=50000)
employee2 = Employee(first_name="Jason", last_name="Smith", salary=10000)
employee3 = Employee(first_name="Emma", last_name="Tonks", salary=20000)
employee4 = Employee(first_name="David", last_name="Thompson", salary=30000)
department1 = Department(department_name="HR")
department2 = Department(department_name="Finance")
department3 = Department(department_name="Marketing")

session.add(employee1)
session.add(employee2)
session.add(employee3)
session.add(employee4)
session.add(department1)
session.add(department2)
session.add(department3)
session.commit()

# Create a relationship
emp_dept = EmployeeDepartment(employee_id=employee1.employee_id, department_id=department1.department_id)
session.add(emp_dept)
session.commit()


# Query and print results to verify deletions
employees = session.query(Employee).all()
departments = session.query(Department).all()
employee_departments = session.query(EmployeeDepartment).all()

print("Employees:", employees)
print("Departments:", departments)
print("EmployeeDepartments:", employee_departments)

session.close()
