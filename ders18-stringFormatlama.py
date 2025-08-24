#format
yas=11
isim="elcinn"
cumle="benim adim {},ben {}yasindayim".format(isim,yas)
#print(cumle)

#f string

cumle2=f"benim adim {isim}, ben {yas} yasindayim."

#f-ondalıklı sayıya çevirir :.2f denilirse 2 basamaklı ondalk sayıya çevirir.

kilo=23.1276453463754
cumle3=f"unun kilosu {kilo:.3f} lira"

#print(cumle2)
#print(cumle3)

not1=input("1. dönem sonucunu giriniz:")

not2=input("2. dönem sonucunu giriniz:")

ortalama=(float(not1)+float(not2))

sonuç=f"ortalamanız {ortalama}'dır"