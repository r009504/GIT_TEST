class EmployeeTax(object):
    def __init__(self, _id, _name, _sal):
        self.eId = _id
        self.eName = _name
        self.eSal = _sal

    def professional_tax(self):
        return 200
        
    def income_tax(self):
        return self.eSal * 0.3
            
    def net_salary(self):
        return self.eSal - self.income_tax() - self.professional_tax()
    
obj = EmployeeTax(1234, 'Jhon', 25000)
obj.net_salary()
