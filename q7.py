# 7. Find the factorial of a number using a while loop.

num=int(input("Enter a number: "))
Fact=1

while num>=1:
    Fact=Fact*num
    num-=1

print(Fact)