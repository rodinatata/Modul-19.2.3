import pytest
from calculator import Calculator


class TestCalc: # создаем класс (название обязательно с Test)
    def setup(self): # подготовительный метод
        self.calc = Calculator # сдаем объект Калькулятора из импортируемого класса

    # тесты
    def test_multiply_calculate_passed(self): # позитивный тест на правильность умножения
        assert self.calc.multiply(self, 2, 2) == 4 # сравнение ОР с ФР

    def test_division_calculate_passed(self): # позитивный тест на правильность деления
        assert self.calc.division(self, 2, 2) == 1 # сравнение ОР с ФР

    def test_subtraction_calculate_passed(self): # позитивный тест на правильность вычитания
        assert self.calc.subtraction(self, 2, 2) == 0 # сравнение ОР с ФР

    def test_adding_calculate_passed(self): # позитивный тест на правильность сложения
        assert self.calc.adding(self, 2, 2) == 4 # сравнение ОР с ФР
