str_a=input("Please enter the number of inputs you want for this fizzbuzz game: ")
if str_a=="":
    a=100
else: a=int(str_a)

def fizzbuzz1(n):
    for i in range(1,n+1):
        if i%5==0 and i%3==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

def fizzbuzz2(n):
    for i in range(1,n+1):
        output=""
        if i%3==0:
            output +="fizz"
        if i%5==0:
            output +="buzz"
        if output=="":
            output=i
        print(output)

def fizzbuzz3(a):
    print(list("fizz"*(i%3<1)+"buzz"*(i%5<1) or i for i in range(1,a+1)))

fizzbuzz1(a)
fizzbuzz2(a)
fizzbuzz3(a)

input("Press enter to exit;")

