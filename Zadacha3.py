# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
number = int (input("Шестизначное число N: "))
cif1 = int (number/1000)
cif2 = int (number%1000)
firstcyf = int(cif1/100)
secondcyf = int(cif1/10) - firstcyf*10
thirdcyf = cif1%10
sum1 = firstcyf + secondcyf + thirdcyf

firstcyf1 = int(cif2/100)
secondcyf1 = int(cif2/10) - firstcyf1*10
thirdcyf1 = cif2%10
sum2 = firstcyf1 + secondcyf1 + thirdcyf1

if (sum1==sum2):
    print ("You're lucky!!!")
else:
    print ("Сорян")

