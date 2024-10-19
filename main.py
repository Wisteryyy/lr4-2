numbers = input("Введите список чисел через пробел: ")
numbers = numbers.split()
numbers = [int(n) for n in numbers]

k = [n**2 for n in numbers]

print("Квадраты чисел из списка:", k)