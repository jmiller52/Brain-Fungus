print('5-1 Conditional Tests') 
# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
car = 'Nissan'
dog = 'Daisy'
wife = 'Kalina'
child = 'Cora'
python = 'Required'

print("Is car == 'Nissan'? I predict True")
print(car == 'Nissan')

print("Kalina's car == 'Nissan'? I predict False.")
print(car == 'Subaru')

print("Is our dog's name == 'Daisy'? I predict True")
print(dog == 'Daisy')

print('5-2 More Conditionals')
items = ['router', 'table', 'controller', 'monitor', 'cad cam']
item1 = 'controller'
item2 = 'bit'

for item in items:
    if item1 in item:
        print(f'{item.title()} is in our list of CNC Router parts')
if item2 not in item:
    print(f'{item2.title()} was not in the list but should have been')