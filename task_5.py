print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

total_number = int(input("Введите количество цифр: "))
summ = 0
amount = 0
this_number = 0
this_number_two = 0

for num in range(1, total_number + 1):
  number = int(input("Введите " + str(num) + " число: "))
  this_number = number
  while number > 0:
    summ += number % 10
    number //= 10
  if summ > amount:
    amount = summ
    max_number = this_number
    summ = 0
  else:
    summ = 0
print("Наибольшее по сумме цифр число:", max_number, "\nСумма его цифр:",
      amount)
