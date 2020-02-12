# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

fruits2 = ('Apples',)
# single value needs trailing comma to be a tuple otherwise it will be considered a string

# print(fruits[1])

# fruits[0] = 'Pears'

# print(fruits2, type(fruits2))

# Delete Tuple
del fruits2

# print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate wont add
fruits_set.add('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
