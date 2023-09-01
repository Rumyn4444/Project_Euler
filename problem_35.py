def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_circular_prime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:] + n_str[:i])):
            return False
    return True
circular_primes = [2]
for i in range(3, 1000000, 2): 
    if is_prime(i) and is_circular_prime(i):
        circular_primes.append(i)
        
print(len(circular_primes))
