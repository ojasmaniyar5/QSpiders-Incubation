# if else.

#1 Write a program to check the if the sum of 2 number is greater than 100

#2 Write a program if the first and last character of string is same ?

#3 Write a program to if the product of 2 number is even

#4 Write a program in the given character is in uppercase or not ?

#5 Write a program if string contains space ?

#6 Write a program to check if the number as 3 digits(take int value from user) 

#7 Write a program to find greatest of two number ?

#8 write a program to print square of given int if it is even, print cube of the num if it odd ?

#9 write a program to check a special symbol which given by user ?

#10 consider a str input and print the concadinating sting of first and last char only if the length more then 5 ?

#11 consider two input whether both are pointing to both location.

#12 consider a tuple and check wheather a tuple is homogenuos or hetrogeonus ?

#13 write a program to check wether the given string is keyword or not ?

#14 Consider a list input print the value at given index if the length is even else print the value at odd index ?

#15 write program to check if the given list is empty or not ?

#16 write a program to check if the sum of first and last digit of a given number is even or odd?

#17 write a program to check if the difference between two number is a multiple of 7 ?

#18 write a program to check wether the given string is having middle character or not ? 

#19 write a program to check if two string are of equal length but not same ?


#...................................................

#elseif.

#20 write a program to check wether the enter character is in uppercase, lowercase, digit or in special character ?

#21 write a program to check wether a integar is in single digit, doble digit, triple digit or more than three ?

#22 Write a program to find geatest of three number ?

#23 Consider a character input, if it is in uppercase print the first digit of its skee value, if it is lower case than print the last digit od skee value, if it is digit print the remainder when is is divided by 3 else print the same character ?

#24 write a program wether the given two points are in lines given qudrants ?

#25 Consider a character a input if it is in uppercase case convert it into lowercase, if it is in lowercase convert it into uppercase if it is in digit find squre of it and if it special character add 5 to ascc value and print value. print without using any function ?

#26 write a program to check wether the number is divisible only by 5 and divisible only by 2 or both by 2 and 5 ?

#27 Write a program to check if the given character is vowel consonent digit or special character ?

#28 Write a program to classified an angle based on its degree ?


#..........................................................

# nested if

#29 write a program to print middle value of list only if it is string ?

#30 Write a program to print first value of tuple only if it is string having length more than 5 and string should bee palindrone ?

#31 Write a program to login in an application with valid username and valid password (enter the password only if username is valid) ?

#32 Write a program to last value of string only if it palindrome string starting with vowels ?

#33 Write a program to print reverse string only if it is strating with vowel ending with consonent and it should have middle value ?

#34 Write a program to find greatest among three in numbers ?

#35 write a program to find greatest among 4 numbers ?

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print(num1, "is the greatest.")
        else:
            print(num4, "is the greatest.")
    else:
        if num3 > num4:
            print(num3, "is the greatest.")
        else:
            print(num4, "is the greatest.")
else:
    if num2 > num3:
        if num2 > num4:
            print(num2, "is the greatest.")
        else:
            print(num4, "is the greatest.")
    else:
        if num3 > num4:
            print(num3, "is the greatest.")
        else:
            print(num4, "is the greatest.")
