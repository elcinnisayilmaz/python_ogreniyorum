#isdigit- eğer string tamamen rakamlarddan oluşuyorsa true mesajı verir
text="24362"
result=text.isdigit()
print(result)
print("_______________________________________")
#isdentifier- eğer sayı ile başlamıyorsa, boşluk yoksa ve _ dışında bir işaret yoksa true mesajı verir.
a="elcin"
b="2elcin"
c="elcin3"
d="el cin"
e="el_cin"
f="el-cin"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())
print(f.isidentifier())
print("_______________________________________")

#isprintable- ekrana yazdırılabilir stringler varsa true mesajı verir.
text2="sucuk/ ?=-_,:..$ 123123"
print(text2.isprintable())
text3="sucuk \n salam" #\n ekrana yazılamadığı için false
print(text3.isprintable())

#isspace- eğer string tamamen boşluktan oluşuyorsa truedur
print("_______________________________________")
text4=" "
print(text4.isspace())

#istitle- eğer her kelimenin ilk harfi büyükse true mesajı verir
print("_______________________________________")
text5="Hello, welcome To my world"
print(text5.istitle())

#join
colors=("brown","bllack","pink","yellow","purple")
result2=",".join(colors)
print(result2) #brown,bllack,pink,yellow,purple

#ljust ve rjust #ljust stringi sola, rjust sağa yaslar, aralarında istediğimz kadar boşluk gelir.
text="yumurta"
print(text.ljust(10,"-"),) #yumurta---
