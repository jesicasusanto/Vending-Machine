import random

def tossDie(pos,pname) :
    die = random.randint(1,6)
    print (pname + ':', pos, '+', die, end='=')
    pos = pos + die
    print(pos)
    return pos

p1, p2 = 0, 0
pname1 = input('Player Name 1 : ')
pname2 = input('Player Name 2 : ')
round = 1

while (p1 != 100 and p2 != 100) :
    print('n\Round', round)
    p1 = tossDie (p1, pname1)
    p2 = tossDie (p2, pname2)
    if (p1>100) :
        p1 = 200 - p1
    if (p2>100) :
        p2 = 200-p2
    round += 1
