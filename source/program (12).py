class NRIEmployeeTax(EmployeeTax):
    def __init__(self, _id, _name, _sal, _citizenship):
        super(NRIEmployeeTax, self).__init__(_id, _name, _sal)
        # -------------
        self.citizenship = _citizenship

    def income_tax(self):
        return self.eSal * 0.4

    def is_us_citizen(self):
        return 'United States' == self.citizenship
    
    def professional_tax(self):
        if self.is_us_citizen():
            return 2000
        return 200
    
nri_emp = NRIEmployeeTax(1234, 'John', 25000, 'United States')
nri_emp.net_salary()
