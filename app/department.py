class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        return self.employees

