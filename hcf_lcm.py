#code to find out HCF of a number
#we are going to use a simple algorithm for making this code
import sys

print("Welcome to HCF calculator")
first = int(input(print("Enter the first number: ")))
second = int(input(print("Enter the second number: ")))
hfc = 1

def hcf(num, num2):
    num = first
    num2 = second
    for i in range(1, min(first, second)+1):
        if num % i ==0 and num2%i==0:
            hfc = i
            
            
    print("The HCF of this number is: ", i)        
        

hcf(first, second)