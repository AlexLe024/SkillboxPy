word = input("Введите слово: ")

def is_palindrome(word):
    return word == word[::-1]

def make_palindrome(word):
    if is_palindrome(word):
        return word
    else:
        return word + word[::-1]

palindrome = make_palindrome(word)

if palindrome:
    print("Палиндром на основе введенного слова:", palindrome)
else:
    print("Нельзя составить палиндром из данного слова.")
