class Employee(object):
    def __init__(self, _num=0, _name='', _salary=0.0):
        self.num = _num
        self.name = _name
        self.salary = _salary
        
    def print_data(self):
        print ('EmpId: {}, EmpName: {}, EmpSalary: {}'.format(self.num,
                                                             self.name,
                                                             self.salary))
    def calculate_tax(self):
        print ('Processing tax for :....')
        self.print_data()
        slab = (self.salary * 12) - 300000
        tax = 0
        if slab > 0:
            tax = slab * 0.1
        print ("tax:", tax)
        
        
e1 = Employee(1234, 'John', 23600.0) # e1.__init__(1234, 'John', 23500)
e2 = Employee(1235, 'Samanta', 45000.0) # e2.__init__(1235, 'Samanta', 45000.0)

e1.print_data()
e2.print_data() 
