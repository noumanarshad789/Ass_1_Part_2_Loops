# 15. Print the sum of even and odd numbers separately up to a given number.

even_sum=0
odd_sum=0

for i in range (1,21):
    if i%2==0:
        even_sum=even_sum+i

    else:
        odd_sum=odd_sum+i

print(even_sum)
print(odd_sum)