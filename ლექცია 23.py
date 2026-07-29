import unittest


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("შესატანი თანხა უნდა იყოს 0-ზე მეტი.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("გამოსატანი თანხა უნდა იყოს 0-ზე მეტი.")
        if amount > self.balance:
            raise ValueError("ანგარიშზე არ არის საკმარისი თანხა.")
        self.balance -= amount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Saba", 100.0)

    def test_initialization(self):
        self.assertEqual(self.account.owner, "Saba")
        self.assertEqual(self.account.balance, 100.0)

    def test_deposit_success(self):
        self.account.deposit(50.0)
        self.assertEqual(self.account.balance, 150.0)

    def test_deposit_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-20.0)

    def test_withdraw_success(self):
        self.account.withdraw(40.0)
        self.assertEqual(self.account.balance, 60.0)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150.0)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-10.0)


if __name__ == '__main__':
    unittest.main()