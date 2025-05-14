# Lambda Function
# A lambda function is a small anonymous function that can take any number of arguments but can only have one expression.
# It is often used for short, throwaway functions that are not going to be reused elsewhere in the code


# Write a program to check the string is palindrome or not if it false print reverse using lambda function.
# n = lambda x: x[::-1]
# s = input('Enter the string: ')
# if s == n(s):
#     print('The string is palindrome')
# else:
#     print('The string is not palindrome')
#     print('The reverse of the string is:', n(s))


# Write a program of following given list using lambda function:
# input : l = [1,2,3,4,5]
# output : [1,4,9,16,25]

# n = lambda x: x**2
# l = [1, 2, 3, 4, 5]
# l1 = list(map(n, l))
# print(l1)


# Write a program of following given list using lambda function and filter function:
# input : l1 = [1,2,3,4,5]
# output : [1,4,9,16,25]

n = lambda x: x**2
l1 = (map(suqr,[1, 2, 3, 4, 5]))
print(l1)