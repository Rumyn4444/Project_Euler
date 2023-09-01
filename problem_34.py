def factorial(a):
    fact_number = 1
    for i in range (1, a+1):
        fact_number *= i
    return fact_number
def factorial_check(number):
    suma_fact = sum (factorial(int(i)) for i in str(number))
    return suma_fact == number
list_fact = [i for i in range (3, 100000) if factorial_check(i)]

print (sum(list_fact))
