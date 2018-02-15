# utils.py
# Math library
# Author: SÃ©bastien CombÃ©fis
# Version: February 8, 2018
from math import sqrt
def fact(n):
    if n==0:
        return 0
    result=1
    while n>0:
        resut= result*n
        n-=1
        return result

def roots(a, b, c):
    delta= b**2-4*a*c
    if delta>0:
        root1= (-b+sqrt(delta))/(2*a)
        root2= (-b-sqrt(delta))/(2*a)
        roots=root1,root2
    elif delta==0:
        roots= (-b/(2*a)),
    else roots=()
    return roots

def integrate(function, lower, upper):
    intervalle=upper-lower
    dx=intervalle/1000
    x1=lower
    x2=x1+dx
    result=0
    while x1!=upper:
        area= (function(x1)+function(x2))*(x2-x1)/2
        result+=area
        x1=x2
        x2=x1+dx
    return result



if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
   print(integrate('x ** 2 - 1', -1, 1))



