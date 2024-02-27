def power(c,e,n):
    m = 1
    print('cen', c, ' ', e, ' ', n)
    while e > 0:
        m = m * c
        e -= 1

        if (m > n):
            m = m % n
    return m

def modular_power(base, exp, mod):
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
        if (result > mod):
            result = result % mod
    return result

def main():
    c = 447
    d = 523
    n = 841

    print(pow(c,d,n))
    result = power(c,d,n)
    print (result)
    result = modular_power(c,d,n)
    print(result)

main()