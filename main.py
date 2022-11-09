from datetime import datetime
from time import strftime
from birthday_service import BirthdayService
from infra.data_file_adapter import DataFileAdapter
from domain.email_service import EmailService


def main():
    birthday_service = BirthdayService(
        DataFileAdapter(list_employee=[]),
        EmailService(),
    )
    birthday_service.sendGreetings(datetime.now().strftime("%Y/%m/%d"))


if __name__ == "__main__":
    main()
