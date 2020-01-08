#guess my no. it is between 1 to 50
#no of gusses left = 10
no_of_gusses = 1
while(no_of_gusses <=10):
    guess = int(input("guess the no.:\n"))
    if guess< 36:
        print("print greater no.")
    elif guess>36:
        print("enter smaller no.")
    else:
        print("winner")
        print(no_of_gusses ," tries taken")
        break
print(10-no_of_gusses ,"tries left")
no_of_gusses =no_of_gusses + 1
if(no_of_gusses>10):
    print("lost")
