#count- aradğımız karakterin kaç tane olduğunu söyler

text="welcome to my world. my world is python"
result=text.count("world",11,22)
print(result)

#startswith- aradığımız karakterle başlayıp başlamadığını söyler

result2=text.startswith("welcome")
print(result2)

#endswith- aradığımız karakterle bitip bitmediğini söyler

result3=text.endswith("welcome")

print(result3)
#expandtabs- tab boşluklarını istediğimiz kadar boşlukla değiştirir

text2="p\ty\tt\th\to\tn"

print(text2)
print(text2.expandtabs(2))
print(text2.expandtabs(4))
print(text2.expandtabs(6))
print(text2.expandtabs(10))

#find- aradığımız karakterin kaçıncı indexte olduğunu söyler

result4=text.find("my")
print(result4)

#index- aradığımız karakterin kaçıncı indexte olduğunu söyler. find ile aynı ama bulamazsa hata verir.

result5=text.index("my")
print(result5)

#isalnum- stringin sadece harf ve rakamlardan oluşup oluşmadığını söyler.

result6=text.isalnum()
print(result6)

#isalpha- stringin sadece harflerden oluşup oluşmadığını söyler.

result7=text.isalpha()
print(result7)

#isascii- stringin sadece ascii karakterlerden oluşup oluşmadığını söyler.

result8=text.isascii()
print(result8)

#isdecimal- stringin sadece ondalık sayılardan oluşup oluşmadığını söyler.

result9=text.isdecimal()
print(result9)