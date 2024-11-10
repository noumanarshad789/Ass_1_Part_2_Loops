# 12. Print all prime numbers between 1 and 50.

for i in range(1,51):
    if i<=1:
        print(f"{i} is not a prime number")

    elif 2<=i<=9:
        if i==2 or i==3 or i==5 or i==7: 
            print(f"{i} is a prime number.")

        else:
            print(f"{i} is not a prime number.")

    elif i>9:
        if i%2==0 or i%3==0  or i%4==0  or i%5==0  or i%6==0 or i%7==0 or i%8==0 or i%9==0:
            print(f"{i} it is not a prime number.")

        else:
            print(f"{i} it is a prime number.")