flavors = ['Doritos', 'Lays', 'Oreo', 'Pringles']
prices = [2.0, 2.5, 3.0, 3.5]
# index          0           1            2           3
print('Welcome to Snack2Go Vending Machine! Please select your choice!')
print('----------------')
total=0
loop=True
while loop :
    print('0. Exit 1. Doritos 2. Lays 3. Oreo 4. Pringles')
    choice = int(input('Input Choose (0-4): '))
    if choice==0 :
      if total==0 :
        print('Order cancelled')
      loop=False
    else : #if choice!=0
      flavor = flavors[choice - 1]
      price = prices[choice - 1]
      print('>>', flavor, '$', price)
      quantity = int(input('Input Quantity (max 10) :'))
      total = total + (price*quantity)
      print('>>Total Price ($): ', total)
if total!= 0 :
  print('>>Grand Total Price ($): ', total)
  input_payment = int(input('Input Payment ($) : '))
  change = input_payment - total
  if change == 0 :
    print('Your change is $0.')
  elif change <0 :
    print('The machine did not receive enough amount for your purchase.')
  else :
    cents = int(change * 100)
    coins = 0
    bills = 0
    qty = cents // 500
    if qty > 0:
      print(qty, "bills of $5")
      bills = bills + qty
    cents = cents % 500
    qty = cents // 200
    if qty > 0:
      print(qty, "bills of $2")
      bills = bills + qty
    cents = cents % 200
    qty = cents // 100
    if qty > 0:
      print(qty, "coins of $1")
      coins = coins + qty
    cents = cents % 100
    qty = cents // 50
    if qty > 0:
      print(qty, "coins of 50 cents")
      coins = coins + qty
    cents = cents % 50
    qty = cents // 20
    if qty > 0:
      print(qty, "coins of 20 cents")
      coins = coins + qty
    cents = cents % 20
    qty = cents // 10
    if qty > 0:
      print(qty, "coins of 10 cents")
      coins = coins + qty
    cents = cents % 10
    qty = cents // 5
    if qty > 0:
      print(qty, "coins of 5 cents")
      coins = coins + qty
    cents = cents % 5
    if cents > 0:
      print(cents, "coins of 1 cent")
      coins = coins + cents
    print("Total coins are", coins, "and bills are", bills)
