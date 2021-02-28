import collections

Employee = collections.namedtuple('Emplyee', ['name', 'age', 'designation'])
E = Employee('Alison', '30', 'Software Engineer')
E1 = ['Tom', '39', 'Sales manager']
Ed = {'name': 'Bob', 'age': 30, 'designation': 'Manager'}
print('The demosntration for using namedtuple as iterable is : ')
print(Employee._make(E1))
print('\n')
print("The demonstration of OrderedDict instance using namedtuple is : ")
print(E._asdict())
print("\n")
print("The demonstration of converstion of namedtuple instance to dict is :")
print(Employee(**Ed))
print("\n")
print("All the fields of Employee are :")
print(E._fields)
print("\n")
print("The demonstration of replace() that modifies namedtuple is : ")
print(E._replace(name='Bob'))
