input_data = input()
comma_index = input_data.index(',')

i = input_data[:comma_index]
n = int(input_data[comma_index + 1:].strip())

if len(i) == 1 and 'a' <= i <= 'z':
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index_i = english_alphabet.index(i)
    new_index = (index_i + n) % 26
    k = english_alphabet[new_index]
    print(k)
else:
    print("Неверный символ i.")
