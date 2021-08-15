'''CHAPTER #6: DICTIONARIES'''

# Page 102
# 6-1. Person
# Dictionary initialization
'''person = {}
# Storing key-value pairs
person['first_name'] = 'ramish'
person['last_name'] = 'masood'
person['age'] = 23
person['height'] = '5\' 11\'\''

#           OR 

person = {
    'first_name' : 'ramish',
    'last_name' : 'masood',
    'age' : 23,
    'height' : '5\' 11\'\''
    }

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['height'])

# 6-2. Favorite Numbers
# Dictionary initialization
favorite_numbers = {}
# Storing key-value pairs
favorite_numbers['ramish'] = 5
favorite_numbers['masood'] = 1820
favorite_numbers['hassan'] = 17
favorite_numbers['ahmed'] = 33
favorite_numbers['sanan'] = 480

#           OR

favorite_numbers = {
    'ramish' : 5,
    'masood' : 1820,
    'hassan' : 17,
    'ahmed' : 33,
    'sanan' : 480
}

print(favorite_numbers['ramish'])
print(favorite_numbers['masood'])
print(favorite_numbers['hassan'])
print(favorite_numbers['ahmed'])
print(favorite_numbers['sanan'])
print(favorite_numbers)

# 6-3. Glossary
# Dictionary initialization
python_dictionary = {
    'mutable' : 'Changeable. The user cannot perform functions on mutable objects.',
    'immutable' : 'Unchangeable. The user cannot perform functions on mutable objects.',
    'variable' : 'stores a value which can be changed.',
    'list' : 'stores multiple variables of same datatype.',
    'modulus operator (%)' : 'returns the remainder of two numbers.'
}
print('Mutable: ' + python_dictionary['mutable'])
print('Immutable: ' + python_dictionary['immutable'])
print('Variable: ' + python_dictionary['variable'])
print('List: ' + python_dictionary['list'])
print('Modulus operator: ' + python_dictionary['modulus operator (%)'])'''

#6-4. Glossary 2
# Dictionary initialization
'''python_dictionary = {
    'mutable' : 'Changeable. The user cannot perform functions on mutable objects.',
    'immutable' : 'Unchangeable. The user cannot perform functions on mutable objects.',
    'variable' : 'stores a value which can be changed.',
    'list' : 'stores multiple variables of same datatype.',
    'modulus operator (%)' : 'returns the remainder of two numbers.'
}
for key,value in python_dictionary.items():
    print('The meaning of the term ' + key.title() + ' is ' + value.lower())'''

# 6-5. Rivers
'''rivers = {
    'rhine' : 'france',
    'indus' : 'pakistan',
    'thames' : 'england'
}
for key,value in rivers.items():
    print('The river ' + key.title() + ' runs through ' + value.title())
print('The dictionary contains the following rivers: ')
for key in rivers.keys():
    print(key.title())
print('The dictionary contains the following countries: ')
for value in rivers.values():
    print(value.title())

#6-6. Polling
favorite_languages = {
    'ramish' : ['python','r'],
    'zubair' : 'c',
    'hassan' : ['c','C#','C++'],
    'musab' : ['c', 'python', 'java']
}
names = ['musab', 'zaeem', 'hizbullah', 'ramish']
for name in names:
    if name.lower() in favorite_languages.keys():
        print('Thank you ' + name.title() + ' for taking the poll. You like ' + str(favorite_languages[name]).title())
    elif name.lower() not in favorite_languages.keys():
        print('I invite you, ' + name.title() + ' for taking the poll.')

# Page 114-115
# 6-7. People

people = {
    'person1' : {
        'first_name' : 'ramish',
        'last_name' : 'masood',
        'age' : 23,
        'height' : '5\' 11\'\''
    },
    'person2' : {
        'first_name' : 'musab',
        'last_name' : 'anees',
        'age' : 24,
        'height' : '5\' 10\'\''
    },
    'person3' : {
        'first_name' : 'sannan',
        'last_name' : 'ali',
        'age' : 24,
        'height' : '5\' 6\'\''
}}
for name,characteristics in people.items():
    print('The information about is about ' + name)
    print('The first name is ' + characteristics['first_name'].title() + ' and the last name is ' + characteristics['last_name'].title())
    print('The age is ' + str(characteristics['age']) + ' and the height is ' + characteristics['height'] + '\n')

# 6-8. Pets
pet1 = {
    'name' : 'lucy',
    'specie' : 'cat',
    'color' : 'grey'
}
pet2 = {
    'name' : 'doggo',
    'specie' : 'dog',
    'color' : 'brown'
}
pet3 = {
    'name' : 'mithu',
    'specie' : 'parrot',
    'color' : 'green'
}
pet4 = {
    'name' : 'percy',
    'specie' : 'goldfish',
    'color' : 'orange'
}
pets = [pet1 , pet2 , pet3 , pet4]
for pet in pets:
    print('The name of the pet is ' + pet['name'].title() + '. It is a ' + pet['specie'] + '. Its color is ' + pet['color'] + '.' ) 

# 6-9. Favorite Places
favorite_places = {
    'ramish' : ['Tokyo', 'Istanbul', 'Toronto'],
    'umair' : ['Vancouver', 'Cairo'],
    'musab' : ['London']
}
for key,value in favorite_places.items():
    print('Favorite places of ' + key.title() + ' are:')
    for v in value:
        print(v.title())

# 6-10. Favorite Numbers
favorite_numbers = {
    'ramish' : [5, 25, 50],
    'masood' : [1820, 546],
    'hassan' : [17, 64],
    'ahmed' : [33, 67, 65, 4],
    'sanan' : [480]
}
for key, value in favorite_numbers.items():
    print('The favorite number/s of ' + key.title() + ' are:')
    for v in value:
        print(v)

# 6-11. Cities
cities = {
    'islamabad' : {
        'country' : 'pakistan',
        'continent' : 'asia'
    },
    'niger' : {
        'country' : 'nigeria',
        'continent': 'africa'
    },
    'havana' : {
        'country' : 'cuba',
        'continent' : 'north america'
    }
}
for key,value in cities.items():
    print('The name of the city is ' + key.title() + ' It is the capital of ' + value['country'].title() + '. ' + value['country'].title() + ' is located in ' + value['continent'].title() )

# 6-12. Extensions:
extra = {
    'tehran' : {
        'country' : 'iran',
        'continent' : 'asia'
}
}    
cities.update(extra)
print(cities)
'''