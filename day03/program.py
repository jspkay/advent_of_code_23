f = open("input 1")
matrix = f.read().strip().split("\n")
f.close()

solution = 0

values_list = []

last_numbers = {}
length = len(matrix[0])
for x in range(len(matrix)):
    for y in range(len(matrix[0])):

        if not matrix[x][y].isdigit() and matrix[x][y] != '.':

            print(f"checking position {(x, y)} with symbol {matrix[x][y]}") 
            
            # We find adjacent numbers
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try: 
                        if matrix[x+i][y+j].isdigit():
                            total_digit = matrix[x+i][y+j]
                            r = 1
                            while 0<= y+j-r < length and matrix[x+i][y+j-r].isdigit():
                                total_digit = matrix[x+i][y+j-r] + total_digit
                                r += 1
                            digit_start = (x+i, y+j-(r-1))
                            r = 1
                            while 0 <= y+j+r < length and matrix[x+i][y+j+r].isdigit():
                                total_digit += matrix[x+i][y+j+r]
                                r+=1
                            print(total_digit, end=" - ")
                            n = int(total_digit)
                            
                            if n not in last_numbers.keys():
                                solution += n
                                print(f" added {n}", end ="\n")
                                values_list.append(n)
                                last_numbers.update({n: [digit_start]})
                            else:
                                positions = last_numbers[n]
                                if digit_start not in positions:
                                    positions.append(digit_start)
                                    print(f"added {n} with new position")
                                    solution += n
                                    values_list.append(n)
                                else:
                                    print(f"Can't add {n} eheh")
                    except Exception as e:
                        print("skipping positions ", (x+i, y+j))
                        print(e)
                        continue
print(values_list)
print(solution)
            
