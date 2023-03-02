import random

print(random.randint(6,11))
print(random.randrange(3,9))

i = ["apple","banana","cherry"]
print(random.choice(i))

l=[10,20,30,40]
random.shuffle(l)
print(l)

r=random.random()
print(r)

u=random.uniform(3,9)
print(u)