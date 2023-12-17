class BalanceException(Exception):
      pass

class BankAccount:
      def __init__(self, account_holder, initial_amount) :
            self.name = account_holder
            self.balance = initial_amount
            print(f'\n Account of "{self.name}" is created \n with initial amountof ${self.balance:.2f}')
    
      def get_balance(self):
            print(f'\n "{self.name}" has ${self.balance:.2f}')
    
      def deposit(self, amount):
            self.balance = self.balance + amount
            print("\n deposit complete")
            self.get_balance()

      def viable_transaction(self, amount):
            if self.balance >= amount:
                  return
            
            else:
                  raise BalanceException(f'\n Sorry, "{self.name}" has only ${self.balance:.2f}')
      
      def withdraw(self, amount):
            try:
                  self.viable_transaction(amount)
                  self.balance = self.balance-amount
                  print(f"\n withdraw of ${amount} successful")
                  self.get_balance()

            except BalanceException as error:
                  print(f'\n withdraw of ${amount} is unsuccessful {error}')

      def transfer(self, account, amount):
            try: 
                  print('\nBeginning Transfer')
                  self.viable_transaction(amount) 
                  self.withdraw(amount) 
                  account.deposit(amount) 
                  print('\nTransfer complete! \n')

            except BalanceException as error: 
                  print(f'\nTransfer interrupted. {error}')

class InterestRewardsAccount(BankAccount): 
      def deposit(self, amount):
            self.balance = self.balance + (amount * 1.05)
            print("\nDeposit complete.")
            self.get_balance()

class SavingsAccount(InterestRewardsAccount):
      def __init__(self, account_holder, initial_amount): 
            super().__init__(account_holder, initial_amount)
            self.fee = 5

      def withdraw(self, amount): 
            try: 
                  self.viable_transaction(amount + self.fee)
                  self.balance = self.balance - (amount + self.fee) 
                  print("\n Withdraw completed.")
                  self.get_balance() 
                  
            except BalanceException as error: 
                  print(f'\nWithdraw interrupted: {error}')


      
      

            



                        

          
      
    