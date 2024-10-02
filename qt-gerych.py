import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout,
    QMainWindow, QPushButton, QStackedLayout,
    QVBoxLayout, QWidget, QLabel,
)

from qtSimplePassword import SimplePassword


class MainGeryCH(QMainWindow):
    """Клас для реализации QT интерфейс для GEryCH."""

    def __init__(self):
        super(MainGeryCH, self).__init__()

        self.setWindowTitle('GEryCh')
        self.setFixedSize(QSize(600, 400))

        tab_panel = QVBoxLayout()
        button_panel = QHBoxLayout()
        self.distribution = QStackedLayout()

        tab_panel.addLayout(button_panel)
        tab_panel.addLayout(self.distribution)

        # Кнопка генерации простого пароля
        button_pass = QPushButton('Простой пароль')
        button_pass.pressed.connect(self.activate_pass)
        button_panel.addWidget(button_pass)
        self.SimplePassword = SimplePassword()
        self.distribution.addWidget(self.SimplePassword)

        # Кнопка генерации пароля вида KEY
        button_key = QPushButton('Пароль вида лицензии')
        button_key.pressed.connect(self.activate_key)
        self.label_key = QLabel('KEY')
        button_panel.addWidget(button_key)
        self.distribution.addWidget(self.label_key)

        # Собираем
        widget = QWidget()
        widget.setLayout(tab_panel)
        self.setCentralWidget(widget)

    def activate_pass(self):
        """Переключение на вклатку генерации простого пароля."""
        self.distribution.setCurrentIndex(0)

    def activate_key(self):
        """Переключение на вклатку генерации вида KEY пароля."""
        self.distribution.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainGeryCH()
    window.show()
    app.exec()


