import sys

import numpy as np

valid_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                *[str(i) for i in range(10)] ]

"""
Wrong solutions:
54624
54591
"""

sol = 0
with open('input', 'r') as file:
    reader = file.readlines()
    for row in reader:
        start_positions = {i: [] for i in range(20)}
        
        print(row, end=" ")
        for i in range(len(valid_digits)):
            value = row.find(valid_digits[i])
            while value > -1:
                start_positions[i].append(value)
                value = row.find(valid_digits[i], value+1)
            
        bigm = -1
        smalln = 1e50
        print(start_positions)
        for value, position in start_positions.items():
            for p in position:
                if p > bigm:
                    bigm = p
                    right_digit = value % 10
                    print(f"new max {bigm}")
                if p < smalln:
                    smalln = p
                    left_digit = value % 10
                    print(f"new min {smalln}")

        
        number = left_digit*10 + right_digit
        print(left_digit, " - " , right_digit, " -> ", number)
            
        
        sol += number
print(sol)
print(sol)
print(sol)
print(sol)