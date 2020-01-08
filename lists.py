list = [["ankit",18], ["harry",16]]
for a,age in list:
    print(a)
list = ["ankit","rahul","harry", 2,3,4,5,6,7,8,33,44,66,78,98,99,34,]
for object in list:
    if str(object).isnumeric() and object>8:
        print(object)