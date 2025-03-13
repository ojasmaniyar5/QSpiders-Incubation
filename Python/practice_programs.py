### write a program to print the multiplication table ?
##
##n = int(input("Enter a number: "))
##
##for i in range(1, 11):
##    print(f"{n} x {i} = {n * i}")
##

#---------------------------------------------------------------

##n = int(input('Enter a Number : '))
##i = n
##res = 0
##while i > 0:
##    rem = i % 10
##    res += rem ** len(str(n))
##    i //= 10
##if res == n:
##    print('Armstrong')
##else:
##    print('Not Armstrong')
##

#--------------------------------------------------------------
# To Find Vowels in given list.
##l = [1,2,3,2+3j,True,'Program','Python','ABC']
##for i in l:
##    if type(i) == str:
##        for j in i:
##            if j in 'AEIOUaeiou':
##                print(j,end='')

#--------------------------------------------------------------

##l = [1,2,3,'Python','ABC',3+2j]

##o/p = {'Program','Program','ABC','ABC'}



def max_substring(s):
    ms = ''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub > ms:
                ms = sub
    return ms

s = 'baca'
print(max_substring(s))  # Output: 'ca'

