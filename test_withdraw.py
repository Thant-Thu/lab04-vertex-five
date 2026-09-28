import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_withdraw(account):
    account.withdraw(50)
    assert account.balance == 50

def test_overdraft(account):
    with pytest.raises(ValueError):
        account.withdraw(200)