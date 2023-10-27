phone_number = input()
cleaned_number = ''.join(filter(str.isdigit, phone_number))
print('+' + cleaned_number)
