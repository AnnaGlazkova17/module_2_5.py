def get_matrix(n,m,value): # создаю функцию
    matrix = [] # задаю пустой список, будет основным списком
    for i in range(n): # создание n вложенных списков
        matrix_1 = [] # вспомогательный список
        matrix.append(matrix_1) # вкладываю вспомогательный в основной
        for j in range(m): # цикл для добавления числа value во вложенный список m раз
            matrix_1.append(value) # добавляю элемент в основной список
    return matrix # возврат списка
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)