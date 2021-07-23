flavors = ['Vanilla', 'Strawberry', 'Chocolate', 'Mocha']
prices = [2.0, 2.5, 3.0, 3.5]
# index          0           1            2           3
print('Hi there! Welcome to our Hello Ice Cream Shop! Here we offer 4 wonderful flavors of ice cream.')
print('----------------')
total = 0
loop = True
while loop :
    print('1. Vanilla 2. Strawberry 3. Chocolate 4. Mocha')
    choice = int(input('Input Choose (1-4) : '))
    if choice == '0' :
        if total == '0' :
            print ('Order cancelled')
        loop = False
    else : 
        flavor = flavors[choice - 1]
        price = prices[choice - 1]
        print('>>', flavor, '$', price)
        quantity = int(input('Input Quantitiy (max 10) :'))
        total = price*quantity
        print('>>Total Price ($): ', total)
if total != 0
    print('>>Grand Total Price ($): ', total)
    input_payment = int(input('Input Payment ($) : '))
    change = input_payment - total
    print('Change ($) : ', change)
    print('Thank you for shopping!Come back soon :)')
