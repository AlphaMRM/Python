'''CHAPTER #3: INTRODUCING LISTS'''
import math

# Page 40
'''friends = ['musab anees', 'rana hassan', 'zubair amjad', 'zaeem sindhu', 'tazah gul']
friends.sort()
for friend in friends:
    print(friend.title())
print('')
message = " is my one of my friends."
[print(friend.title() + message) for friend in friends]'''

# Page 46-47
friends = ['musab anees', 'rana hassan', 'zubair amjad', 'zaeem sindhu', 'tazah gul']
message = ', I invite you to my home for dinner.'
'''friends.sort()
#[print(friend.title() + message) for friend in friends]
                    #OR
i = 0
l = len(friends)
while i < l:
    print(friends[i].title() + message)
    i = i+1'''

'''print(friends[0].title() + ' cannot make it to the dinner.')
friends.pop(0)
print(friends)
friends.append('hizbullah masood')
friends.sort()
message = ', I invite you to my home for dinner.'
#[print(friend.title() + message) for friend in friends]
                    #OR
i = 0
l = len(friends)
while i < l:
    print(friends[i].title() + message)
    i = i+1'''

'''friends.sort()
x = math.floor(len(friends)/2)
print(x)
friends.insert(0,'hizbullah masood')
friends.insert(x, 'khubaib waqar khan')
friends.append('umair latif')
#[print(friend.title() + message) for friend in friends]
#               OR
i = 0
l = len(friends)
while i < l:
    print(friends[i].title() + message)
    i = i+1

print('I can only invite two people.')
friends = [friend.title() for friend in friends]
message2 = ', I am sorry for not inviting you to dinner.' 
print('Mr. ' + friends.pop() + message2)
print('Mr. ' + friends.pop() + message2)
print('Mr. ' + friends.pop() + message2)
print('Mr. ' + friends.pop() + message2)
print('Mr. ' + friends.pop() + message2)
print('Mr. ' + friends.pop() + message2)
[print('Mr. ' + friend.title() + message) for friend in friends]
del friends
print(friends)'''

# Page 50
places = ['seoul', 'tokyo', 'vancouver','rome','paris']
places = [place.title() for place in places]
'''print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()
print(places)

#           OR
i = -1
l = -len(places)
while i >= l:
    print(places[i])
    i=i-1

print('I would like to visit at least ' + str(len(places)) + ' places.')'''


'''CHAPTER #4: WORKING WITH LISTS'''
# Page 60
'''fav_pizzas = ['behari', 'chicken supreme', 'fajita']
for pizza in fav_pizzas:
    print('I like ' + pizza.title() + ' pizza')
print('Above are some of the pizzas that I like.')

pets = ['cat', 'parrot', 'dog']
for pet in pets:
    print('A ' + pet + ' would make a great pet.')
print('These animals have nothing in common except that they make wonderful pets.')'''

# Page 64
'''for num in range (1,21):
    print(num)

million = [num for num in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))

odd_nums1 = []
for num in range(1,21,2):    
    odd_nums1.append(num)
print(odd_nums1)
#           OR    
odd_nums = [num for num in range(1,21,2)]
print(odd_nums)

table_of_3 = []
for num in range(1,11):
    x = num*3
    table_of_3.append(x)
print(table_of_3)

# multiples_of_3 = [num*3 for num in range(1,11)]
# print(multiples_of_3)

cubes = []
for num in range(1,11):
    x = num**3
    cubes.append(x)
print(cubes)

cubes = [num**3 for num in range(1,11)]
print(cubes)'''

# Page 69
'''places = ['seoul', 'tokyo', 'vancouver','rome','paris']
places = [place.title() for place in places]
places.sort()
print('The first three items of the list are: ')
print(places[0:4])
print('The last three items of the list are: ')
print(places[2:])
print(places)
print('The middle three items of the list are: ')
l = int(len(places)/2)
start = l - 1
end = l + 2
print(places[start:end])

my_pizza = ['pepperoni', 'cheese', 'veg']
friends_pizza = my_pizza[:]
my_pizza.append('fajita')
friends_pizza.append('chicken supreme')
print('My favorite pizzas are: ')
for pizza in my_pizza:
    print(pizza.title())
print('My friend\'s favorite pizzas are: ')
for pizza in friends_pizza:
    print(pizza.title())'''

# Page 71
'''for food in foods:
    print(food.title())'''