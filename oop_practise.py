## person
class Person:
    def __init__(self, name: str, course:str, faculty:str):
        self.name = name
        self.course = course
        self.faculty = faculty
    def print_details(self):
        print(f"my name is {self.name}")
    def __str__(self):
        return f"my name is {self.name}"



person1 = Person("Charles Coco", "IT", "CIT")
# person1.print_details()
print(person1)



class Student(Person):
    def __init__(self, name:str, course:str, faculty:str, reg_no:str, year:int, hostel:bool):
        super().__init__(name, course, faculty)
        self.reg_no = reg_no
        self.year = year
        self.hostel = hostel
    def book_hostel(self):
        if self.hostel==False:
            print(f"{self.name} registration number {self.reg_no} you have successfully booked a hostel")
        else:
            print("You already booked a hostel")

student1 = Student("Katuo Kinda", "IT", "CIT", "CIT-77U-2026", 2026, True)
student2 = Student("John Doe", "BS", "Business", "BS-89I-2026", 2026, False)
student1.book_hostel()
student2.print_details()
student2.book_hostel()


