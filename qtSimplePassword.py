from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel,
    QCheckBox, QPushButton, QComboBox,
)

from generpas import GenerPas

MIN_PASS = 5   # Минимальная длина пароля
MAX_PASS = 31  # Максимальная длина пароля


class SimplePassword(QMainWindow):
    """Класс для генерации простого пароля."""

    def __init__(self):
        super(SimplePassword, self).__init__()
        tp = QVBoxLayout()

        self.label_pass = QLabel('PASS')

        self.numbers = QCheckBox('Цыфры')
        self.numbers.setChecked(True)

        self.number_characters = QLabel('Длина будующего пароля')

        self.choosing_password_length = QComboBox()
        self.choosing_password_length.addItems(
            [str(x) for x in range(MIN_PASS, MAX_PASS)]
        )

        self.lowercase_letters = QCheckBox('Буквы англ в нижнем регистре')
        self.lowercase_letters.setChecked(True)

        self.uppercase_letters = QCheckBox('Буквы англ в верхнем регистре')
        self.uppercase_letters.setChecked(True)

        self.symbols = QCheckBox('Символы')
        self.symbols.setChecked(False)

        self.get_pass = QPushButton('Получить')
        self.get_pass.pressed.connect(self.clik_get_pass)

        tp.addWidget(self.label_pass)
        tp.addWidget(self.number_characters)
        tp.addWidget(self.choosing_password_length)
        tp.addWidget(self.numbers)
        tp.addWidget(self.lowercase_letters)
        tp.addWidget(self.uppercase_letters)
        tp.addWidget(self.symbols)
        tp.addWidget(self.get_pass)

        widget = QWidget()
        widget.setLayout(tp)
        self.setCentralWidget(widget)

    def clik_get_pass(self):
        """Клик кнопки [get_pass] для генерации простого пароля."""

        numbers = self.numbers.isChecked()
        lowercase_letters = self.lowercase_letters.isChecked()
        uppercase_letters = self.uppercase_letters.isChecked()
        symbols = self.symbols.isChecked()
        length_pass = MIN_PASS + self.choosing_password_length.currentIndex()
        sp = GenerPas(1, '', 1, length_pass)
        sp.list_of_character_types['number_symbols'][0] = numbers
        sp.list_of_character_types['lowercase_letters'][0] = lowercase_letters
        sp.list_of_character_types['uppercase_letters'][0] = uppercase_letters
        sp.list_of_character_types['symbols'][0] = symbols
        sp.createPass()
        self.label_pass.setText(sp.passwords[0])
