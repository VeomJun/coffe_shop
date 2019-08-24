ice = 1500
count = 10
print('Hello, this is jun\'s cafe.')
print('We have 10 ice americanos. It\'s %d won each.' % (ice))
while True:
    money = int(input("Money please: "))
    if money == ice:
        print('=====================')
        print("Here's your coffee")
        count = count - 1
        print('We have %d coffe left.' % (count))
        print('=====================')
    elif money > ice:
        print('=====================')
        print("Here's your coffee")
        count = count - 1
        change = money - ice
        print('Here\'s your change. %d won.' % (change))
        print('We have %d coffe left.' % (count))
        print('=====================')
    elif money < ice:
        print('=====================')
        print("Sorry, not enough money.")
        print("Here's your money.")
        print('=====================')
    if count == 0:
        print('We\'re out of coffee. Thank you.')
        break