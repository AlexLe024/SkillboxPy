domain_name = input()

domain_level = ""
dot_count = 0
output = ""

for char in domain_name:
    if char == '.':
        dot_count += 1
        continue

    if dot_count > 0 and domain_level:
        if output:
            output = domain_level + "\n" + output
        else:
            output = domain_level
        dot_count -= 1
        domain_level = ""

    domain_level = domain_level + char

if domain_level:
    if output:
        output = domain_level + "\n" + output
    else:
        output = domain_level

print(output, end="")
