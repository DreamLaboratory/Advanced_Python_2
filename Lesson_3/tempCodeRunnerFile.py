
counter = 0

class Employee:

    counter = 0 # Class variable or attribute

    def __init__(self, first, last):
        self.first = first
        self.last = last

        Employee.counter += 1


    def __repr__(self):
        return f"Employee ('{ self.first }', '{ self.last }')"

    def __str__(self):
        return f"{ self.first } { self.last }"

    def __add__(self, other):
        return f"{ self.first } { other.last }"


    def __len__(self):
        return len(self.first) + len(self.last)

emp_1 = Employee("Davron", "Davronov")

print(emp_1.counter)

emp_2 = Employee("Adam", "Smith")
print(emp_2.counter)

print(Employee.counter)


print(emp_1)
print(emp_2)

print(emp_1 + emp_2)

print(len(emp_1))
