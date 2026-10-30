# inheritance

# employee -- name, id, department, gender
# salaried -- + salary, tenure
# casual -- rates,

# parent / super class
class Employee:
    def __init__(self, name:str, id_no:str, department:str, gender:str):
        self.full_names = name
        self.identity_no= id_no
        self.department = department
        self.gender = gender
    def print_detail(self):
        print(self.full_names)
        print(self.identity_no)
        print(self.department)
        print(self.gender)
        print("***********")

    def print_name(self):
        print(f"Name is {self.full_names}")

# sub class == child class
class SalariedEmployee(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, salary:int, tenure:int):
        super().__init__(name, id_no, department, gender)
        self.salary = salary
        self.tenure = tenure

class CasualWorker(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, rate:float):
        super().__init__(name, id_no, department, gender)
        self.rate = rate

    def calc_wage(self, hours:float):
        return hours * self.rate



s1 = SalariedEmployee("Nicole San", "345321", "IT", "F", 87_500, 4)
c1 = CasualWorker("Bob Val", "892378", "HR", "M", 300)

s1.print_detail()
c1.print_detail()
print(c1.calc_wage(7))

c1.print_name()