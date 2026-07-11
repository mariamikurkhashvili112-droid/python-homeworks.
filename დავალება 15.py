class BankAccount:
    bank_name = "TBC Bank"
    __total_accounts = 0

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        return False

    def __init__(self, owner, balance):
        self._owner = owner

        if BankAccount.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0

        BankAccount.__total_accounts += 1

        count = BankAccount.__total_accounts
        if count < 10:
            self.__account_number = f"AN000{count}"
        elif count < 100:
            self.__account_number = f"AN00{count}"
        elif count < 1000:
            self.__account_number = f"AN0{count}"
        else:
            self.__account_number = f"AN{count}"

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.__balance += amount

    def withdraw(self, amount):
        if BankAccount.validate_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"


account1 = BankAccount("Nino Beridze", 500)
account2 = BankAccount("Anna Ugulava", -100)

print(account1)
print(account2)

account1.deposit(200)
print(account1.check_balance())

account1.withdraw(100)
print(account1.check_balance())

print(BankAccount.get_total_accounts())

