#strip- sağ ve soldaki gereksiz boşlukları kaldırır
text="    sucuk   "
print(text.strip())

print("___________________")

#lstrip and rstrip- lstrip soldaki gereksiz boşlukları, rstrip ise sağdaki gereksiz boşlukları siler
print(text.lstrip())
print(text.rstrip())

print("___________________")

#maketrans and translate- stringlerin yerini değiştirir.
text2="Hello, Python"
result=str.maketrans("P","T")
print(text2.translate(result))

print("___________________")

#partition- bir string grubunun içerisinde bir stringi seçer ve öncesi,kendisi ve sonrası farjlı gruplara ayrılır
text3="I could eat strawberry all day"
print(text3.partition("strawberry"))

print("___________________")
