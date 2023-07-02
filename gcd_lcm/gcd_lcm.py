def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


while True:
    a = int(input("a = "))
    b = int(input("b = "))
    if a >= 0 and b >= 0:
        break
GCD = gcd(a, b)
print("gcd(" + str(a) + ", " + str(b) + ") = " + str(GCD))
LCM = lcm(a, b)
print("lcm(" + str(a) + ", " + str(b) + ") = " + str(LCM))
