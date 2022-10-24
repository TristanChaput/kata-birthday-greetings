from domain.employee import Employee
from domain.employee_repository import EmployeeRepository
from birthday_service import BirthdayService

import pytest


@pytest.fixture
def john():
    return Employee(
        last_name="Doe",
        first_name="John",
        date_of_birth="1982/10/08",
        email="john.doe@foobar.com",
    )


@pytest.fixture
def mary():
    return Employee(
        last_name="Ann",
        first_name="Mary",
        date_of_birth="1975/09/11",
        email="mary.ann@foobar.com",
    )


def test_should_return_a_list_of_employee_when_repository_is_called(john, mary):
    employee_repository = EmployeeRepository(list_employees=[john, mary])
    list_employees = employee_repository.get_all_employees()
    assert list_employees == [john, mary]


def test_can_send_a_greeting_when_its_john_birthday(john):
    today = "2022/10/08"
    employee_repository = EmployeeRepository(list_employees=[john])
    bs = BirthdayService(employee_repository=employee_repository, email_service=None)
    send_a_greeting = bs.can_send_a_greeting(employee=john, date=today)
    assert send_a_greeting


@pytest.mark.parametrize(
    "today",
    ["2022/10/22", "2022/10/21", "2022/10/20"],
)
def test_cant_send_a_greeting_when_its_not_john_birthday(today, john):
    employee_repository = EmployeeRepository(list_employees=[john])
    bs = BirthdayService(employee_repository=employee_repository, email_service=None)
    send_a_greeting = bs.can_send_a_greeting(employee=john, date=today)
    assert not send_a_greeting


def test_should_return_no_employees_when_repository_is_empty():
    employee_repository = EmployeeRepository(list_employees=[])
    list_employees = employee_repository.get_all_employees()
    assert list_employees == []
