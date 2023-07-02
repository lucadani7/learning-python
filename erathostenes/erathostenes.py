import bitarray


def erathostenesSieve(n):
    if n < 2:
        return []  # there are no prime numbers less than 2, so I'll return an empty list
    sieve = bitarray.bitarray(n + 1)
    sieve.setall(True)
    for i in range(4, n + 1, 2):
        sieve[i] = False
    p = 3
    while p ** 2 <= n:
        if sieve[p]:
            for i in range(p ** 2, n + 1, p):
                sieve[i] = False
        p += 2
    primes = list(filter(lambda x: sieve[x], range(3, n + 1, 2)))
    primes.append(2)  # 2 is the unique number which is even and prime at the same time, so I'll append the number 2 to the list
    primes.sort()
    return primes


n = int(input("n = "))
print(erathostenesSieve(n))
