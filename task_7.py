print('Задача 7. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

number_levels = int(input("Введите количество уровней пирамиды: "))
number = 1

for row in range(1, number_levels + 1):
  print("\t" * (number_levels - row), end="")
  for col in range(row):
    print(number, end="")
    number += 2
    print("\t" * 2, end="")
  print()
