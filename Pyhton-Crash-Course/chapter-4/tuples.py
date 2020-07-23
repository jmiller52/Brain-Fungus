# Tuples

# A tuple is difined by usign paranthesis instead of square brackets
# A tuple requires a comma be present in the values or python would think you are just trying to provide on argument
# Tuples are immutable

print('4-13 Buffet')
main_items = ('waffles', 'scrambles eggs', 'bacon', 'grits', 'chicken fried steak')
print("The buffet's five main items are: ")
for value in main_items:
    print(value)
print('\n')
# This should fail
# main_items[4] = 'cinnamon rolls'
# failed correctly

print("The buffet's updates main items are: ")
main_items = ('waffles', 'scrambles eggs', 'bacon', 'fresh fruit', 'cinnamon rolls')
for value in main_items:
    print(value)