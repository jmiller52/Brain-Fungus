print('5-3 Alien Colors #1')
alien_color = 'green'

if 'green' in alien_color:
    print('You shot down a green alien. You earned 5 points!')

if 'purple' in alien_color:
    print('This alien is worth 400')

print('\n')

print('5-4 Alien Color #2')
alien_color = 'red'

if 'green' in alien_color:
    print('You earned 5 points')
else:
    print('You Earned 10 points')

print('\n')
print('5-5 Alien Color #3')
if 'green' in alien_color:
    print('You earned 5 points')
elif 'yellow' in alien_color:
    print('You Earned 10 points')
elif 'red' in alien_color:
    print('You earned 15 points!')

print('\n')

print('5-6 Stages of Life')
age = 37

if age < 2:
    print('You are a baby')
elif age < 4:
    print('You are a toddler')
elif age < 13:
    print('You are a kid')
elif age < 20:
    print('You are a teenager')
elif age < 65:
    print('You are an adult')
elif age >= 65:
    print('You are an elder')

print('\n')

print('5-7 Favorite Fruits')
fruits = ['bananas', 'raspberries', 'kiwis']

if 'kiwis' in fruits:
    print('I really like Kiwis!')
if 'grapes' in fruits:
    print('I really like Grapes!')
if 'raspberries' in fruits:
    print('I really like Raspberrries!')
if 'papayas' in fruits:
    print('I really like Papayas!')
if 'bananas' in fruits:
    print('I really like Bananas!')

print('\n')

print('5-8 Hello Admin')
users = ['steve', 'bob', 'admin', 'carol', 'debbie']

for user in users:
    if user == 'admin':
        print(f'Welcome {user.title()}, would you like to see a status report?')
    else:
        print(f'Welcome back {user.title()}, thank you for logging in again.')

print('\n')

print('5-9 No Users')
usersn = []

if usersn:
    for user in usersn:
        if user == 'admin':
            print(f'Welcome {user.title()}, would you like to see a status report?')
        else:
            print(f'Welcome back {user.title()}, thank you for logging in again.')
else:
    print('We need to get some users.')

print('\n')

print('5-10 Checking Usernames')
current_users = ['Silent', 'Mythic', 'Raging', 'Filthy', 'Drinky']
new_users =  ['sIlEnt', 'Flashing', 'Scrappy', 'FiLtHy', 'Hammered']

cul = [cul.lower() for cul in current_users]
# above adds new variable, variable is a list that is made from the values in an already existing list but all lowercase values.

for new_user in new_users:
    if new_user.lower() in cul:
        print(f'{new_user} is already taken. Please enter a different username.')
    else:
        current_users.append(new_user)
print(current_users)

print('\n')

print('5-11 Ordninal Number')
positions = [1,2,3,4,5,6,7,8,9]

for p in positions:
    if p == 1:
        print(f'{p}st Position')
    elif p == 2:
        print(f'{p}nd Postiion')
    elif p == 3:
        print(f'{p}rd Position')
    else:
        print(f'{p}th Position')