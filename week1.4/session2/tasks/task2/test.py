def factorial( n ):
        if n == 1: # base case
            return 1
        return n*factorial(n-1) # recursive call reducing n
while True:
    print(factorial(999)) # result will be 120