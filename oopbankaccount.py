'''
This is an Object Oriented Programming example.
It demonstrates the concepts of inheritance,encapsulation,data hiding and polymorphism.

'''
#The parent class BankAccount
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder #Public attribute
        self.__balance = balance #Private attribute(Encapsulation)

    #deposit() method
    '''
    Allows the account holder to deposit money into the account.
    '''    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount} has been deposited into your account. New balance is {self.__balance}')
        else:   
            print('Invalid deposit amount')

    #withdraw() method
    def withdraw(self, amount):
        '''
        Allows withdrawal of money from the account to reduce the balance.
        '''
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f'{amount} has been withdrawn from your account. New balance is {self.__balance}')
        else:
            print('Invalid withdrawal amount') 

    #get_balance() method
    def get_balance(self):
        '''
        Allows viewing of balance (getter method)
        '''
        return self.__balance           

   #end of Parent class BankAccount
   
   #We will now create child classes that inherit from the parent class BankAccount      
   ## INHERITANCE ##
   #The child class SavingsAccount
    class SavingsAccount(BankAccount):
      #child Constructor method
      def __init__(self, account_holder, balance, interest_rate):
          super().__init__(account_holder, balance) #Call the parent class constructor
          self.interest_rate = interest_rate #Public attribute
    

      def apply_interest(self):
          '''
          Applies interest to the account balance
          '''
          interest = self.get_balance() * self.interest_rate/100
          self.deposit(interest) #Call the parent class deposit method
          print(f'Interest of {interest} has been applied to your account. New balance is {self.get_balance()}')

 #child Class CheckingAccount
class CheckingAccount():
    def __init__(self, account_holder, balance, overdraft_limit):
        '''
        child constructor which uses the parent but also adds an extra feature of overdraft_limit
        '''
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        '''
        Polymorphism applies by having a child withdraw() method that overrides the parent withdraw() method to allow for overdrafts
        '''    
        if amount <= self.get_balance() + self.overdraft_limit:
            self.deposit(-amount)  #We will deposit a negative amount indicating an overdraft
            print(f'Overdraft allowed.{amount} has been withdrawn from your account. New balance is {self.get_balance()}')
        else:
            print('Withdrawal amount exceeds overdraft limit')

#Actual program

savings = SavingsAccount('John Doe', 1000, 5) #Create a savings account object with 1000 balance and 5% interest rate
checking = CheckingAccount('Jane Doe', 500, 200) #Create a checking account object with 500 balance and 200 overdraft limit 

savings.deposit(500) #Deposit 500 into savings account
savings.apply_interest() #Apply interest to savings account

checking.withdraw(900) #Exceeds overdraft limit
checking.withdraw(700) #Within overdraft limit   

