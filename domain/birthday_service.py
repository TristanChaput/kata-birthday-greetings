from datetime import datetime
from domain.employee import Employee
from domain.email_service import EmailService
from domain.ports.employee_repository import EmployeeRepository


class BirthdayService:
    def __init__(
        self, employee_repository: EmployeeRepository, email_service: EmailService
    ) -> None:
        self.employee_repository = employee_repository
        self.email_service = email_service

    def sendGreetings(self, today: datetime):
        for employee in self.employee_repository.get_all_employees():
            if self.can_send_a_greeting(employee, today):
                self.email_service.send_email(employee.first_name, employee.email)

    def can_send_a_greeting(self, employee: Employee, date: str):
        if self.is_birthday(employee, date):
            return True
        return False

    def is_birthday(self, employee: Employee, date: str):
        date_datetime = datetime.strptime(date, "%Y/%m/%d")
        employee_birthdate = datetime.strptime(employee.date_of_birth, "%Y/%m/%d")
        return (
            date_datetime.day == employee_birthdate.day
            and date_datetime.month == employee_birthdate.month
        )
