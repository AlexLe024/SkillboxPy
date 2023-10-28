input_str = input("Введите числа через пробел: ")
numbers = [int(x) for x in input_str.split()]

def check_numbers(numbers):
    if len(set(numbers)) == 1:
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

result = check_numbers(numbers)
print(result)
