# Input = [1,2,5,3,8,7,6,1]
# Output = [1,1,2,3,5,6,7,8]

# a = [1,2,5,3,8,7,6,1]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)

# -----------------------------------------------

# Write a program to display prime no. in a given range and also count the prime no. ?
# l = int(input("enter first number: "))
# end = int(input("enter last number: "))
# count = 0
# print("Prime numbers:")
# for num in range(l, end + 1):
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end =" ")
#             count += 1
# print("\nTotal prime numbers:", count)

# -----------------------------------------------

# Write a Program to find missing no. from given list ?

l = [1,2,3,4,6,7,8,9]

n = len(l) + 1
out = n * (n + 1) // 2
output = out - sum(l)