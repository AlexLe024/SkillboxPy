input_str = input()
vowels_count = 0
consonants_count = 0

vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

for char in input_str:
    if char.isalpha() and char in vowels_list:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1

print("Количество гласных:", vowels_count)
print("Количество согласных:", consonants_count)
