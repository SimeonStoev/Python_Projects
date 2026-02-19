class Student:

    def __init__(self, name, age, job, salary):
        self.__name = name
        self.__age = age
        self.__job = job
        self.__salary = salary

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_job(self):
        return self.__job
    def get_salary(self):
        return self.__salary

    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_job(self, job):
        self.__job = job
    def set_salary(self, salary):
        self.__salary = salary

    def get_student_info(self):
        return f"Name: {self.__name}, age: {self.__age}, job: {self.__job}, salary: {self.__salary}"

student1 = Student("John", "25", "Mathematics", 20000)
student2 = Student("Elon", "27", "Engineer", 50000)
print(student1.get_student_info())
student1.set_age(20)
print(student1.get_student_info())
print(student2.get_student_info())
