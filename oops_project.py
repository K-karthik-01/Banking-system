from bank_accounts import *

John=BankAccount('John', 1000)
Taylor=BankAccount('Taylor', 2000)

John.get_balance()
Taylor.get_balance()

Taylor.deposit(500)

John.withdraw(2000)
John.withdraw(10)

John.transfer(Taylor,10000)
John.transfer(Taylor,100)

Peter = InterestRewardsAccount('Peter', 1000)
Peter.get_balance()
Peter.deposit(100)
Peter.transfer(John, 100)

Tom = SavingsAccount('Tom', 1000)
Tom.get_balance()
Tom.deposit(100)
Tom.transfer(Taylor, 10000)
Tom.transfer(Taylor, 1000)



