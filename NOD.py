def gcd(a, b):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)

print('Вычисление наибольшего общего делителя.')
gcd(4782, 698)