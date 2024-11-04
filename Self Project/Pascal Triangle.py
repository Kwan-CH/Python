"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
copy and paste from Google"""

from math import factorial


def pascal_tri(num_rows):
    # Print Pascal's triangle with numRows.
    for i in range(num_rows):
        # loop to get leading spaces
        for j in range(num_rows - i + 1):
            print(end=" ")

        # loop to get elements of row i
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print('*', end=" ")

        # print each row in a new line
        print("\n")


pascal_tri(6)
