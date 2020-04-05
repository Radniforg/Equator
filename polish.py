
polish = input('Пожалуйста, введите желаемую арифметическую операцию в формате: "Знак Число1 Число2"\n')

sequence_processed = polish.split(' ')
if len(polish.split(' ')) != 3:
  print('Ошибка. Убедитесь, что знаки и числа разделены пробелами')
else:
  try:
    if sequence_processed[0] == '+':
      arithmetic = int(sequence_processed[1]) + int(sequence_processed[2])
    elif sequence_processed[0] == '-':
      arithmetic = int(sequence_processed[1]) - int(sequence_processed[2])
    elif sequence_processed[0] == '*':
      arithmetic = int(sequence_processed[1]) * int(sequence_processed[2])
    elif sequence_processed[0] == '/':
      arithmetic = int(sequence_processed[1]) / int(sequence_processed[2])
    else: 
      arithmetic = 'Ошибка: задана не арифметическая операция'
  except ValueError:
    arithmetic = 'Ошибка: задано не число'
  except ZeroDivisionError:
    arithmetic = 0
    print ('Внимание: деление на ноль!')
print(arithmetic)
  
