import random
print(random.sample([x for x in range(100,201) if not x%2],5))