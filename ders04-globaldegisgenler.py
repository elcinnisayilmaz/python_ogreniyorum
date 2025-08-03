#global variables
text="marvellous"

def myfunction():
    global x  
    x="fantistic"
    #print("python is "+text)

myfunction()
print("python is "+x)