for i in range(1, 9):
    for j in range(1, i + 1):
        product = i * j
        print(f'{f"{j} x {i} = {product}":<15}', end=' ')
    print('\n')