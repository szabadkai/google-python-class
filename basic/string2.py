#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    # +++your code here+++
    if len(s) >= 3 and s[len(s)-3:len(s)] != 'ing':
        s = s + 'ing'
    elif len(s) >= 3:
        s = s + 'ly'
            
    return s 


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    # +++your code here+++
    a = s
    for index in range(0, len(s)):
        for x in range(0,len(s)-index):
       # print (s[index])
            if s[index:index+3] == 'not' and s[index + x:index+ x +3] == 'bad' and s[-1] != 'd' :
                a = s[0:index] + 'good' + s[-1]
            elif s[index:index+3] == 'not' and s[index + x:index+ x +3] == 'bad' :
                 a = s[0:index] + 'good' 
                
    return a 
         


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    afront = ['']
    bfront = ['']
    aback = ['']
    bback = ['']
    final = ['']
    
    if len(a) % 2 == 0:
        afront = a[0:round((len(a)/2))]
        aback = a[round((len(a)/2)):len(a)]
        
    elif len(a) > 3:
        afront = a[0:round((len(a)/2))+1]
        aback = a[round((len(a)/2))+ 1:len(a)]
        
    elif len(a) < 4 and len(a) % 2 != 0:
        afront = a[0:round(len(a)/2)]
        aback = a[round(len(a)/2):len(a)]
        
        
        
    if len(b) % 2 == 0:
        bfront = b[0:round((len(b)/2))]
        bback = b[round((len(b)/2)):len(b)]
        
    elif len(b) > 3:
        bfront = b[0:round((len(b)/2))+1]
        bback = b[round((len(b)/2))+ 1:len(b)]
   
    elif len(b) < 4 and len(a) % 2 != 0:
        bfront = b[0:round(len(b)/2)]
        bback = b[round(len(b)/2):len(b)]
        
    final = afront + bfront + aback + bback
    
    return final 
        

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print('\nnot_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print('\nfront_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
