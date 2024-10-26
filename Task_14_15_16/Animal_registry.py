from datetime import date
from typing import List


# Базовый класс Animals
class Animals:
    def __init__(self, name: str, birth_date: date):
        self._name = name
        self._birth_date = birth_date

    def speak(self) -> str:
        return "Some sound"

    def get_info(self) -> str:
        return f"Name: {self._name}, Birth Date: {self._birth_date}"

    def get_type(self) -> str:
        return "Animal"


# Класс Pets, наследующий от Animals
class Pets(Animals):
    def __init__(self, name: str, birth_date: date):
        super().__init__(name, birth_date)
        self._commands = []

    def add_command(self, command: str):
        self._commands.append(command)

    def get_commands(self) -> List[str]:
        return self._commands

    def get_type(self) -> str:
        return "Pet"


# Класс PackAnimals, наследующий от Animals
class PackAnimals(Animals):
    def __init__(self, name: str, birth_date: date, load_capacity: float):
        super().__init__(name, birth_date)
        self._load_capacity = load_capacity

    def carry_load(self, weight: float) -> bool:
        return weight <= self._load_capacity

    def get_type(self) -> str:
        return "Pack Animal"


# Подклассы Pets
class Dogs(Pets):
    def __init__(self, name: str, birth_date: date, breed: str):
        super().__init__(name, birth_date)
        self._breed = breed

    def fetch(self) -> str:
        return f"{self._name} is fetching!"

    def get_type(self) -> str:
        return "Dog"


class Cats(Pets):
    def __init__(self, name: str, birth_date: date, color: str):
        super().__init__(name, birth_date)
        self._color = color

    def meow(self) -> str:
        return f"{self._name} says Meow!"

    def get_type(self) -> str:
        return "Cat"


class Hamsters(Pets):
    def __init__(self, name: str, birth_date: date, type_: str):
        super().__init__(name, birth_date)
        self._type = type_

    def run_in_wheel(self) -> str:
        return f"{self._name} is running in the wheel!"

    def get_type(self) -> str:
        return "Hamster"


# Подклассы PackAnimals
class Horses(PackAnimals):
    def __init__(self, name: str, birth_date: date, load_capacity: float, speed: float):
        super().__init__(name, birth_date, load_capacity)
        self._speed = speed

    def gallop(self) -> str:
        return f"{self._name} is galloping!"

    def get_type(self) -> str:
        return "Horse"


class Camels(PackAnimals):
    def __init__(self, name: str, birth_date: date, load_capacity: float):
        super().__init__(name, birth_date, load_capacity)

    def get_type(self) -> str:
        return "Camel"


class Donkeys(PackAnimals):
    def __init__(self, name: str, birth_date: date, load_capacity: float):
        super().__init__(name, birth_date, load_capacity)

    def get_type(self) -> str:
        return "Donkey"


# Класс Счетчик
class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1


# Функция для работы с реестром животных
def main():
    animals_registry = []
    counter = Counter()  # Инициализируем счетчик один раз

    while True:
        print("\nMenu:")
        print("1. Завести новое домашнее животное")
        print("2. Завести новое вьючное животное")
        print("3. Посмотреть список команд питомца")
        print("4. Обучить питомца новым командам")
        print("5. Вывести список всех животных")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            name = input("Введите имя домашнего животного: ")
            birth_date_str = input("Введите дату рождения (YYYY-MM-DD): ")
            birth_date = date.fromisoformat(birth_date_str)
            animal_type = input("Введите тип домашнего животного (Dog/Cat/Hamster): ")

            if animal_type.lower() == 'dog':
                breed = input("Введите породу собаки: ")
                animal = Dogs(name, birth_date, breed)
            elif animal_type.lower() == 'cat':
                color = input("Введите цвет кошки: ")
                animal = Cats(name, birth_date, color)
            elif animal_type.lower() == 'hamster':
                type_ = input("Введите тип хомяка: ")
                animal = Hamsters(name, birth_date, type_)
            else:
                print("Неправильный тип домашнего животного!")
                continue

            counter.add()
            animals_registry.append(animal)
            print(
                f"Завели новое домашнее животное: {animal.get_info()} (Тип: {animal.get_type()}), Общее количество животных: {counter.count}")

        elif choice == '2':
            name = input("Введите имя вьючного животного: ")
            birth_date_str = input("Введите дату рождения (YYYY-MM-DD): ")
            birth_date = date.fromisoformat(birth_date_str)
            load_capacity = float(input("Введите грузоподъемность вьючного животного: "))
            animal_type = input("Введите тип вьючного животного (Horse/Camel/Donkey): ")

            if animal_type.lower() == 'horse':
                speed = float(input("Введите скорость лошади: "))
                animal = Horses(name, birth_date, load_capacity, speed)
            elif animal_type.lower() == 'camel':
                animal = Camels(name, birth_date, load_capacity)
            elif animal_type.lower() == 'donkey':
                animal = Donkeys(name, birth_date, load_capacity)
            else:
                print("Неправильный тип вьючного животного!")
                continue

            counter.add()
            animals_registry.append(animal)
            print(
                f"Завели новое вьючное животное: {animal.get_info()} (Тип: {animal.get_type()}), Общее количество животных: {counter.count}")

        elif choice == '3':
            for animal in animals_registry:
                if isinstance(animal, Pets):
                    print(f"{animal.get_info()}, Команды: {animal.get_commands()}")

        elif choice == '4':
            name = input("Введите имя питомца для обучения: ")
            for animal in animals_registry:
                if isinstance(animal, Pets) and animal._name == name:
                    command = input("Введите команду для добавления: ")
                    animal.add_command(command)
                    print(f"Команда '{command}' добавлена для {animal._name}.")
                    break
            else:
                print("Питомец не найден.")

        elif choice == '5':
            if not animals_registry:
                print("Список животных пуст.")
            else:
                print("\nСписок всех животных:")
                for animal in animals_registry:
                    print(f"{animal.get_info()}, Тип: {animal.get_type()}")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
