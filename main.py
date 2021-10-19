class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def display(self):
         return {'name':self.name, 'Age':self.age}


class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        tempdict = Person.display(self)
        tempdict['Section'] = self.section
        return tempdict


person1 = Person('Bhojaraj bharambe', '22')
print(person1.display(),'\n\n')

stud1 = Student('Ashish', '21', 'TY-01')
print(stud1.displayStudent())