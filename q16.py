# 16. Create a program to calculate the sum of the digits of an inputted integer.
sum=0
user_input=int(input('Enter a number: '))

for i in str(user_input):
    sum=sum+int(i)

print(sum)