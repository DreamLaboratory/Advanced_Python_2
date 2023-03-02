from dataclasses import dataclass, field, asdict, astuple

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        '''Called after __init__ method.'''
        if self.age < 0:
            raise ValueError("Age cannot be negative.")
    
    def __setattr__(self, name, value):
        '''Called when we try to set an attribute on an object.'''
        print(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

# Create a Person object.
person = Person(age=30, name="John")

# update the name attribute
person.name = "Davron"

# Print the Person object.
print(person)