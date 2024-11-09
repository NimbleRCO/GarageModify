import json
import os

class Car:
    def __init__(self, brand, model, headlights, doors, engine, color="", tint=0, year=0, engine_type="", fuel_type="", transmission="", price=0, attack=0):
        self.brand = brand
        self.model = model
        self.color = color
        self.tint = tint
        self.year = year
        self.engine_type = engine_type
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.price = price
        self.headlights = headlights  # Состояние фар (True/False)
        self.doors = doors  # Состояние дверей (True/False)
        self.engine = engine  # Состояние двигателя (True/False)
        self.attack = attack

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        data.setdefault('headlights', False)
        data.setdefault('doors', False)
        data.setdefault('engine', False)
        return cls(**data)


class Garage:
    def __init__(self):
        self.cars = []
        self.brands = []
        self.models = []
        self.colors = []
        self.filename = "GarageMy.json"
        self.brands_filename = "BrandsT.json"
        self.models_filename = "ModelsT.json"
        self.colors_filename = "ColorsT.json"
        self.load_cars()
        self.load_brands()
        self.load_models()
        self.load_colors()

    def load_cars(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.cars = [Car.from_dict(car_data) for car_data in data]

    def save_cars(self):
        with open(self.filename, 'w') as f:
            json.dump([car.to_dict() for car in self.cars], f)

    def load_brands(self):
        if os.path.exists(self.brands_filename):
            with open(self.brands_filename, 'r') as f:
                self.brands = json.load(f)

    def save_brands(self):
        with open(self.brands_filename, 'w') as f:
            json.dump(self.brands, f)

    def load_models(self):
        if os.path.exists(self.models_filename):
            with open(self.models_filename, 'r') as f:
                self.models = json.load(f)

    def save_models(self):
        with open(self.models_filename, 'w') as f:
            json.dump(self.models, f)

    def load_colors(self):
        if os.path.exists(self.colors_filename):
            with open(self.colors_filename, 'r') as f:
                self.colors = json.load(f)

    def save_colors(self):
        with open(self.colors_filename, 'w') as f:
            json.dump(self.colors, f)

    def display_cars(self):
        if not self.cars:
            print("Гараж пуст.")
            return

        for i, car in enumerate(self.cars, 1):
            print(f"{i}. {car.year} | {car.brand} | {car.model} | {car.color}")

        while True:
            choice = input("Введите номер машины для подробной информации (или 0 для возврата): ")
            if choice == '0':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.cars):
                    self.display_car_details(self.cars[index])
                else:
                    print("Неверный номер машины.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def display_car_details(self, car):
        print(f"\nБренд: {car.brand}")
        print(f"Модель: {car.model}")
        print(f"Цвет: {car.color}")
        print(f"Тонировка: {car.tint}%")
        print(f"Год выпуска: {car.year}")
        print(f"Тип двигателя: {car.engine_type}")
        print(f"Тип топлива: {car.fuel_type}")
        print(f"Коробка передач: {car.transmission}")
        print(f"Цена: {car.price}")
        print(f"Состояние:")
        print(f"- Фары: {'Включены' if car.headlights else 'Выключены'}")
        print(f"- Двери: {'Открыты' if car.doors else 'Закрыты'}")
        print(f"- Двигатель: {'Заведён' if car.engine else 'Не заведён'}")
        print(f"- Количество ДТП: {car.attack}")
    def additional_characteristics(self):
        while True:
            print("\n--- Доп. характеристики ---")
            print("1. Бренды")
            print("2. Модели")
            print("3. Цвета")
            print("4. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.brand_management()
            elif choice == '2':
                self.model_management()
            elif choice == '3':
                self.colors_management()
            elif choice == '4':
                return
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 3.")

    def brand_management(self):
        while True:
            print("\n--- Управление брендами ---")
            print("1. Добавить бренд")
            print("2. Удалить бренд")
            print("3. Вывести список брендов")
            print("4. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_brand()
            elif choice == '2':
                self.remove_brand()
            elif choice == '3':
                self.display_brands()
            elif choice == '4':
                return
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")

    def model_management(self):
        while True:
            print("\n--- Управление моделями ---")
            print("1. Добавить модель")
            print("2. Удалить модель")
            print("3. Вывести список моделей")
            print("4. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_model()
            elif choice == '2':
                self.remove_model()
            elif choice == '3':
                self.display_models()
            elif choice == '4':
                return
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")

    def colors_management(self):
        while True:
            print("\n--- Управление цветами ---")
            print("1. Добавить цвет")
            print("2. Удалить цвет")
            print("3. Вывести список цветов")
            print("4. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_color()
            elif choice == '2':
                self.remove_color()
            elif choice == '3':
                self.display_colors()
            elif choice == '4':
                return
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")
    def add_brand(self):
        brand = input("Введите новый бренд: ")
        if brand not in self.brands:
            self.brands.append(brand)
            self.save_brands()
            print("Бренд успешно добавлен.")
        else:
            print("Бренд уже существует.")

    def remove_brand(self):
        if not self.brands:
            print("Список брендов пуст.")
            return

        print("Доступные бренды:")
        for i, brand in enumerate(self.brands, 1):
            print(f"{i}. {brand}")

        while True:
            choice = input("Введите номер бренда для удаления (или 0 для отмены): ")
            if choice == '0':
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.brands):
                    confirm = input(f"Вы точно хотите удалить бренд {self.brands[index]}? (да/нет): ").lower()
                    if confirm == 'да':
                        del self.brands[index]
                        self.save_brands()
                        print("Бренд успешно удален.")
                    return
                else:
                    print("Неверный номер бренда.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def display_brands(self):
        if not self.brands:
            print("Список брендов пуст.")
            return

        print("Доступные бренды:")
        for i, brand in enumerate(self.brands, 1):
            print(f"{i}. {brand}")

    def add_model(self):
        model = input("Введите новую модель: ")
        if model not in self.models:
            self.models.append(model)
            self.save_models()
            print("Модель успешно добавлена.")
        else:
            print("Модель уже существует.")

    def remove_model(self):
        if not self.models:
            print("Список моделей пуст.")
            return

        print("Доступные модели:")
        for i, model in enumerate(self.models, 1):
            print(f"{i}. {model}")

        while True:
            choice = input("Введите номер модели для удаления (или 0 для отмены): ")
            if choice == '0':
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.models):
                    confirm = input(f"Вы точно хотите удалить модель {self.models[index]}? (да/нет): ").lower()
                    if confirm == 'да':
                        del self.models[index]
                        self.save_models()
                        print("Модель успешно удалена.")
                    return
                else:
                    print("Неверный номер модели.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def display_models(self):
        if not self.models:
            print("Список моделей пуст.")
            return

        print("Доступные модели:")
        for i, model in enumerate(self.models, 1):
            print(f"{i}. {model}")

    def add_color(self):
        color = input("Введите новый цвет: ")
        if color not in self.colors:
            self.colors.append(color)
            self.save_colors()
            print("Цвет успешно добавлен.")
        else:
            print("Цвет уже существует.")

    def remove_color(self):
        if not self.colors:
            print("Список цветов пуст.")
            return

        print("Доступные цвета:")
        for i, color in enumerate(self.colors, 1):
            print(f"{i}. {color}")

        while True:
            choice = input("Введите номер цвета для удаления (или 0 для отмены):")
            if choice == '0':
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.colors):
                    confirm = input(f"Вы точно хотите удалить цвет {self.colors[index]}? (да/нет):").lower()
                    if confirm == 'да':
                        del self.colors[index]
                        self.save_colors()
                        print("Цвет успешно удален.")
                    return
                else:
                    print("Неверный номер цвета.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def display_colors(self):
        if not self.colors:
            print("Список цветов пуст.")
            return

        print("Доступные цвета:")
        for i, color in enumerate(self.colors, 1):
            print(f"{i}. {color}")

    def add_car(self):
        fuel_types = {
            "двс": ["92", "95", "98", "дизель"],
            "гибрид": ["92+электро", "95+электро", "98+электро", "дизель+электро"],
            "электро": ["электро"]
        }

        print("\nДобавление новой машины:")
        if not self.brands:
            print("Список брендов пуст. Пожалуйста, добавьте бренд.")
            return

        print("Доступные бренды:")
        for i, brand in enumerate(self.brands, 1):
            print(f"{i}. {brand}")

        while True:
            choice = input("Введите номер бренда (или 0 для добавления нового бренда): ")
            if choice == '0':
                self.add_brand()
                continue
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.brands):
                    brand = self.brands[index]
                    break
                else:
                    print("Неверный номер бренда.")
            except ValueError:
                print("Пожалуйста, введите число.")

        if not self.models:
            print("Список моделей пуст. Пожалуйста, добавьте модель.")
            return

        print("Доступные модели:")
        for i, model in enumerate(self.models, 1):
            print(f"{i}. {model}")

        while True:
            choice = input("Введите номер модели (или 0 для добавления новой модели): ")
            if choice == '0':
                self.add_model()
                continue
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.models):
                    model = self.models[index]
                    break
                else:
                    print("Неверный номер модели.")
            except ValueError:
                print("Пожалуйста, введите число.")

        if not self.colors:
            print("Список цветов пуст. Пожалуйста, добавьте цвет.")
            return

        print("Доступные цвета:")
        for i, color in enumerate(self.colors, 1):
            print(f"{i}. {color}")

        while True:
            choice = input("Введите номер цвета (или 0 для добавления нового цвета): ")
            if choice == '0':
                self.add_color()
                continue
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.colors):
                    color = self.colors[index]
                    break
                else:
                    print("Неверный номер цвета.")
            except ValueError:
                print("Пожалуйста, введите число.")

        if not brand or not model or not color:
            print("Бренд, модель и цвет обязательны для заполнения.")
            return

        while True:
            tint = input("Тонировка (0-100): ")
            try:
                tint = int(tint)
                if 0 <= tint <= 100:
                    break
                else:
                    print("Тонировка должна быть от 0 до 100.")
            except ValueError:
                print("Пожалуйста, введите число.")

        while True:
            year = input("Год выпуска (не менее 1900): ")
            try:
                year = int(year)
                if year >= 1900:
                    break
                else:
                    print("Год выпуска должен быть не менее 1900.")
            except ValueError:
                print("Пожалуйста, введите число.")

        while True:
            engine_type = input("Тип двигателя (электро, гибрид, ДВС): ").lower()
            if engine_type in fuel_types:
                break
            else:
                print("Тип двигателя должен быть 'электро', 'гибрид' или 'ДВС'.")

        print("Доступные типы топлива:")
        for fuel in fuel_types[engine_type]:
            print(f"- {fuel}")

        while True:
            fuel_type = input(f"Введите тип топлива для {engine_type}: ").strip()
            if fuel_type in fuel_types[engine_type]:
                break
            else:
                print("Неверный тип топлива. Попробуйте еще раз.")

        while True:
            transmission = input("Коробка передач (автоматическая, механическая, робот): ").lower()
            if transmission in ["автоматическая", "механическая", "робот"]:
                break
            else:
                print("Коробка передач должна быть 'автоматическая', 'механическая' или 'робот'.")

        price = input("Цена (необязательно): ")
        if price:
            try:
                price = float(price)
            except ValueError:
                print("Неверный формат цены. Цена будет установлена в 0.")
                price = 0
        else:
            price = 0

            # Состояние фар
            while True:
                headlights_choice = input("Фары включены? (да/нет): ").lower()
                if headlights_choice == "да":
                    headlights = True
                    break
                elif headlights_choice == "нет":
                    headlights = False
                    break
                else:
                    print("Неверный ввод. Попробуйте еще раз.")

            # Состояние дверей
            while True:
                doors_choice = input("Двери открыты? (да/нет): ").lower()
                if doors_choice == "да":
                    doors = True
                    break
                elif doors_choice == "нет":
                    doors = False
                    break
                else:
                    print("Неверный ввод. Попробуйте еще раз.")

            # Состояние двигателя
            while True:
                engine_choice = input("Двигатель заведён? (да/нет): ").lower()
                if engine_choice == "да":
                    engine = True
                    break
                elif engine_choice == "нет":
                    engine = False
                    break
                else:
                    print("Неверный ввод. Попробуйте еще раз.")

            #Сколько раз машина была в дтп
            while True:
                attack = input("Введите сколько раз машина попадала в ДТП: ")
                try:
                    if 0 <= int(attack) <= 100:
                        break
                    else:
                        print('Вы что-то напутали')
                except ValuError():
                    print('Вы ввели не числовой тип данных')

        new_car = Car(brand, model, headlights, doors, engine, color, tint, year, engine_type, fuel_type, transmission, price,attack)
        self.cars.append(new_car)
        self.save_cars()
        print("Машина успешно добавлена.")

    def remove_car(self):
        self.display_cars()
        if not self.cars:
            return

        while True:
            choice = input("Введите номер машины для удаления (или 0 для отмены): ")
            if choice == '0':
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.cars):
                    confirm = input(f"Вы точно хотите удалить машину {self.cars[index].brand} {self.cars[index].model}? (да/нет): ").lower()
                    if confirm == 'да':
                        del self.cars[index]
                        self.save_cars()
                        print("Машина успешно удалена.")
                    return
                else:
                    print("Неверный номер машины.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def edit_car(self):
        fuel_types = {
            "двс": ["92", "95", "98", "дизель"],
            "гибрид": ["92+электро", "95+электро", "98+электро", "дизель+электро"],
            "электро": ["электро"]
        }

        self.display_cars()
        if not self.cars:
            return

        while True:
            choice = input("Введите номер машины для редактирования (или 0 для отмены): ")
            if choice == '0':
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.cars):
                    car = self.cars[index]
                    print(f"\nРедактирование {car.brand} {car.model}:")
                    print("Просим вас обратить внимание, что бренд, модель, год выпуска и тип двигателя не изменяемы.")

                    print("Доступные цвета:")
                    for i, color in enumerate(self.colors, 1):
                        print(f"{i}. {color}")

                    while True:
                        choice = input(f"Введите номер цвета ({car.color}): ")
                        if choice == '':
                            break
                        try:
                            index = int(choice) - 1
                            if 0 <= index < len(self.colors):
                                car.color = self.colors[index]
                                break
                            else:
                                print("Неверный номер цвета.")
                        except ValueError:
                            print("Пожалуйста, введите число.")


                    while True:
                        tint = input(f"Тонировка (0-100) ({car.tint}): ")
                        if not tint:
                            break
                        try:
                            tint = int(tint)
                            if 0 <= tint <= 100:
                                car.tint = tint
                                break
                            else:
                                print("Тонировка должна быть от 0 до 100.")
                        except ValueError:
                            print("Пожалуйста, введите число.")

                    while True:
                        fuel_type = input(f"Тип топлива ({car.fuel_type}): ").strip()
                        if not fuel_type or fuel_type in fuel_types[car.engine_type]:
                            if fuel_type:
                                car.fuel_type = fuel_type
                            break
                        else:
                            print("Неверный тип топлива. Попробуйте еще раз.")

                    while True:
                        transmission = input(f"Коробка передач (автоматическая, механическая, робот) ({car.transmission}): ").lower()
                        if not transmission or transmission in ["автоматическая", "механическая", "робот"]:
                            if transmission:
                                car.transmission = transmission
                            break
                        else:
                            print("Коробка передач должна быть 'автоматическая', 'механическая' или 'робот'.")

                    price = input(f"Цена ({car.price}): ")
                    if price:
                        try:
                            car.price = float(price)
                        except ValueError:
                            print("Неверный формат цены. Цена не изменена.")

                    # Редактирование состояния фар
                    while True:
                        headlights_choice = input(
                            f"Фары включены? ({'да' if car.headlights else 'нет'}): ").strip().lower()
                        if not headlights_choice or headlights_choice == "да" or headlights_choice == "нет":
                            if headlights_choice == "да":
                                car.headlights = True
                            elif headlights_choice == "нет":
                                car.headlights = False
                            break
                        else:
                            print("Неверный ввод. Попробуйте еще раз.")

                    # Редактирование состояния дверей
                    while True:
                        doors_choice = input(f"Двери открыты? ({'да' if car.doors else 'нет'}): ").strip().lower()
                        if not doors_choice or doors_choice == "да" or doors_choice == "нет":
                            if doors_choice == "да":
                                car.doors = True
                            elif doors_choice == "нет":
                                car.doors = False
                            break
                        else:
                            print("Неверный ввод. Попробуйте еще раз.")

                    # Редактирование состояния двигателя
                    while True:
                        engine_choice = input(f"Двигатель заведён? ({'да' if car.engine else 'нет'}): ").strip().lower()
                        if not engine_choice or engine_choice == "да" or engine_choice == "нет":
                            if engine_choice == "да":
                                car.engine = True
                            elif engine_choice == "нет":
                                car.engine = False
                            break
                        else:
                            print("Неверный ввод. Попробуйте еще раз.")

                    #Редактирование количества ДТП
                    while True:
                        attack = input("Сколько раз машина была в ДТП (0-100): ")
                        if not attack:
                            break
                        try:
                            attack = int(attack)
                            if 0 <= attack <= 100:
                                car.attack = attack
                                break
                            else:
                                print('Вы не соблюли диапазон')
                        except ValueError:
                            print('Введите нужный формат данных')

                    self.save_cars()
                    print("Машина успешно отредактирована.")
                    return
                else:
                    print("Неверный номер машины.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def search_cars(self):
        print("\nПоиск машин:")
        search_params = {}

        # Доступные бренды
        print("Доступные бренды:")
        brands = sorted(set(car.brand for car in self.cars))
        for i, brand in enumerate(brands, 1):
            print(f"{i}. {brand}")

        while True:
            brand_choice = input("Выберите бренд (или оставьте пустым для пропуска): ")
            if not brand_choice or brand_choice.isdigit() and 1 <= int(brand_choice) <= len(brands):
                if brand_choice and brand_choice.isdigit():
                    search_params['brand'] = brands[int(brand_choice) - 1]
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        # Доступные модели
        print("Доступные модели:")
        models = sorted(
            set(car.model for car in self.cars if 'brand' not in search_params or car.brand == search_params['brand']))
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")

        while True:
            model_choice = input("Выберите модель (или оставьте пустым для пропуска): ")
            if not model_choice or model_choice.isdigit() and 1 <= int(model_choice) <= len(models):
                if model_choice and model_choice.isdigit():
                    search_params['model'] = models[int(model_choice) - 1]
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        # Доступные цвета
        print("Доступные цвета:")
        colors = sorted(set(car.color for car in self.cars if
                            'brand' not in search_params or car.brand == search_params.get('brand', '') if
                            'model' not in search_params or car.model == search_params.get('model', '')))
        for i, color in enumerate(colors, 1):
            print(f"{i}. {color}")

        while True:
            color_choice = input("Выберите цвет (или оставьте пустым для пропуска): ")
            if not color_choice or color_choice.isdigit() and 1 <= int(color_choice) <= len(colors):
                if color_choice and color_choice.isdigit():
                    search_params['color'] = colors[int(color_choice) - 1]
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        # Типы двигателей
        engine_types = {
            "двс": ["92", "95", "98", "дизель"],
            "гибрид": ["92+электро", "95+электро", "98+электро", "дизель+электро"],
            "электро": ["электро"]
        }
        print("Доступные типы двигателей:")
        for i, engine_type in enumerate(engine_types.keys(), 1):
            print(f"{i}. {engine_type}")

        while True:
            engine_type_choice = input("Выберите тип двигателя (или оставьте пустым для пропуска): ")
            if not engine_type_choice or engine_type_choice.isdigit() and 1 <= int(engine_type_choice) <= len(
                    engine_types):
                if engine_type_choice and engine_type_choice.isdigit():
                    search_params['engine_type'] = list(engine_types.keys())[int(engine_type_choice) - 1]
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        # Типы топлива
        fuel_types_list = []
        if 'engine_type' in search_params:
            fuel_types_list = engine_types[search_params['engine_type']]
        else:
            for fuel_types in engine_types.values():
                fuel_types_list.extend(fuel_types)
        fuel_types_list = list(set(fuel_types_list))
        fuel_types_list.sort()
        print("Доступные типы топлива:")
        for i, fuel_type in enumerate(fuel_types_list, 1):
            print(f"{i}. {fuel_type}")

        while True:
            fuel_type_choice = input("Выберите тип топлива (или оставьте пустым для пропуска): ")
            if not fuel_type_choice or fuel_type_choice.isdigit() and 1 <= int(fuel_type_choice) <= len(
                    fuel_types_list):
                if fuel_type_choice and fuel_type_choice.isdigit():
                    search_params['fuel_type'] = fuel_types_list[int(fuel_type_choice) - 1]
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        # Типы коробок передач
        transmission_types = ["автоматическая", "механическая", "робот"]
        print("Доступные типы коробок передач:")
        for i, transmission_type in enumerate(transmission_types, 1):
            print(f"{i}. {transmission_type}")

        while True:
            transmission_type_choice = input("Выберите тип коробки передач (или оставьте пустым для пропуска): ")
            if not transmission_type_choice or transmission_type_choice.isdigit() and 1 <= int(
                    transmission_type_choice) <= len(transmission_types):
                if transmission_type_choice and transmission_type_choice.isdigit():
                    search_params['transmission'] = transmission_types[int(transmission_type_choice) - 1]
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        # Состояние фар
        while True:
            headlights_choice = input("Фары включены? (да/нет): ").strip().lower()
            if not headlights_choice or headlights_choice in ["да", "нет"]:
                if headlights_choice == "да":
                    search_params['headlights'] = True
                elif headlights_choice == "нет":
                    search_params['headlights'] = False
                break
            else:
                print("Неверный ввод. Попробуйте еще раз.")

        # Состояние дверей
        while True:
            doors_choice = input("Двери открыты? (да/нет): ").strip().lower()
            if not doors_choice or doors_choice in ["да", "нет"]:
                if doors_choice == "да":
                    search_params['doors'] = True
                elif doors_choice == "нет":
                    search_params['doors'] = False
                break
            else:
                print("Неверный ввод. Попробуйте еще раз.")

        # Состояние двигателя
        while True:
            engine_choice = input("Двигатель заведён? (да/нет): ").strip().lower()
            if not engine_choice or engine_choice in ["да", "нет"]:
                if engine_choice == "да":
                    search_params['engine'] = True
                elif engine_choice == "нет":
                    search_params['engine'] = False
                break
            else:
                print("Неверный ввод. Попробуйте еще раз.")

        # Количество ДТП
        while True:
            attack_poisk = input('Введите количество дтп 0-100: ')
            if not attack_poisk or attack_poisk.isdigit() or not (0 <= int(attack_poisk) <= 100):
                search_params['attack'] = attack_poisk
                break
            else:
                print('Неверный формат ввода')

        # Поиск машин по параметрам
        results = []
        for car in self.cars:
            match = True
            for param, value in search_params.items():
                if isinstance(value, bool):
                    if getattr(car, param) != value:
                        match = False
                        break
                elif str(getattr(car, param)).lower() != value.lower():
                    match = False
                    break
            if match:
                results.append(car)

        if results:
            print("\nНайденные машины:")
            for i, car in enumerate(results, 1):
                print(
                        f"{i}. {car.year} | {car.brand} | {car.model} | {car.color} | {car.engine_type} | {car.fuel_type} | {car.transmission} | {car.attack}")
        else:
            print('Не нашел подходящих машин')


def main():
    garage = Garage()

    while True:
        print("\n--- Меню ---")
        print("1. Показать список машин")
        print("2. Добавить машину")
        print("3. Удалить машину")
        print("4. Изменить информацию о машине")
        print("5. Поиск машин")
        print("6. Доп. характеристики")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            garage.display_cars()
        elif choice == '2':
            garage.add_car()
        elif choice == '3':
            garage.remove_car()
        elif choice == '4':
            garage.edit_car()
        elif choice == '5':
            garage.search_cars()
        elif choice == '6':
            garage.additional_characteristics()
        elif choice == '7':
            print("Спасибо за использование программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")


if __name__ == "__main__":
    main()
