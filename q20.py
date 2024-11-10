# 20. Create a program that simulates a countdown timer starting from a given number down to zero.

user_input=int(input("Enter a number: "))
for i in range(user_input,-1,-1):
    print(i)