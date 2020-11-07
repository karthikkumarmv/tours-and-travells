"""
Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each element is shifted by one place in a clockwise manner.
For example, given the following matrix

1 2 3
4 5 6
7 8 9

The output should be

4 1 2
7 5 3
8 9 6

Input Format:
The first line of the Input contains a number n representing the number of rows and columns.
After this, there are n rows with each row containing n elements separated by a space

Output Format:
Print the elements of the modified matrix with each row in a new line and all the elements in each row is separated by a space.

Example 1:

Input:
3
1 2 3
4 5 6
7 8 9

Output:
4 1 2
7 5 3
8 9 6

Example 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
5 1 2 3
9 10 6 4
13 11 7 8
14 15 16 12

Explanation: 
In the first example, there is an odd number of rows and columns hence excluding the middle element i.e. 5 all the elements were shifted by one position in a clockwise manner.
In the second example, there are even number of rows and columns hence all the elements were shifted by one position in a clockwise manner
"""


import random


def rotate(matrix, size):
    print_matrix(matrix, size)
    print("\n\nMatrix After Clock-Wise Rotation:")
    index = 0
    if size % 2 == 0:
        flag = 0
    else:
        flag = 1
    while True:
        temp = matrix[index][index]
        for i in range(index+1, size-index):
            matrix[i-1][index] = matrix[i][index]
        for i in range(index+1, size-index):
            matrix[size-index-1][i-1] = matrix[size-index-1][i]
        for i in range(size-index-2, index-1, -1):
            matrix[i+1][size-index-1] = matrix[i][size-index-1]
        for i in range(size-index-2, index, -1):
            matrix[index][i+1] = matrix[index][i]
        matrix[index][index+1] = temp
        index += 1
        if flag == 1 and index*2 == size - 1:
            break
        elif flag == 0 and index*2 > size-1:
            break
    return matrix


def print_matrix(matrix, size):
    print_statement = ""
    for r in range(size):
        for c in range(size):
            print_statement += str(matrix[r][c])
            if c != size-1:
                print_statement += " "
        if r != size - 1:
            print_statement += '\n'
    print(print_statement, end="")


def generate_matrix(n):
    return [[random.randint(1,9) for i in range(n)] for x in range(n)]


n = random.randint(2,9)
print(n)
matrix = generate_matrix(n)
rotated_matrix = rotate(matrix, n)
print_matrix(rotated_matrix, n)
