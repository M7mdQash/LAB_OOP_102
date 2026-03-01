from bank import BankAccount

#main methood
if __name__ == "__main__":
    # while True:
        account1 = BankAccount("Mohammad")
        account2 = BankAccount("Abdulbari",154000.54)
        
        account1.deposit(15)
        account1.withdraw(5)
        
        account2.get_account_holder()
        account2.get_balance()
    
