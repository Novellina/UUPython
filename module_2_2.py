first = int (input('Введите любое целое число 1: '))
second =int (input('Введите любое целое число 2: '))
third = int (input('Введите любое целое число 3: '))
if first==second==third:
    print (3)
elif first==second or second==third or third==first:
    print (2)
elif first!= second and second!= third and third!= first:
    print (0)