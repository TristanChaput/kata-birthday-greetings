from domain.employee import Employee
from domain.ports.employee_repository import EmployeeRepository
import pandas as pd


class CSVDataFileAdapter(EmployeeRepository):
    def __init__(self, list_employee) -> None:
        super().__init__(list_employee)
        self.format_data_from_file()

    def format_data_from_file(self) -> None:
        data_from_csv_file = pd.read_csv("data.txt", sep=",")
        formated_employee_list = []
        for i in range(len(data_from_csv_file)):
            entry = data_from_csv_file.iloc[i]
            formated_employee_list.append(
                Employee(
                    last_name=entry.last_name,
                    first_name=entry.first_name,
                    date_of_birth=entry.date_of_birth,
                    email=entry.email,
                )
            )
        self.list_employees = formated_employee_list
