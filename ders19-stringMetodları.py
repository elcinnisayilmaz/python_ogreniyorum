#capitalice- stringin ilk harfini büyük yazar

text="hel2lo, weLcome TO my world, HOW is IT going?"

result=text.capitalize()
print(result)
print("...")

#casefold
result2=text.casefold()
print(result2)
print("...")

#title- her kelimenin ilk harfini büyük yazar.

result3=text.title() #title bir rakamdan sonraki harfi büyük yazar.
print(result3)
print("...")
#swapcase- büyük harfleri küçük, küçük harfleri büyük yazar. yani değişim-takas yapar

result4=text.swapcase()
print(result4)
print("...")

#islower-eğer tüm harfler küçükse true mesajı verir
text2="welcome to my world"
result5=text2.islower()
print(result5)
print("...")

#isupper- eğer tüm harfler büyük ise true mesajı verir

result6=text2.isupper()
print(result6)
print("...")

#center- metni ortalar.
text3="hello python"
result7=text3.center(30,"*")
print(result7)