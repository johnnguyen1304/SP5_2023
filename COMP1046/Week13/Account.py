import icontract

class Account:
    minimumBalance = 1000

    @icontract.require(lambda initialBalance: isinstance(initialBalance,int) and initialBalance >= Account.minimumBalance)
    def __init__(self, initialBalance):
        self.balance = initialBalance
    
    @icontract.require(lambda amount: isinstance(amount, int) and amount > 0)
    def deposit(self, amount):
        self.balance += amount

    @icontract.require(lambda amount: isinstance(amount, int) and amount >0)
    @icontract.ensure(lambda self: self.balance >= Account.minimumBalance)
    def withdraw(self, amount):
        self.balance -= amount


# Testing contracts.
try:
    account = Account(500)  # Should cause exception
    print("Allowing balance lower than 1000!")
except:
    print("Minimum balance is 1000.")

try:
    account = Account(1000.5)  # Should cause exception
    print("Allowing non-integer initial balance!")
except:
    print("Initial balance must be integer.")

try:
    account = Account(1000)  # Should run without exception
except:
    print("This should not happen.")

try:
    account.deposit(100.0)  # Should cause exception
    print("Allowing non-integer amount to deposit!")
except:
    print("Must be integer amount to deposit.")

try:
    account.deposit(-100)  # Should cause exception
    print("Allowing negative amount to deposit!")
except:
    print("Cannot deposit negative amount.")

try:
    account.deposit(100)  # Should run without exception
except:
    print("This should not happen.")

try:
    account.withdraw(100.0)  # Should cause exception
    print("Allowing non-integer amount to withdraw!")
except:
    print("Must be integer amount to withdraw.")

try:
    account.withdraw(-100)  # Should cause exception
    print("Allowing negative amount to withdraw!")
except:
    print("Cannot withdraw negative amount.")

try:
    account.withdraw(200)  # Should cause exception
    print("Allowing balance to go below minimum!")
except:
    print("Warning: balance went below minimum balance.")

# 1 - The minimum balance is 1000 this is a precondition violation at the initialiser.
account = Account(999)

# 2 - The account balance after withdraw is less than the mimum balance so this is a post-condition violation at the withdraw method.
account=Account(1000)
account.withdraw(1)

# 3- The deposite is less than 0 this is a precondition violation at the withdraw method.
account=Account(1000)
account.deposit(-1)
