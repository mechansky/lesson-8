class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


numerator = int(input('введите числитель: '))
denominator = int(input('введите знаменатель: '))

try:
    if denominator == 0:
        raise ZeroDivision('на ноль делить нельзя!')
    else:
        print(f'{numerator} / {denominator} = {numerator / denominator}')
except ZeroDivision as error:
    print(error)

