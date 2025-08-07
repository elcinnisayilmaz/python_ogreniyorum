myBool=False    # boolean veri türü
print(type(myBool))
print(myBool)

x=None  # null none type veri türü
print(type(x))
print(x)

print("______________________")
name=b"elcin" 
print(type(name))
print(name)

print("______________________")
nameByte=bytes("elçin","utf-8")
print(type(nameByte)) 
print(nameByte) 

print("______________________")
nameByteArray=bytearray([65]) # ASCII tablosundaki karşılığını verir, bytetan farkı daha esnek olmasıdır.
print(type(nameByteArray)) 
print(nameByteArray) 

print("______________________")
nameByteArray2=bytearray("elcinn")
print(type(nameByteArray2)) 
print(nameByteArray2) 