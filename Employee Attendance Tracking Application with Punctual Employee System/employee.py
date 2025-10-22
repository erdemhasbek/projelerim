class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def to_dict(self):
        return {"Employee ID": self.emp_id, "Name": self.name}