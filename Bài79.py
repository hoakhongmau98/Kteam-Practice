import random
print(random.sample([x for x in range(1,10001) if x%5==0 and x%7==0],5))