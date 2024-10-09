from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel,
    QCheckBox, QPushButton, QComboBox, QHBoxLayout,
    QLineEdit, QMessageBox,
)

from generpas import GenerPas

MIN_PASS = 5   # Минимальная длина пароля
MAX_PASS = 31  # Максимальная длина пароля


class SimplePassword(QMainWindow):
    """Класс для генерации простого пароля."""

    def __init__(self):
        super(SimplePassword, self).__init__()
        tp = QVBoxLayout()

        self.edit_line_pass = QLineEdit('GENERATE_PASS')
        font = self.edit_line_pass.font()
        font.setPointSize(22)
        self.edit_line_pass.setFont(font)
        self.edit_line_pass.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # font - общий
        font_all = font
        font_all.setPointSize(15)
        self.setFont(font_all)

        # Отвечает за интерфейс Учёта размера пароля
        choice_size_pass = QHBoxLayout()
        self.number_characters = QLabel('Длина будующего пароля:')
        self.choosing_password_length = QComboBox()
        self.choosing_password_length.addItems(
            [str(x) for x in range(MIN_PASS, MAX_PASS)]
        )
        choice_size_pass.addWidget(self.number_characters)
        choice_size_pass.addWidget(self.choosing_password_length)

        # Панель из чего генерить пароль
        generation_range_1 = QHBoxLayout()
        self.uppercase_letters = QCheckBox('Буквы англ в верхнем регистре')
        self.uppercase_letters.setChecked(True)
        self.numbers = QCheckBox('Цыфры')
        self.numbers.setChecked(True)
        generation_range_1.addWidget(self.uppercase_letters)
        generation_range_1.addWidget(self.numbers)

        generation_range_2 = QHBoxLayout()
        self.lowercase_letters = QCheckBox('Буквы англ в нижнем регистре')
        self.lowercase_letters.setChecked(True)
        self.symbols = QCheckBox('Символы')
        self.symbols.setChecked(False)
        generation_range_2.addWidget(self.lowercase_letters)
        generation_range_2.addWidget(self.symbols)

        self.get_pass = QPushButton('Получить')
        self.get_pass.pressed.connect(self.clik_get_pass)

        # Распределяем элементы по секциям
        tp.addWidget(self.edit_line_pass)
        tp.addLayout(choice_size_pass)
        tp.addLayout(generation_range_1)
        tp.addLayout(generation_range_2)
        tp.addWidget(self.get_pass)
        widget = QWidget()
        widget.setLayout(tp)
        self.setCentralWidget(widget)

    def clik_get_pass(self):
        """Клик кнопки [get_pass] для генерации простого пароля."""

        number = self.numbers.isChecked()
        lowercase_letters = self.lowercase_letters.isChecked()
        uppercase_letters = self.uppercase_letters.isChecked()
        symbols = self.symbols.isChecked()
        if (
            not number
            and not lowercase_letters
            and not uppercase_letters
            and not symbols
        ):
            error = QMessageBox(self)
            error.setWindowTitle('Ошибка:')
            error.setText('Нужно выбрато хотябы один из чекбоксов!!!')
            button_error = error.exec()
            if button_error == QMessageBox.StandardButton.Ok:
                pass
        else:
            length_pass = MIN_PASS + self.choosing_password_length.currentIndex()
            sp = GenerPas(1, '', 1, length_pass)
            sp.list_of_character_types['number_symbols'][0] = number
            sp.list_of_character_types['lowercase_letters'][0] = lowercase_letters
            sp.list_of_character_types['uppercase_letters'][0] = uppercase_letters
            sp.list_of_character_types['symbols'][0] = symbols
            sp.createPass()
            self.edit_line_pass.setText(sp.passwords[0])
