#A python program demonstarting the fibonacci sequence

def fibonacci(n):
    if n < 0:
        print("Incorrect input! Enter a non-negative integer.") 
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(fibonacci(10))