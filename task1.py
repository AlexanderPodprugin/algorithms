def steps(num): #вводим функцию 
    step = 0 # ввел начальное значение счетчика 
    while num > 0: #условие для цикла 
        if num % 2 == 0: #проверяем число на четность 
            num /= 2 #если число четное делим на два 
        else: #иначе 
            num -= 1 # если число не четное, отнимаю один 
        step +=1 # пока идет цикл добавляем шаг
    return step # возвращаем значение 
    

x = int(input(" num = "))
print(steps(x))
""" Сложность - O(n) """