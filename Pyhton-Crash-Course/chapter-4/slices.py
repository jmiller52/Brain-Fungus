# Slice

# a slice takes a section of a list and behaves similar to the range function
# print(players[0:3])  This prints the players in index 0,1 and 2
# print(players[3:])  This prints the players from the index 2 (third position due to starting at 0) and goes to the end of the list no matter what.
# print(players[:3])  This prints the players from the beginning up to but not including index 3 (0,1,2)
# print(players[:20:2])  This prints every other player in the list from teh beginning up to index 20 (not including)

print('4-10 Slices')

threes = []
for value in range(3,30,3):
    threes.append(value)
print(threes[:3])
print(threes[-3:])
print(threes[3:6])
print('\n')

print('4-11 My pizza, Your Pizza')
my_pizzas = ['pepperoni', 'sausage', 'ham']
friend_pizzas = my_pizzas[:]

my_pizzas.append('white sauce')
friend_pizzas.append('pineapple')

print(f'My favorite pizzas are: {my_pizzas}')
print(f'My friends favorite pizzas are: {friend_pizzas}\n')

# for pizza in pizzas:
#     print(f'I like {pizza.title()}.')

print('4-12 More Looping')
for value in my_pizzas:
    print(f'One of my favorite pizza toppings is {value}')
print('\n')
for value in friend_pizzas:
    print(f"One of my friend's favorite pizza toppings is {value}")