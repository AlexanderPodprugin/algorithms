def getDecimalValue(self, head): # создаем функцию
    s = ''   # создаем пустую строку для записи ответа 
    while head:    # пока голова не пустая 
        s += str(head.val)  # добавляем к переменной значение головы 
        head = head.next  # переходим на след узел
    return int(s,2) # возвращаем число в десятичном виде 

    """O(n)"""



