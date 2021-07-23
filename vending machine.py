#vending machine
#input
change  = 8.48
#process and input
cents = int(change*100)
coins = 0
bills = 0
qty = cents//500
if qty > 0 :
  print(qty, "bills of $5")
  bills = bills + qty
cents = cents%500
qty = cents//200
if qty > 0 :
  print(qty, "bills of $2")
  bills = bills + qty
cents = cents%200
qty = cents//100
if qty > 0 :
  print(qty, "coins of $1")
  coins = coins + qty
cents = cents%100
qty = cents//50
if qty > 0 :
  print(qty, "coins of 50 cents")
  coins = coins + qty
cents = cents%50
qty = cents//20
if qty > 0 :
  print(qty, "coins of 20 cents")
  coins = coins + qty
cents = cents%20
qty = cents//10
if qty > 0 :
  print(qty, "coins of 10 cents")
  coins = coins + qty
cents = cents%10
qty = cents//5
if qty > 0 :
  print(qty, "coins of 5 cents")
  coins = coins + qty
cents = cents%5
if cents > 0 :
  print(cents, "coins of 1 cent")
  coins = coins + cents
print ("Total coins are" , coins, "and bills are", bills)