# 4. Print the multiplication table of a given number.

table=int(input("Enter a number to print it's table: "))

for i in range (1,11):
    print(table,"x",i,"=",table*i)