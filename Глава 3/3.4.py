def fill_snake_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    for layer in range((n + 1) // 2):
        # заполняем верхнюю строку
        for i in range(layer, n - layer):
            matrix[layer][i] = num
            num += 1
        # заполняем последний столбец
        for i in range(layer + 1, n - layer):
            matrix[i][n - 1 - layer] = num
            num += 1
        # заполняем последнюю строку
        for i in range(layer + 1, n - layer):
            matrix[n - 1 - layer][n - 1 - i] = num
            num += 1
        # заполняем первый столбец
        for i in range(layer + 1, n - 1 - layer):
            matrix[n - 1 - i][layer] = num
            num += 1
    return matrix


# пример использования функции
n = 5  # размерность матрицы
snake_matrix = fill_snake_matrix(n)

# выводим матрицу на экран
for row in snake_matrix:
    print(row)
