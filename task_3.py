class NotANumber(Exception):
    def __init__(self, text):
        self.text = text


list_of_numbers = []

while True:
    new_element = input('Введите число, для добавления в список (для выхода напишите STOP): ')
    if new_element.lower() == 'stop':
        print(f'полученный список:\n{[int(element) for element in list_of_numbers]}')
        break
    try:
        if new_element.isdigit():
            list_of_numbers.append(new_element)
        else:
            raise NotANumber('Вы ввели не число! Введите число (для выхода напишите STOP): ')
    except NotANumber as error:
        print(error)


