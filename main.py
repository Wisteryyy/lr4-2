numbers = input("Введите список чисел через пробел: ") # вводим список чисел через пробел
numbers = numbers.split() #  split(): разбивает строку на части по умолчанию по пробелам 
numbers = [int(n) for n in numbers] # генераторное выражение, чтоббы преобразовать каждую введеную строку в целое числло с помощью int(n)
k = [n**2 for n in numbers] # такое же генераторное выражение но мы умнажаем уже целые числа на 2 и присваиваем переменной k
print("Квадраты чисел из списка:", k) # выводим эту переменную
