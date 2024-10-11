import time
import os
import sys

from PyQt6.QtCore import QSize
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout,
    QMainWindow, QPushButton, QStackedLayout,
    QVBoxLayout, QWidget, QDialog, QLabel,
    QDialogButtonBox, QSpinBox, QFileDialog,
)

from qtSimplePassword import SimplePassword
from qtKeyPassword import KeyPassword


class MainGeryCH(QMainWindow):
    """Клас для реализации QT интерфейс для GEryCH."""

    def __init__(self):
        super(MainGeryCH, self).__init__()

        # Настройки основного окна
        self.setWindowTitle('GEryCh')
        self.setWindowIcon(QtGui.QIcon('images/1682135435611.ico'))
        self.setFixedSize(QSize(600, 400))

        # Распределёная панель програмы
        tab_panel = QVBoxLayout()
        button_panel = QHBoxLayout()
        self.distribution = QStackedLayout()

        tab_panel.addLayout(button_panel)
        tab_panel.addLayout(self.distribution)

        # Кнопка генерации простого пароля
        button_pass = self.create_button_panel(
            'Простой пароль',
            'images/5582931.png',
            self.activate_pass,
        )
        button_panel.addWidget(button_pass)
        self.simple_password = SimplePassword()
        self.distribution.addWidget(self.simple_password)

        # Кнопка генерации пароля вида KEY
        button_key = self.create_button_panel(
            'Пароль вида лицензии',
            'images/5395518.png',
            self.activate_key,
        )
        button_panel.addWidget(button_key)
        self.key_password = KeyPassword()
        self.distribution.addWidget(self.key_password)

        # Меню програмы
        self.create_menu()

        # Собираем
        widget = QWidget()
        widget.setLayout(tab_panel)
        self.setCentralWidget(widget)

    def create_button_panel(self, title: str, images: str, fun: object):
        """Кнопка создания на панели."""

        button = QPushButton(title)
        button.setIconSize(QSize(32, 32))
        button.setIcon(QtGui.QIcon(images))
        button.pressed.connect(fun)
        return button

    def create_menu(self):
        """Создание основного меню програмы."""

        menu = self.menuBar()
        # Меню Файла
        file_menu = menu.addMenu('&Файл')

        # Кнопка сохраняет в фаил заданное количество простых паролей
        button_action_pass = QtGui.QAction(
            QtGui.QIcon('images/5582931.png'),
            'Простые пароли сохранить в фаил', self
        )
        button_action_pass.triggered.connect(self.action_menu_pass)
        file_menu.addAction(button_action_pass)

        # Кнопка сохраняет в фаил заданое количество паролей типа Key
        button_action_key = QtGui.QAction(
            QtGui.QIcon('images/5395518.png'),
            'Кей пароли сохранить в файл', self
        )
        button_action_key.triggered.connect(self.actions_menu_key)
        file_menu.addAction(button_action_key)

        # Выход
        button_exit = QtGui.QAction(
            QtGui.QIcon('images/power-button.png'),
            'Выход', self
        )
        button_exit.triggered.connect(self.action_button_exit)
        file_menu.addAction(button_exit)

    def save_to_file(self, list_password: list):
        """Сохраняет фаил в выбраной директории."""

        self.qdiolog_save = QFileDialog.getSaveFileName(
            self, 'Где сохранить фаил?', None, '*.txt',
        )
        if self.qdiolog_save[0] == '':
            Namefile = time.strftime("%Y_%m_%d_%H.%M.%S", time.localtime())
            file_way = os.path.abspath(os.curdir) + '/' + Namefile + '.txt'
            file = open(file_way, 'w')
        else:
            file = open(self.qdiolog_save[0], 'w')
        for password in list_password:
            file.write(password + '\n')
        file.close()

    def create_dialog_input_value(self, message: str):
        """Диалоговое окно для ввода количество паролей."""

        input_value = QDialog(self)
        input_value.setWindowTitle('Сохранения в фаил:')

        self.plan = QVBoxLayout()
        self.water_quantity = QHBoxLayout()

        qbutton = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(qbutton)
        self.buttonBox.accepted.connect(input_value.accept)
        self.buttonBox.rejected.connect(input_value.reject)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 1000)

        self.water_quantity.addWidget(QLabel(message))
        self.water_quantity.addWidget(self.spin_box)
        self.plan.addLayout(self.water_quantity)
        self.plan.addWidget(self.buttonBox)

        input_value.setLayout(self.plan)
        return input_value

    def action_menu_pass(self):
        """Открывает вод количества простого пароля."""

        qdialog_input = self.create_dialog_input_value('В количество сгенерируемых простых паролей:')
        if qdialog_input.exec():
            list_password = self.simple_password.get_password(
                self.spin_box.value(), True,
            )
            self.save_to_file(list_password)

    def actions_menu_key(self):
        """Открывает вод количества паролей типа Key."""

        qdialog_input = self.create_dialog_input_value('В количество сгенерируемых паролей типа Key:')
        if qdialog_input.exec():
            print(self.spin_box.value())

    def action_button_exit(self):
        """Кнопка выхода из програмы."""
        self.close()

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
