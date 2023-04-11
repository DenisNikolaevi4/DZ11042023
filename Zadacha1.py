# Задача 2: Найдите сумму цифр трехзначного числа

number = int(input("Введите трехзначное число N: "))
if  (100<=number<1000): 
    firstcyf = int(number/100)
    secondcyf = int(number/10) - firstcyf*10
    thirdcyf = number%10
    sum = firstcyf + secondcyf + thirdcyf
    print (f"Сумма цифр числа N = {sum}")
else:
    print("Введите ТРЕХЗНАЧНОЕ число!!!")
