#kaçış karakterleri-eğer metinsel bir ifedadeyi "" ile ifade eersek ama içerde de "" kullanacaksak kaçış karakterlerini kullanırız.
#  \\ bir kaçış karakteidir.

print(' it\'s a beatiful day outside')

#çok satıtlı değişgenler- """""" konulur

text="""pazartesi   
        sali
        çarşamba"""

print(text)

#for a in b:- ayı bye aktarma- h 

yumurta="kekiniz hazir"

for x in yumurta:
    print(x)

    #len- stringin uzunluğunu ölçer
print(len(yumurta))

#in- not in -var mı yok mu


kek="yumurta süt yağ şeker kabartma tozu vanilin"
y="süt"

print(y in kek)

print(y not in kek)