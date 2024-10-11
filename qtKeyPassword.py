from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QLineEdit, QLabel, QVBoxLayout,
    QHBoxLayout, QComboBox, QWidget, QCheckBox,
    QPushButton, QMessageBox,
)

from generpas import GenerPas

MIN_NUMBER = 2   # Минимальное длина
MAX_NUMBER = 10  # Максимальная длина
SEPARATING_SIMPLE = [
    '#', '-', '@', '%', '$', '<>', ':', '><', '?', '::'
]


class KeyPassword(QMainWindow):
    """Клас для создание интерфейса создания пароля типа Key."""
    def __init__(self):
        super(KeyPassword, self).__init__()
        os_panely = QVBoxLayout()

        self.edit_line_pass = QLineEdit('GENERATE_KEY_PASS')
        font = self.edit_line_pass.font()
        font.setPointSize(22)
        self.edit_line_pass.setFont(font)
        self.edit_line_pass.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # font - общий
        font_all = font
        font_all.setPointSize(15)
        self.setFont(font_all)

        # Выбор разделяющий символ
        separating_simple = QHBoxLayout()
        text = 'Выбирите разделяющий символ:'
        self.lable_separating_simple = QLabel(text)
        self.cb_separating_simple = QComboBox()
        self.cb_separating_simple.addItems(SEPARATING_SIMPLE)
        separating_simple.addWidget(self.lable_separating_simple)
        separating_simple.addWidget(self.cb_separating_simple)

        # Выбор количество секций
        number_section = QHBoxLayout()
        text = 'Выбор количетсво секций:'
        self.lable_number_section = QLabel(text)
        self.cb_number_section = QComboBox()
        self.cb_number_section.addItems(
            [str(number) for number in range(MIN_NUMBER, MAX_NUMBER+1)]
        )
        number_section.addWidget(self.lable_number_section)
        number_section.addWidget(self.cb_number_section)

        # Выбор размер секции
        size_section = QHBoxLayout()
        text = 'Выбор размер секции:'
        self.lable_size_section = QLabel(text)
        self.cb_size_section = QComboBox()
        self.cb_size_section.addItems(
            [str(number) for number in range(MIN_NUMBER, MAX_NUMBER+1)]
        )
        size_section.addWidget(self.lable_size_section)
        size_section.addWidget(self.cb_size_section)

        # Кнопка получить сгенерированый пароль
        self.receive_password = QPushButton('Получить')
        self.receive_password.pressed.connect(self.clik_receive_pass)

        # Чекбоксы выбора деапазона генерации
        generate_panely_1 = QHBoxLayout()
        self.uppercase_letters = QCheckBox('Буквы англ в верхнем регистре')
        self.uppercase_letters.setChecked(True)
        self.number = QCheckBox('Цыфры')
        self.number.setChecked(True)
        generate_panely_1.addWidget(self.uppercase_letters)
        generate_panely_1.addWidget(self.number)

        generate_panely_2 = QHBoxLayout()
        self.lowercase_letters = QCheckBox('Буквы англ в нижнем регистре')
        self.lowercase_letters.setChecked(True)
        self.symbols = QCheckBox('Символы')
        self.symbols.setChecked(False)
        generate_panely_2.addWidget(self.lowercase_letters)
        generate_panely_2.addWidget(self.symbols)

        # Распределение элементов
        os_panely.addWidget(self.edit_line_pass)
        os_panely.addLayout(separating_simple)
        os_panely.addLayout(number_section)
        os_panely.addLayout(size_section)
        os_panely.addLayout(generate_panely_1)
        os_panely.addLayout(generate_panely_2)
        os_panely.addWidget(self.receive_password)

        widget = QWidget()
        widget.setLayout(os_panely)
        self.setCentralWidget(widget)

    def clik_receive_pass(self, kol_pass: int = 1, file: bool = False):
        """Сгенирировать пароль по типу KEY."""

        separating_simple = SEPARATING_SIMPLE[
            self.cb_separating_simple.currentIndex()
        ]
        kolsekciy = MIN_NUMBER + self.cb_number_section.currentIndex()
        dlinasekcii = MIN_NUMBER + self.cb_size_section.currentIndex()
        gp = GenerPas(kol_pass, separating_simple, kolsekciy, dlinasekcii)
        number = self.number.isChecked()
        lowercase_letters = self.lowercase_letters.isChecked()
        uppercase_letters = self.uppercase_letters.isChecked()
        symbols = self.symbols.isChecked()

        # Проверка на чекбоксы что выбран хотябы один
        if (
                not number
                and not lowercase_letters
                and not uppercase_letters
                and not symbols
        ):
            error = QMessageBox(self)
            error.setWindowTitle('Ошибка:')
            error.setText('Нужно выбрато хотябы один из чекбоксов!!!')
            error.exec()
        else:
            gp.list_of_character_types['number_symbols'][0] = number
            gp.list_of_character_types['lowercase_letters'][0] = lowercase_letters
            gp.list_of_character_types['uppercase_letters'][0] = uppercase_letters
            gp.list_of_character_types['symbols'][0] = symbols
            gp.createPass()
            if file:
                return gp.passwords
            self.edit_line_pass.setText(gp.passwords[0])
