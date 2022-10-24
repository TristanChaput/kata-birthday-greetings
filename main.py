from datetime import datetime
from time import strftime
from birthday_service import BirthdayService
from data_file_adapter import DataFileAdapter
from email_service import EmailService
from domain.employee_repository import EmployeeRepository


def main():
    birthday_service = BirthdayService(
        DataFileAdapter(list_employee=[]),
        EmailService(),
    )
    birthday_service.sendGreetings(datetime.now().strftime("%Y/%m/%d"))


if __name__ == "__main__":
    main()
