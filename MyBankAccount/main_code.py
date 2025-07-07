from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, bank_balance=0):
        self._bank_balance = bank_balance  # Changed to protected (single underscore)

    @abstractmethod  
    def deposit(self, amt):
        pass

    @abstractmethod
    def withdrawl(self, amt):
        pass

class SavingBankAccount(BankAccount):
    __deposit_limit_year = 1_00_000  # Class-level private variable

    def __init__(self, balance=0):
        super().__init__(balance)
        print("Your Account has been created.")

    def deposit(self, amt):
        if amt <= 0:
            print("Enter a valid amount.")
            return

        if amt > SavingBankAccount.__deposit_limit_year:
            print("Deposit Limit reached.")
            return

        self._bank_balance += amt
        SavingBankAccount.__deposit_limit_year -= amt
        print(f"Thank You for Depositing.\nYour Current balance is {self._bank_balance}")

    def withdrawl(self, amt):
        if amt <= 0:
            print("Enter a valid amount.")
        elif amt > self._bank_balance:
            print("Insufficient funds.")
        else:
            self._bank_balance -= amt
            print(f"Withdrawal successful. Remaining balance: {self._bank_balance}")

# Usage
siddh = SavingBankAccount(0)
siddh.deposit(5000000000000)
siddh.withdrawl(200)
