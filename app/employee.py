class Employee:
    def __init__(self,emp_id,name,title,department):
        self.emp_id = emp_id
        self.name = name
        self.title = title
        self.departments = department

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}"

    def to_dict(self):
        return {
            'emp_id': self.emp_id,
            'name': self.name,
            'title': self.title
        }
