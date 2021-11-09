#pseudo_random

import random
seed=random.randint(1, 50)
a=123123
c=246
m=12**5
numbers=[seed]
count=0


while True:
    number=(a*seed+c)%m
    seed=number
    count+=1
    print(number)
    if number in numbers:
        break
    else:
        numbers.append(number)
print(count, "unique number")
    


