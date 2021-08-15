'''CHAPTER #7: USER INPUT AND WHILE LOOPS'''

# Page 121
# 7-1. Rental Car
'''car = input("Which car are you lookig for?\n")
print('Let me see if I can find you a ' + car.title)

#7-2. Restaurant Seating
people = input('How many people are in the dinner group?\n')
if int(people) > 8:
    print('You will have to wait for a table.')
else:
    print('The table is ready.')

# 7-3 Multiples of Ten
number = input('Enter a number:\n')
if int(number) % 10 == 0:
    print('The number is a multiple of 10.')
else:
    print('The number is not a multiple of 10.')

# Page 127-128
# 7-4. Pizza Toppings
message = 0
while message != 'quit':
    message = input('Enter the pizza toppings you would like:\n')
    print('Adding ' + message + ' to the pizza.')
    if message == 'quit':
        print('Quitting...')

# 7-5. Movie Tickets
age = ''
while age != 0:
    age = int(input("What is the age of the buyer?\n"))
    if age == 0:
        print('Invalid age.')
    elif 0 < age < 3:
        print('The ticket is free.')
    elif 3 <= age < 12:
        print('The ticket is $10.')
    elif age >= 12:
        print('The ticket is $15.') 

# 7-8. Deli
sandwich_orders = ['beef','fish','chicken','cheese','veg']
finished_sandwiches = []
while sandwich_orders[:]:
    x = sandwich_orders.pop()
    print('I made your ' + x + ' sandwich.')
    finished_sandwiches.append(x)
print(str(len(finished_sandwiches)) + ' sandwiches were made: ')
for order in finished_sandwiches:
    print(order.title() + ' sandwich')

# 7-9. No Pastrami
sandwich_orders = ['pastrami','beef','fish','pastrami','chicken','cheese','pastrami','veg']
sandwich_orders = [order.lower() for order in sandwich_orders]
finished_sandwiches = []
# for order in sandwich_orders:
#     if order == 'pastrami':
#         sandwich_orders.remove(order)
#           OR
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders[:]:
    x = sandwich_orders.pop()
    print('I made your ' + x + ' sandwich.')
    finished_sandwiches.append(x)
print(str(len(finished_sandwiches)) + ' sandwiches were made: ')
for order in finished_sandwiches:
    print(order.title() + ' sandwich')
'''
# 7-10. Dream Vacation
poll = {}
flag = True
while flag:
    name = input('What is your name: ')
    place = input('If you could visit one place in the world, where would you go? ')

    poll[name] = place
    
    again = input('Would you like to let another person respond? (yes/ no) ') 
    if again.lower() == 'yes':
        continue
    elif again.lower() == 'no':
        flag = False
for key,value in poll.items():
    print(key.title() + ' would like to visit ' + value.title())