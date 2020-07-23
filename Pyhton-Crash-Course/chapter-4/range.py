# Working with the range() function
# creating a list of numbers using the list() function with range() to provide the values

# range() argument options:
# single value range(4) output is 0,1,2,3
# start and end value range(1,5) output is 1,2,3,4.  Think of a loop where the last value changed the result to False and ended the loop before taking anymore actions.
# skipping number range(1,10,2) output is 1,3,5,7,9

# list conprehension
# used to write a simple for loop in a single line instead of multiple
# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# Conprehension
# squares = [value**2 for value in range(1,11)]
# print(squares)

print('4-3 Counting to Twenty')
counting = []
for number in range(1,21):
    counting.append(number)
print(counting)

print('4-4 One Million')
million_count = list(range(1,1000001))
# for number in million_count:
#     print(number)

print('4-5 Summing a Milion')
print(min(million_count))
print(max(million_count))
print(sum(million_count))

print('4-6 Odd Numbers')
odds = []
for value in range(1,20,2):
    odds.append(value)
print(odds)

print('4-7 Threes')
threes = []
for value in range(3,30,3):
    threes.append(value)
print(threes)

print('4-8 Cubes')
cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

print('4-9 Cube Comprehension')
cubes = [value ** 3 for value in range(1,11)]
print(cubes)