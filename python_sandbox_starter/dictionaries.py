# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name' : 'Doe',
    'age' : 30
}

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')

# print(person2, type(person2))

#Get value
print(person['first_name'])
print(person.get('last_name'))

#Add key/value

person['phone'] = '555-555-5555'

#Get dict keys
print(person.keys())

#Get dict items
print(person.items())

# Copy dict and add specific value
person2 = person.copy()
person2['city'] = 'Boston'

# REmove item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Get Length
print(len(person2))

#List of Dictionary
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'kevin', 'age': 20},
]

print(people[1]['name'])
