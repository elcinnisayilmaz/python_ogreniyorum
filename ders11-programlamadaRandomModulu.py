import random
#choice
#mylist=["elma","armut","muz","üzüm","karpuz"]
text="elcin" #eğer bir kelime verirsek içindeki rasgele bir harfi verir.

#print(random.choice(text))

#choices

list2=["beyaz","mor","turuncu","kirmizi"]

print(random.choices(list2,weights=(1,10,1,1),k=2))
#weightsda hangisine daha çok ağırlık vereceğini yüzdelik açısından gösterirsin.
#k kaç tane rasgele seçeceğini söyler.

#shuffle

list3=["1","2","3","4","5","7"]

random.shuffle(list3) #shuffle listeyi rasgele karıştırır

print(list3)

#sample- verdiğin listeden istediğin sayı kadar rasgele veri verir.

print(random.sample(list3,k=3))

#uniform- verdiğimiz iki sayı arasıda rasgele bir ondalıklı sayı verir.

print(random.uniform(20,45))

#triangular-uniformdan farkı ikiden fazla sayı arasında rasgele ondalıklı sayı üretir.


