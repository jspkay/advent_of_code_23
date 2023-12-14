f = open("input 1")
matrix = f.read().splitlines()
f.close()

def find_number(x, y):
    numbers = {}
    for i in range(-1, 2):
        for j in range(-1, 2):
            if matrix[x+i][y+j].isdigit():
                total_digit = matrix[x+i][y+j]
                digit_start = (x+i, y+j)
                r = 1
                while 0 <= y+j-r < length and matrix[x+i][y+j-r].isdigit():
                    total_digit = matrix[x+i][y+j-r] + total_digit
                    r += 1
                    digit_start = (x+i, y+j-(r-1))
                r = 1
                while 0 <= y+j+r < length and matrix[x+i][y+j+r].isdigit():
                    total_digit += matrix[x+i][y+j+r]
                    r+=1
                n = int(total_digit)
                
                if n not in numbers.values():
                    numbers.update({n: digit_start})
                else:
                    l = numbers[n]
                    if digit_start not in l:
                        l.append(digit_start)
    return numbers

solution = 0
length = len(matrix[0])
for x in range(len(matrix)):
    for y in range(length):
        if matrix[x][y] == '*':
            # It may be a gear, we want to find two numbers:
            numbers = list(find_number(x, y).keys())
            print(numbers)
            if len(numbers) == 2:
                solution += numbers[0] * numbers[1]
            elif len(numbers) >= 3:
                print("***********************************************")
print(solution)

