
# List , dictionary

# dictionary creation === OBJECT
orders = {
    'wings':0,
}


print('Welcome to the Snakes Cafe')
print('Please see our menu below')
print('to quit any time type "quit"')

# lists

apps = ['Wings','Cookies','Spring Rolls']
ents = ['Salmon','Steak','Meat Tornado','A Literal Garden']
dess = ['Ice  Cream','Cake','Pie']
drnk = ['Coffee','Tea','Unicorn Tears']

# Printing loops
length = len(apps)

for i in range(length):
    print(apps[i])

length = len(ents)

for j in range(length):
    print(ents[j])

length = len(dess)

for k in range(length):
    print(dess[k])

length = len(drnk)

for l in range(length):
    print(drnk[l])



user_input = input('Please enter a item to order')


orders['wings'] += 1

wing_order = orders['wings']

# print(orders['wings'])

print(wing_order)


print(user_input)