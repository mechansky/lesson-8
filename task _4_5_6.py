class NotANumber(Exception):
    def __init__(self, text):
        self.text = text


class NegativeLeftovers(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.leftovers = {}

    def __str__(self):
        return f'Склад {self.name} (Адрес: {self.address})'

    def arrival(self, obj, amount):  # занести поступление на склад
        try:
            if str(amount).isdigit():
                arriving = {obj: amount}
                self.leftovers.update(arriving)
            else:
                raise NotANumber('для корректного поступления вы должны вводить числа!')
        except NotANumber as error:
            print(error)
        arriving = {obj: amount}
        self.leftovers.update(arriving)

    def show_leftovers(self):  # показать остатки на складе
        print(f'Остатки по складу "{self.name}":')
        for key, value in self.leftovers.items():
            print(f'{key.name} {key.brand} {key.model}: {value} шт')

    def movement(self, obj, amount, place):  # метод перемещения со склада на склад
        if obj in self.leftovers:
            try:
                if str(amount).isdigit():
                    try:
                        if self.leftovers[obj] - amount > 0:
                            self.leftovers[obj] = self.leftovers[obj] - amount
                            movement = {obj: amount}
                            place.leftovers.update(movement)
                        else:
                            movement = {obj: self.leftovers[obj]}
                            place.leftovers.update(movement)
                            self.leftovers[obj] = 0
                            raise NegativeLeftovers(f'На складе {self.name} больше не осталось товара {obj.name} '
                                                    f'{obj.brand} {obj.model}')
                    except NegativeLeftovers as error:
                        print(error)
                else:
                    raise NotANumber('для корректного перемещения вы должны вводить числа!')
            except NotANumber as error:
                print(error)


class Office(Warehouse):
    def show_leftovers(self):  # показать остатки на складе
        print(f'Остатки в офисе "{self.name}":')
        for key, value in self.leftovers.items():
            print(f'{key.name} {key.brand} {key.model}: {value} шт')


class OfficeEquipment:
    def __init__(self, name, brand, model):
        self.name = name
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'Наименование: {self.name}'


class Xerox(OfficeEquipment):
    def __init__(self, name, brand, model, is_colorful, speed):
        super().__init__(name, brand, model)
        self.is_colorful = is_colorful
        self.speed = speed


class Printer(OfficeEquipment):
    def __init__(self, name, brand, model, technology, form):
        super().__init__(name, brand, model)
        self.technology = technology
        self.format = form


class Scanner(OfficeEquipment):
    def __init__(self, name, brand, model, characteristic, resolution):
        super().__init__(name, brand, model)
        self.characteristic = characteristic
        self.resolution = resolution


product_1 = Xerox('Ксерокс', 'XEROX', 'XHG-420', True, 150)
product_2 = Printer('Принтер', 'HP', 'ZPA-4000', 'Laser', 'A4')
product_3 = Scanner('Сканер', 'SAMSUNG', 'STR-9-50', 'lingering', '1440X760')

main_warehouse = Warehouse("Главный материальный склад", "Пионерская 13")
office_1 = Office('Главный офис', 'Ленина 1')
office_2 = Office('Филиал г. СПб', 'Невский проспект 13')

main_warehouse.arrival(product_1, 10)
main_warehouse.arrival(product_2, 10)
main_warehouse.arrival(product_3, 10)

main_warehouse.movement(product_1, 15, office_1)
main_warehouse.movement(product_2, 8, office_1)
main_warehouse.movement(product_3, 5, office_1)

main_warehouse.movement(product_2, 2, office_2)
main_warehouse.movement(product_3, 'строка', office_2)


office_1.show_leftovers()
office_2.show_leftovers()
main_warehouse.show_leftovers()
