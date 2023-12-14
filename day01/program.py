sol = 0
with open('input', 'r') as file:
    reader = file.readlines()
    for row in reader:
        digits = filter(lambda x: x.isdigit(), row) f(row[0])
        newlist = list(digits)
        str_digit = newlist[0] + newlist[-1]
        int_digit = int(str_digit)
        sol += int_digit
print(sol)