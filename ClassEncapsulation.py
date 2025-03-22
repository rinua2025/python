class BankAccount:
    def __init__(self):
        self.__salary = 50000
    
    def salary(self):
        return self.__salary
    
obj = BankAccount()
print(obj.salary()) #works
#obj.__salary=1000
#print(obj.__salary) #Raises AttributError
