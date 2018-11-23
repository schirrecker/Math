import random
import time

def Factorial(n):
    f = 1
    i = 1
    while i < n:
        f = f * (i+1)
        i += 1
    return f
  
def compLists(list1, list2):
    comp = False
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                comp = True
            else:
                comp = False
    return comp
'''
print(compLists([1, 2, 3], [1, 2, 3]))
print(compLists([1, 2, 3], [1, 3, 2]))
print(compLists([1, 2, 3], [1, 2]))
'''

size = 145
print ("size: " + str(size))
print ("----------------------------------------------")
print ("Permutations :" + str(Factorial(size)))
print ("----------------------------------------------")


items = list(range(size))
lottery_winner = list (items)
random.shuffle(lottery_winner)



attempt = 0
NotWon = True
while NotWon:
    attempt += 1
    random.shuffle(items)
    print (*items)
    if compLists(items, lottery_winner):
        print ("You won the lottery in " + str(attempt) + " attempts")
        NotWon = False


'''
RandFoo = []

def Random(List, Length):
    global RandFoo
    for i in range(Length):
        RandFoo.append(random.choice(List))
    
while True:
    Random(foo, 10)
    print(*RandFoo)
    time.sleep(1)
'''


