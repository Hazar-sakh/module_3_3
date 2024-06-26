# Задача "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print_params()
print_params(1, 2, 3)
print_params(2, 2)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(c = {'a': 1, 'b': 2})
print()
values_list = ['yankee', False, 3.7]
values_dict = {'a': 52, 'b': 'bulochka', 'c': False}

print_params(*values_list)
print_params(**values_dict)

print()
values_list_2 = ['kurochka', 5.3]
print_params(*values_list_2, 42)
