"""Вывести лесенкой символ звёздочки по кол-ву строк, заданных пользователем:
запросить ввод у пользователя кол-ва строк, вывести звёздочки лесенкой."""

quantity = int(input("Enter stairs quantity: "))

count = 1
while count<=quantity:
    print("*"*count)
    count+=1
