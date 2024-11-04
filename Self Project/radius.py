import math

height_value = []
for i in range(2, 13, 2):
    r = i
    r_plus_2 = r + 2
    sphere_area = 4 * (r ** 2)
    up_part = 16 * (r ** 4)
    below = r_plus_2 ** 4
    final = ((up_part / below) - (r_plus_2 ** 2)) * -1
    sqrt = math.sqrt(round(final, 2))
    height_value.append(int(sqrt))
print(height_value)