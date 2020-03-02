class Employee(object):
    def __init__(self):
        self.num = 0
        self.name = ''
        self.salary = 0.0

    def get_salary(self):
        return self.salary
    
    def get_name(self):
        return self.name
    
    def print_employee(self):
        print ('num=', self.num, ' name=', self.name, ' sal=', self.salary)