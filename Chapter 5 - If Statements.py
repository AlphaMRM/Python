'''CHAPTER #5: IF STATEMENTS'''

# Page 89
# 5-3. Alien Colors #1
'''alien_color = 'green'
if alien_color.lower() == 'green':
    print('The player earned 5 points.')
if alien_color.lower() == 'blue':
    print('The player earned 10 points.')
if alien_color.lower() == 'yellow':
    print('The player earned 15 points.')

# 5-4. Alien Colors #2
alien_color = input('Enter the color of the alien: ')
if alien_color.lower() == 'green':
    print('The player earned 5 points.')
elif alien_color.lower() != 'green':
    print('The player earned 10 points.')

# 5-5. Alien Colors #3
alien_color = input('Enter the color of the alien: ')
if alien_color.lower() == 'green':
    print('The player earned 5 points.')
if alien_color.lower() == 'yellow':
    print('The player earned 10 points.')
if alien_color.lower() == 'red':
    print('The player earned 15 points.')

# 5-6. Stages of Life
age = 42
if age < 2:
    print('The person is a baby.')
elif 2 <= age < 4:
    print('The person is a toddler.')
elif 4 <= age < 13:
    print('The person is a kid.')
elif 13 <= age < 20:
    print('The person is a teenager.')
elif 20 <= age < 65:
    print('The person is an adult.')
elif age >= 65 :
    print('The person is an elder.')

# 5-7. Favorite Fruit
favorite_fruits = ['mango', 'date', 'strawberry']
if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'mango' in favorite_fruits:
    print('You really like mangoes!')
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'date' in favorite_fruits:
    print('You really like dates!')
if 'strawberry' in favorite_fruits:
    print('You really like strawberries!')

# Page 93
# 5-8. Hello Admin
usernames = ['ramish','masood','admin','hassan','ahmed']
for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + username.title() + ', thank you for logging in again.')

# 5-9. No Users
usernames = ['ramish','masood','admin','hassan','ahmed']
if len(usernames) == 0:
        print('We need to find some users!')
elif len(usernames) != 0:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + username.title() + ', thank you for logging in again.')

# 5-10. Checking Usernames
current_users = ['Ramish','Masood','sanan','hassan','ahmed']
new_users = ['zaeem','hizbullah','ramish','musab','masood']
current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in new_users]
for new_user in new_users:
    if new_user in current_users:
        print('The username \'' + new_user + '\' is unavailable. Kindly add another username.')
    elif new_users not in current_users:
        print('The username \'' + new_user + '\' is available.')

# 5-11. Ordinal Numbers
numbers = list(range(1,10))
ordinal_list = []
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
        ordinal_list.append(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
        ordinal_list.append(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
        ordinal_list.append(str(number) + 'rd')
    elif 3 < number <= 9:
        print(str(number) + 'th')
        ordinal_list.append(str(number) + 'th')
print('I also created the ordinal list. Here it is: ')
print(ordinal_list)'''