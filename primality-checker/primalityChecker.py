def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    return isPrimeHelper(n, 3)


def isPrimeHelper(n, divisor):
    if n % divisor == 0:
        return False
    elif divisor ** 2 > n:
        return True
    return isPrimeHelper(n, divisor + 2)


n = int(input("n = "))
message = str(n) + " is prime" if isPrime(n) else str(n) + " is not prime"
print(message)
