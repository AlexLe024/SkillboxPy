base = int(input("Введите основание: "))
exponent = int(input("Введите степень: "))

def fast_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = fast_power(base, exponent // 2)
        return half_power * half_power
    else:
        return base * fast_power(base, exponent - 1)

result = fast_power(base, exponent)
print(f"{base}^{exponent} = {result}")
