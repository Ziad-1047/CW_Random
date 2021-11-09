#true_random

import time
s=time.time()
a=123123
c=246
m=12**5
numbers=[s]
count=0


while True:
    n=(a*s+c)%m
    s=n
    count+=1
    print(n)
    if n in numbers:
        break
    else:
        numbers.append(n)
print(count, "unique number")