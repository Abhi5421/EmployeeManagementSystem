def add_department(company):
    dep_id = input("Enter department id: ")
    name = input("Enter department name: ")
    company.add_department(dep_id, name)


def remove_department(company):
    dep_id = input("Enter department ID: ")
    company.remove_department(dep_id)


def add_employee(company):
    dep_id = input("Enter department ID: ")
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    title = input("Enter employee title: ")
    company.add_employee(dep_id, emp_id, name, title)


def remove_employee(company):
    dep_id = input("Enter department ID: ")
    emp_id = input("Enter employee ID: ")
    company.remove_employee(dep_id, emp_id)


def list_employees_by_department(company):
    department_id = input("Enter department ID: ")
    company.list_employees_by_department(department_id)


def list_departments(company):
    company.list_departments()


def save_data(company):
    company.save_data("company_data.json")


def exit_program():
    print("Exiting program.")
    exit()
