a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)

result = euclidean_gcd(a, b)
print(f"Наибольший общий делитель чисел {a} и {b} равен {result}")
