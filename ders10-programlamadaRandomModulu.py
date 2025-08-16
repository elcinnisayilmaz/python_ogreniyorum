import random
#random sürekli rasgele sayı verir.

"""random.seed(8) #seed rasgele olan sayının sabit olmasını sağlar.

print(random.random())

print(random.random())

print(random.random())"""
#getstate sonrakini kopyalamasını sağlar.
#setstate önceki aldığımız sayıyı verir.
"""print(random.random())

state=random.getstate() 

print(random.random())

random.setstate(state)

print(random.random())"""

#print(random.randrange(86)) #8 bit büyülüğünde sayı elde eder.

print(random.randrange(1,10)) #1-10 arası sayı söyler,10 dahil etmez.

print(random.randint(1-10))#1-10 arası sayı söyler.1 de 10 da dahil


