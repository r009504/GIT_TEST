class BankAccount(object):
    numberOfAccounts = 0
    def _init_(self, 
                 _ano=None, 
                 _atype=None,
                 _bal=None,
                 _name=None,
                 _pan =None,
                 _aadhar=None):
        self.__accNo = _ano
        self.__accType = _atype
        self.__balance = _bal
        self.__accHolderName = _name
        self.__panNumber = _pan
        self.__aadharNumber = _aadhar
        self.__ledger = []
        
        BankAccount.numberOfAccounts += 1
        
    def withdraw_amount(self, _amount):
        if self.__balance >= _amount:
            self.__balance -= _amount
            self.__ledger.append(-(_amount))
        else:
            print("Insufficient funds")
            
    def deposite_amount(self, _amount):
        self.__balance += _amount
        self.__ledger.append(_amount)
        
    def check_balance(self):
        return self.__balance
        
    def get_recent_transactions(self, n):
        return self.__ledger[-n:]
    
    @staticmethod
    def get_number_of_accounts():
        return BankAccount.numberOfAccounts