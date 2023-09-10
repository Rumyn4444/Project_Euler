def is_palindrome(n):
    return str(n) == str(n)[::-1]
def find_palindrome_sums(limit):
    palindromes = []
    for start in range(1, limit):
        current_sum = start ** 2
        for end in range(start + 1, limit):
            current_sum += end ** 2
            if current_sum >= limit:
                break
            if is_palindrome(current_sum):
                palindromes.append(current_sum)
    return palindromes

palindrome_sums = find_palindrome_sums(1000)
print(sum(palindrome_sums))



# Solution 2
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def find_palindrome_sums(limit):
    squares = [i**2 for i in range(1, int(limit**0.5) + 1)]
    palindrome_sums = []
    for n in range(2, limit):
        if is_palindrome(n):
            for i in range(len(squares)):
                for j in range(i+1, len(squares)):
                    if sum(squares[i:j+1]) == n:
                        palindrome_sums.append(n)
                        break
    return palindrome_sums

palindrome_sums = find_palindrome_sums(1000)
print(sum(palindrome_sums))
