import json
from app.department import Department
from app.employee import Employee


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_id, name):
        if department_id not in self.departments:
            self.departments[department_id] = Department(department_id, name)
            print("Department Created")
        else:
            print("Department already exists")

    def remove_department(self, department_id):
        if department_id in self.departments:
            del self.departments[department_id]
            print("Department removed")
        else:
            print("Department not found")

    def add_employee(self, department_id, emp_id, name, title):
        if department_id in self.departments:
            department = self.departments[department_id]
            employee = Employee(emp_id, name, title,department)
            department.add_employee(employee)
            print("Employee added")
        else:
            print("Department not found")

    def remove_employee(self, department_id, emp_id):
        if department_id in self.departments:
            department = self.departments[department_id]
            if department.remove_employee(emp_id):
                print("Employee removed")
            else:
                print("Employee not found")
        else:
            print("Department not found")

    def list_employees_by_department(self, department_id):
        if department_id in self.departments:
            department = self.departments[department_id]
            print(f"\nEmployees in {department_id}:")
            for employee in department.list_employees():
                print(employee)
        else:
            print("Department not found.")

    def list_departments(self):
        print("\n Departments:")
        for department_id in self.departments:
            print(f"department_id: {department_id}")

    def save_data(self, filename):
        data = {'departments': {}}
        for dept_name, department in self.departments.items():
            data['departments'][dept_name] = {
                'dept_id': department.dept_id,
                'name': department.name,
                'employees': [emp.to_dict() for emp in department.employees]
            }

        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for dept_id, dept_data in data['departments'].items():
                    self.departments[dept_id] = Department(dept_data['dept_id'],dept_data['name'])
                    self.departments[dept_id].employees = [Employee(**emp) for emp in dept_data['employees']]
            print("Data is loaded")
        except FileNotFoundError:
            print("No Data Found")
