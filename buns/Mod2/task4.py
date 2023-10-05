a = int(input())
b = a
binary = ""
octal = ""
hexadecimal = ""

while a > 0:
    rem = a % 2
    binary = str(rem) + binary
    a = a // 2

a = b
while a > 0:
    rem = a % 8
    octal = str(rem) + octal
    a = a // 8

a = b
while a > 0:
    rem = a % 16
    hexadecimal = str(rem) + hexadecimal
    a = a // 16

if a < 0:
    print("Неверный ввод")

print(binary, octal, hexadecimal)
