x = 10 #global
def f1(n):
    global x
    x = 5
    x =x+50
    print(x)
    print(n,"i have printed")
f1("this is me")
print(x)


def f2():
    a=60
    def f3():
        global a
        a=70
    print("before calling f3",a)
    f3()
    print("after calling f3 ",a)

f2()
print(a)
