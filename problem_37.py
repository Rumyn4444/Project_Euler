def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_vybr_prime(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:i+1])):
            return False
    return True
list_prime = [i for i in range (11, 1000000) if is_vybr_prime(i)]

print (sum(list_prime))
