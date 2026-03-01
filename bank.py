class BankAccount():
    pass
    def __init__(self,account_holder:str, init_balance:float=0):
        if not account_holder:
            raise ValueError("cannot make account with no holder")
        self.account_holder = account_holder
        
        if init_balance >= 0:
            self.__init_balance = init_balance
        else:
            raise ValueError("cannot make negative initial balance")
        
    
    def deposit(self, amount:float):
        if amount > 0:
            self.init_balance += amount
            return self.init_balance
        else:
            raise ValueError("deposit must be more than 0")
        
    
    def withdraw(self, amount:float):
        try:
            if self.init_balance - amount < 0:
                raise Exception("insuffucient funds in account")
            self.init_balance -= amount
            print(self.init_balance)
        except TypeError as e:
            print(e)
            
    
    def get_balance(self):
        print(self.init_balance)
        
    
    def get_account_holder(self):
        print(self.account_holder)
        