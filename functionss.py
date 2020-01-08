'''a= 9
b= 8
c = sum((a,b))  #builtin functions
print(c)'''
#user defined functions
def f1(a,b):
    print("hello you nare in function 1\n", a+b)
f1(5,7)
def f2(a,b):
    """ this function is used to calculate average"""
    avg =(a+b)/2
    #print(avg)
    return avg
#v= f2(4,9)
#print(v)
print(f2.__doc__)
