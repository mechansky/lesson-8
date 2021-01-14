class Data:
    def __init__(self, user_data):
        self.user_data = user_data
        print(f'Дата: {self.user_data}')

    @classmethod
    def get_number(cls, user_data):
        result = [int(element) for element in user_data.split('-')]
        return result

    @staticmethod
    def validation(data):
        if data[0] > 31:
            return 'Неправильно указано число!'
        elif data[1] > 12:
            return 'существует только 12 месяцев!'
        elif data[1] == 4 or data[1] == 6 or data[1] == 9 or data[1] == 11:
            if data[0] > 30:
                return 'в апреле, июне, сентябре, ноябре 30 дней!'
            else:
                return 'Дата введена корректно'
        elif data[1] == 2:
            if data[2] % 4 == 0:
                if data[0] > 29:
                    return 'в феврале високосного года 29 дней!'
                else:
                    return 'Дата введена корректно'
            elif data[0] > 28:
                return 'в феврале невисокосного года 28 дней!'
            else:
                return 'дата корректна'





data_1 = Data('29-02-2021')
print(Data.get_number('29-02-2021'))
print(Data.validation(Data.get_number('31-04-2021')))
