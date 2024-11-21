import pytest

from employee import Employee, BankAccount


@pytest.fixture
def bank_account():
    return BankAccount("MyBank", 200)


@pytest.fixture
def employee(bank_account):
    return Employee("John Smith", bank_account, 1000)


@pytest.mark.parametrize("percent,salary_exp", [
    (5, 1050), (10, 1100), (20, 1200)])
def test_valid_percent(employee, percent, salary_exp):
    employee.raise_salary(percent)
    assert employee.salary == salary_exp


def test_invalid_percent(employee):
    with pytest.raises(ValueError):
        employee.raise_salary(50)
