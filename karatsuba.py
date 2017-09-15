#Karan Sodhi
#Karatsuba multiplication algorithm
#it is assumed that the number of digits in a number is of the form n=2**k

#Function to carry out the recursive karatsuba multiplication
def karatsuba(X,Y,n):
    n_half=n/2
    if (n==1):
        T=X*Y
    else:
        #divide the digits of input numbers in halves
        X_1=X/(10**n_half)
        X_2=X%(10**n_half)
        Y_1=Y/(10**n_half)
        Y_2=Y%(10**n_half)
        #recursive calls to compute the product of two numbers
        U=karatsuba(X_1,Y_1,n_half)
        V=karatsuba(X_2,Y_2,n_half)
        W=karatsuba(X_1-X_2,Y_1-Y_2,n_half)
        Z=U+V-W
        T=(10**n)*U+(10**(n/2))*Z+V
    return T

#Function to find the number of digits in the input numbers
def size(X):
    n=0
    while(X!=0):
        if(X%10!=0):
            n=n+1
            X=X/10
    return n

#Function to check if my karatsuba algorithm implementation
#spits out right results
def mult_check(X,Y):
    return X*Y

def main():
    #Get inputs from user
    X=input("Enter number 1:")
    Y=input("Enter number 2:")
    #Find number of digits in the input numbers
    #uncomment "size(X)" for the program to figure out the number of digits in
    #the input number by itself; however this makes the program slower! 
    n=64#size(X)
    #Carry out multiplication using Karatsuba multiplication algorithm
    T=karatsuba(X,Y,n)
    #Carry out multiplication using python multiplication operator
    product=mult_check(X,Y)
    print "The output of multiplying the two input numbers using Karatsuba algorithm is:",T
    print "The out of multiplying the two input numbers using the multiplication opreator is:",product

main()
