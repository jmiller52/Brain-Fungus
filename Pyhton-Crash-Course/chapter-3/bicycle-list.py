# Lists
# Make a list using the square brackets
bicycles = ['trek', 'cannondale', 'co-op', 'giant', 'specialized']

# This prints out the entire list including the brackets
print(bicycles)

# This prints out 'trek' becasue the only index that was called was the first.
print(bicycles[0])

# Lists can also take string methods
# The output from this is 'Trek' instead of 'trek' like before
print(bicycles[0].title())

# Can use F-strings to access values from a list and include them in your sentance.
message = (f"My current bike is a {bicycles[0].title()}.")
print(message)

# Updating list values

motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)

# Change the value of a list item in a specific index
# motorcycles[0] = 'ducati'

# add value to end of list with '.append(value)'
# motorcycles.append('ducati')

# add value to a specific index with '.insert(index, value)'
# motorcycles.insert(0, 'ducati')

# remove a value from a specific index with 'del motorcycles[index]'
# del motorcycles[2]

# remove the last value from a list and still be able to use it with '.pop()'
popped_motorcycles = motorcycles.pop()

print(popped_motorcycles)
print(motorcycles)


# Organizing lists

# Permanent change to list
# sort a list with '.sort()'
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# # reverse sort with '.sort(reverse=True)'.  T must be capital
# cars.sort(reverse=True)
# print(cars)

# Temporarily sort a list with 'sorted' before specifying the list
print('Here is the original list of cars:')
print(cars)

print('\nHere is the sorted list of cars:')
print(sorted(cars))

print('\nHere is the original list of cars again:')
print(cars)

# reverse a lists order with '.reverse()'
cars.reverse()
print(cars)

# get the length of a list with 'len(list_name)'
print(len(cars))