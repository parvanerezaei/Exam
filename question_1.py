#!/usr/bin/env python
# coding: utf-8


def repeatFunc(strInput,n):
    repNum =int(n/len(strInput))         # This is used to calculate new string length
    newStr=repNum*strInput               # New string regardless of length
    result=[]
    for i in range(0,n):                 # Apply length restrictions
        result.append(newStr[i])


    print("Number of 'a' s in the new string: {0} ".format(result.count("a")))
    return result.count("a")
   

#example
# repeatFunc("abcac",10)


