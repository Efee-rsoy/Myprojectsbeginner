

def prime_finder(number):
    if number < 2:
        return False
    for divisor in range(2,number):
        if number % divisor == 0:
            return False 
    return True
        
print(prime_finder())