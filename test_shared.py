from bank import BankAccount

def test_shared_account_initial_balance(funded_account):
    assert funded_account.balance == 1000

def test_shared_account_deposit(funded_account):
    funded_account.deposit(500)
    assert funded_account.balance == 1500
    