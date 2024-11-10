# 9. Write a program to print the first 10 Fibonacci numbers.

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

a=0
b=1
num=int(input("Enter a number: "))
if num==1:
    print(0)

elif num==2:
    print(a,b)

elif num>2:
    print(a)
    print(b)
    for i in range (2,num):
        c=a+b
        a=b
        b=c
        print(c)