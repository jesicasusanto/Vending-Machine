flavors = ['Vanilla', 'Strawberry', 'Chocolate', 'Mocha']
prices   = [   2.0   ,     2.5     ,    3.0     ,   3.5  ]
#index          0           1            2           3
print ('Point of Sales')
print('----------------')
print('1. Vanilla 2. Strawberry 3. Chocolate')
choice = int(input('Input Choose (1-4) : '))
flavor = flavors[choice-1]
price = prices[choice-1]
print('>>', flavor,'$', price)
quantity = int(input('Input Quantitiy (max 10) :'))
total = prices[choice-1]*quantity
print('>>Total Price ($): ', total)
input_payment = int(input('Input Payment ($) : '))
change = input_payment - total
print('Change ($) : ', change)