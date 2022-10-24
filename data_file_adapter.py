from data_file import DataFile
from domain.employee import Employee
from domain.employee_repository import EmployeeRepository


class DataFileAdapter(EmployeeRepository, DataFile):
    def __init__(self, list_employee) -> None:
        super().__init__(list_employee)
        self.format_data_from_file()

    def format_data_from_file(self) -> None:
        data = self.get_data_from_file()
        formated_employee_list = []
        for i in range(len(data)):
            entry = data.iloc[i]
            formated_employee_list.append(
                Employee(
                    last_name=entry.last_name,
                    first_name=entry.first_name,
                    date_of_birth=entry.date_of_birth,
                    email=entry.email,
                )
            )
        self.list_employees = formated_employee_list
