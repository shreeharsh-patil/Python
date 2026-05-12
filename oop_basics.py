# Python program to create a class and call methods
class Student:
    def __init__(self):
        self.name = 'Shreeharsh'
        self.age = 20
        self.marks = 90.5
    
    def display(self):
        print('Hi, I am', self.name)
        print('My age is', self.age)
        print('My marks are', self.marks)

print("Basics: instantiate student object")
s1 = Student()
s1.display()

print("\nConstructor with parameters")
class Employee:
    def __init__(self, n='', a=10, s=1000.0):
        self.name = n
        self.age = a
        self.sal = s
    
    def show(self):
        print('Emp Name: %s' % self.name)
        print('Emp Age: %d' % self.age)
        print('Emp Salary: %.2f' % self.sal)

e1 = Employee()
e2 = Employee('Rahul', 24, 50000.0)
print("Empty Employee record:")
e1.show()
print("Populated Employee record:")
e2.show()

print("\nPass values into another class's methods")
class EmployeeHelper:
    @staticmethod
    def update_salary(emp):
        emp.sal += 5000.0
        emp.show()

print("Salary update demonstration:")
EmployeeHelper.update_salary(e2)

print("\nTrack instances using class variables")
class CounterSample:
    count = 0  # Class Variable
    def __init__(self):
        CounterSample.count += 1
    
    @staticmethod
    def display_count():
        print("Number of instances created so far:", CounterSample.count)

c1 = CounterSample()
c2 = CounterSample()
CounterSample.display_count()
c3 = CounterSample()
CounterSample.display_count()

print("\nDemonstrating Instance, Class and Static methods")
class Bird:
    wings = 2  # static variable
    
    @classmethod
    def fly(cls, name):
        print('{} flies with {} wings'.format(name, cls.wings))

Bird.fly('Parrot')
Bird.fly('Sparrow')

print("\nComprehensive demo of distinct method types")
class Demo:
    # static variable
    base = 10
    
    def __init__(self, x):
        # instance variable
        self.val = x
    
    def calculate_square(self):
        # instance method
        return self.val * self.val
    
    @classmethod
    def modify_base(cls, new_val):
        # class method
        cls.base = new_val
    
    @staticmethod
    def check_even(num):
        # static method
        return num % 2 == 0

d = Demo(4)
print("Square of 4 (instance method):", d.calculate_square())
Demo.modify_base(20)
print("Modified Class base:", Demo.base)
print("Is 22 even (static method):", Demo.check_even(22))
