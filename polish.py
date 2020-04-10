polish = input('Пожалуйста, введите желаемую арифметическую операцию в формате: "Знак Число1 Число2"\n')

sequence_processed = polish.split(' ')
assert len(polish.split(' ')) == 3, 'Ошибка. Убедитесь, что знаки и числа разделены пробелами'
assert sequence_processed[0] in ['+', '-', '*', '/'], 'Ошибка: задана не арифметическая операция'

try:
  if int(sequence_processed[1]) >= 0 and int(sequence_processed[2]) >= 0:
    if sequence_processed[0] == '+':
      arithmetic = int(sequence_processed[1]) + int(sequence_processed[2])
    elif sequence_processed[0] == '-':
      arithmetic = int(sequence_processed[1]) - int(sequence_processed[2])
    elif sequence_processed[0] == '*':
      arithmetic = int(sequence_processed[1]) * int(sequence_processed[2])
    else:
      arithmetic = int(sequence_processed[1]) / int(sequence_processed[2])
  else:
    arithmetic = 'Ошибка ввода: задано отрицательное число'
except ValueError:
  arithmetic = 'Ошибка ввода: задано не число'
except ZeroDivisionError:
  arithmetic = 'Внимание: деление на ноль!'
except Exception:
  arithmetic = 'Непредвиденная ошибка'
print(arithmetic)
