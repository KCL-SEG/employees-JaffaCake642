"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return

    def __str__(self):
        return self.name


class SalaryEmployee(Employee):
    def __init__(self, name, salaryPay, bonuscommission =0, contractcommission =0, contracts =0):
        super().__init__(name)
        self.salaryPay = salaryPay
        self.bonuscommission = bonuscommission
        self.contractcommission = contractcommission
        self.contracts = contracts

    def get_pay(self):
        totalPay = self.salaryPay + self.bonuscommission + self.contractcommission*self.contracts
        return totalPay

    def __str__(self):
        if self.bonuscommission == 0 and self.contractcommission == 0:
            return(f'{self.name} works on a monthly salary of {self.salaryPay}.  Their total pay is {self.get_pay()}.')
        elif self.bonuscommission > 0:
            return(f'{self.name} works on a monthly salary of {self.salaryPay} and receives a bonus commission of {self.bonuscommission}.  Their total pay is {self.get_pay()}.')
        elif self.contractcommission > 0:
            return(f'{self.name} works on a monthly salary of {self.salaryPay} and receives a commission for {self.contracts} contract(s) at {self.contractcommission}/contract.  Their total pay is {self.get_pay()}.')


class ContractEmployee(Employee):
    def __init__(self, name, contractPay, contractHours, bonuscommission =0, contractcommission =0, contracts =0):
        super().__init__(name)
        self.contractPay = contractPay
        self.contractHours = contractHours
        self.bonuscommission = bonuscommission
        self.contractcommission = contractcommission
        self.contracts = contracts

    def get_pay(self):
        totalPay = self.contractPay*self.contractHours + self.bonuscommission + self.contractcommission*self.contracts
        return totalPay

    def __str__(self):
        if self.bonuscommission == 0 and self.contractcommission == 0:
            return(f'{self.name} works on a contract of {self.contractHours} hours at {self.contractPay}/hour.  Their total pay is {self.get_pay()}.')
        elif self.bonuscommission > 0:
            return(f'{self.name} works on a contract of {self.contractHours} hours at {self.contractPay}/hour and receives a bonus commission of {self.bonuscommission}.  Their total pay is {self.get_pay()}.')
        elif self.contractcommission > 0:
            return(f'{self.name} works on a contract of {self.contractHours} hours at {self.contractPay}/hour and receives a commission for {self.contracts} contract(s) at {self.contractcommission}/contract.  Their total pay is {self.get_pay()}.')



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)
#billie.get_pay()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)
#charlie.get_pay()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, 600)
