def factroial_itrative (n):
    """input =n
    result= n*(n-1)*(n-2).........1"""
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac
number=int(input("enter the no."))
print(factroial_itrative(number))

def factroial_recurive(n):
    if n==1:
        return 1
    else:
        return n*factroial_recurive(n-1)
number=int(input("enter the no."))
print("factorial using recursive merthod",factroial_recurive(number))

