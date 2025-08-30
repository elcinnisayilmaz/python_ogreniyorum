#formatlama
#1. yöntem
text="the price is only {price:.2f} turkish lira"
print(text.format(price=70))

#2. yöntem
text2="my name is {fname} I'm {age} years old".format(fname="elcin",age=11)
print(text2)

#3. yöntem
text3="my name is {0} I'm {1} years old".format("elcin",11)
print(text3)

#format biçimlendirme
#:<     yanına yazdığınız sayı kadar boşluk bırakır formatlarken yazdığınız sayıyı sola hizalar

text4="dondurmamda {:<5} top varrrrr"
print(text4.format(5))

#:>     yanına yazdığınız sayı kadar boşluk bırakır formatlarkenki yazdığınız sayıyı sağa hizalar

text4="dondurmamda {:>5} top varrrrr"
print(text4.format(5))

#:^     yanına yazdığınız sayı kadar boşluk bırakır farmatlarkenki yazdığınız sayıyı ortalar

text5="dondurmamda {:^5} top varrrrr"
print(text5.format(5))

#:=     

text6="bugün hava {:=5} derece"
print(text6.format(-5))

#:+ ve :-     artı veya eksiği matematiksel işsret olarak değil de pozitif veya negaitf olarak göstermek icinler

text7="sicaklik {:+} ve {:+} arasinda değisiyor"
print(text7.format(-3,5))