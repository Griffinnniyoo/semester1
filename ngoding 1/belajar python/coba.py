class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def is_old(self):
        return self.age > 100
    
print(Student)
   