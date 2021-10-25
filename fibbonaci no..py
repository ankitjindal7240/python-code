#this program is completly created by me without any help
# an example of recursion where func is calling itself
def fibbonaci(n):
    """fibbonaci no. 0 1 1 2 3 5 8 13 21......"""
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)
number= int(input("enter the no."))
print(fibbonaci(number))
