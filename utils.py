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
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
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
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lowerâ€˜ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
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



