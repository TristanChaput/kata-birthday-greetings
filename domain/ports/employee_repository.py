class EmployeeRepository:
    def __init__(self, list_employees) -> None:
        self.list_employees = list_employees

    def get_all_employees(self):
        return self.list_employees
