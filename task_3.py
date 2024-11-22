# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
# Чтение файла и обработка данных
with open('test_file/task_3.txt', 'r', encoding='utf-8') as f:
    # Считываем все строки и разделяем на покупки по пустым строкам
    content = f.read().strip().split('\n\n')

    # Для каждой покупки считаем сумму (суммируем цены товаров в строках)
    purchase_sums = [sum(map(int, purchase.split())) for purchase in content]

# Сортируем покупки по убыванию и берём три самых дорогие
three_most_expensive_purchases = sum(sorted(purchase_sums, reverse=True)[:3])
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
