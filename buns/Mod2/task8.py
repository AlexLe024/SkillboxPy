s = input()
count = 0

for char in s:
    if char == s[0]:
        count += 1
    else:
        break
print(count)
