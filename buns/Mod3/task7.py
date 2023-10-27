numbers = input().split()
has_duplicates = len(numbers) != len(set(numbers))
print(has_duplicates)
