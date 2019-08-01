'''Starting a new program to evaluate your income
factor in expenses and use a common formula to
reccommend certain living arrangements based on
given data for the city of San Diego.'''

#The goal of v0.7 is to add an error system.
#Hope to run more than one iteration after errors.


#program into
print('Welcome to quick budget!\n')
print('This quick program is to help give the user an idea of what to budget for expenses like food, housing, and savings. \n')
print('*Notice this will only be as accurate as the information input for all values. \n')


#Initial income to draw budget from
#Taking the average 1br rent in San Diego
#Which was $1955 in 2019 then multiply by 3 to get reccommended income for single income


while True:
    try:
        income = float(input('Total monthly income after tax?\n(Take home money)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

if income >= 5865:
    print('Great! With an income like that you can chose to live alone or with a roomate to cut down costs.\n')
else:
    print('It is reccommended to find a at least one roommate to make living costs more manageable.\n')

print('Okay time to calculate expenses. \nTry to be as accurate as possible.\n')


#average spending on rent
while True:
    try:
        rent = float(input('Rent?\n(Housing,rent,mortgage)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

#average spending on utilities
while True:
    try:
        utilities = float(input('Utilities?\n(include internet,tv,water,sewage,energy,trash)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

#average spending on transportation related items
while True:
    try:
        transportation = float(input('Transportation?\n(Vehicle, Insurance, Bus, Gas)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

#average food related costs
while True:
    try:
        food = float(input('Food?\n(Groceries, Eating out, Supplements)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

#average spending on other monthly expenses
while True:
    try:
        other = float(input('Other monthly expenses?\n(Phone, Netflix, Gym)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

#average planned savings
while True:
    try:
        savings = float(input('Savings?\n(Roth, 401k, Standard savings account)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break

#average debt being paid off each month    
while True:
    try:
        debt = float(input('Debt?\n(School loans, CC Debt, Owe family)\n'))
    except ValueError:
        print('Sorry, please enter a number.\n')
    else:
        break


#Totaling all expenses
expenses = rent + savings + debt + transportation + utilities + other + food
extra_money = income - expenses

print("Your total expenses are " + str(expenses) + ' and with that you have ' + str(extra_money) + ' of extra money each month!')

experience = input("Were you happy with this experience?")



