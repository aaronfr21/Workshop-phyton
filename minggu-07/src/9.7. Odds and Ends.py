# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000