#find and rfind- find aradığınız stringin indexsini söyler rfind ise eğer stringden birden fazla varsa sonuncusunu verirs
text="strawberry is my favorite fruit.my"
print(text.find("my"))
print(text.rfind("my"))

#splitlines- her alt satıra geçtiğimizde stringi ayırır
text2="strawberry is my\n favorite \n fruit"
print(text2.splitlines())

#zfill- stringin başına istedğimiz kadar sıfır vırakır
text3="hello python"
print(text3.zfill(15))