
"""
collections.namedtuple – Convenient Data Objects, assigning meaning to each position at tuple
typing.NamedTuple – Improved Namedtuples, with type hints and more
somenamedtuple._make(iterable) – Constructs a namedtuple from a sequence or iterable
somenamedtuple._asdict() – Returns a new OrderedDict which maps field names to their values
somenamedtuple._replace(**kwargs) – Returns a new namedtuple replacing specified fields with new values
somenamedtuple._fields – Returns the list of field names
"""

from collections import namedtuple

def example_1():
    Point = namedtuple('Point', ['x', 'y', 'z'])
    p = Point(11, y=22, z=33)
    print(p.x, p.y, p.z)
    print((p.x + p.y)==p.z)
    p.z = 234  #  can't set attribute

def example_2():
    """Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3:
    """
    import csv


    EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

    em1 = EmployeeRecord('John', '25', 'Software Engineer', 'IT', 'A')
    em2 = EmployeeRecord('Jane', '23', 'Software Engineer', 'IT', 'A')
    em3 = EmployeeRecord('Jack', '25', 'Software Engineer', 'IT', 'A')

    employees = [em1, em2, em3]

    # write to csv
    with open('output.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(('Name', 'age', 'title', 'department'))  # header
        w.writerows([(data.name, data.age, data.department) for data in employees])

    # read from csv
    
    # for emp in map(EmployeeRecord._make, csv.reader(open("csv_file.csv", "rb"))):
    #     print(emp.name, emp.title)


def main():
    # example_1()
    example_2()


if __name__ == "__main__":
    main()