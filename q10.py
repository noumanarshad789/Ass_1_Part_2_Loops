# 10. Use a loop to count the number of digits in an integer.
num=int(input("Enter a number: "))
count=0
for i in str(num):
    count+=1

print(count)

