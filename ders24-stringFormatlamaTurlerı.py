#:      pozitif sayının soluna 1 fazladan boşluk bırakır
text="sicaklik bugün {: } ile {: } arasinda değişecekmis"
print(text.format(-1,13))

#:,     binlik sayıların aralarına virgül atar
text2="the universe is {:,} years old"
print(text2.format(2345876543229483719793))

#:_     binlik sayıların aralarına _ atar
text3="the universe is {:_} years old"
print(text3.format(2345876543229483719793))

#:b     sayının binary versiyonunu yazar
text4="the binary version of {0} is {0:b}"
print(text4.format(3))

#:c unicode versiyonunu normal hal ile yazar
text5="the binary version of {0} is {0:c}"
print(text5.format(350))

