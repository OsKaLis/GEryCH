import tkinter as tk
from tkinter.ttk import Combobox

from generpas import generPas

import pyperclip


class VizualPas():
    def __init__(self) -> None:
        # Создаю окно
        window = tk.Tk()
        window.title('GEryCH')
        window.geometry('800x500')
        window.iconbitmap('images/1682135435611.ico')

        # Генерация простого пароля (######## ->)
        lb_frame_op = tk.LabelFrame(
            window,
            text='Генерация простого пароля',
            font='Calibri 20'
            )

        for c in range(3): lb_frame_op.columnconfigure(index=c, weight=1)
        for r in range(3): lb_frame_op.rowconfigure(index=r, weight=1)

        self.lb_pass_op = lb_pass_op = tk.Label(
            lb_frame_op,
            text='########',
            font='Calibri 25',
            fg='#1E90FF'
            )
        lb_pass_op.bind("<Button-1>", self.copy_password_clipboard)

        lb_len_symbol_op = tk.Label(
            lb_frame_op,
            text='Количество синволов в пароле:',
            font='Calibri 18'
        )

        combobox_op = Combobox(
            lb_frame_op,
            font='Calibri 18',
            values=[str(x) for x in range(8, 101)]
            )
        combobox_op.set(8)
        self.combobox_op = combobox_op

        generate_one_pass = tk.Button(
            lb_frame_op,
            fg='#000000',
            text=' Новый Пароль ',
            font='Calibri 15',
            command=self.fun_one_pass
            )

        # Расположение элементов
        lb_frame_op.pack(fill=tk.X)
        lb_pass_op.grid(row=0, column=0, columnspan=3)
        lb_len_symbol_op.grid(row=1, column=0)
        combobox_op.grid(row=1, column=1, padx=10)
        generate_one_pass.grid(row=1, column=2)


        # Генерация пароля вида (####-####-####)
        lb_frame_pv = tk.LabelFrame(
            window,
            text='Генерация пароля вида Лицензии',
            font='Calibri 20'
            )

        for c in range(4): lb_frame_pv.columnconfigure(index=c, weight=1)
        for r in range(4): lb_frame_pv.rowconfigure(index=r, weight=1)

        self.lb_pass_pv = lb_pass_pv = tk.Label(
            lb_frame_pv,
            text='####-####-####',
            font='Calibri 25',
            fg='#1E90FF'
            )
        lb_pass_pv.bind("<Button-1>", self.copy_password_lic_clipboard)

        lb_separating_symbol_pv = tk.Label(
            lb_frame_pv,
            text='Выбрать разделяющий символ:',
            font='Calibri 18'
        )
        combobox_separating_symbol_pv = Combobox(
            lb_frame_pv,
            font='Calibri 18',
            values=['-', '#', '_', '%', '$']
        )
        combobox_separating_symbol_pv.set('-')
        self.combobox_separating_symbol_pv = combobox_separating_symbol_pv

        lb_number_of_sections_pv = tk.Label(
            lb_frame_pv,
            text='Выбрать количество секций:',
            font='Calibri 18'
        )
        combobox_number_of_sections_pv = Combobox(
            lb_frame_pv,
            font='Calibri 18',
            values=[str(x) for x in range(2, 101)]
        )
        combobox_number_of_sections_pv.set(3)
        self.combobox_number_of_sections_pv = combobox_number_of_sections_pv

        lb_size_of_sections_pv = tk.Label(
            lb_frame_pv,
            text='Выбрать размер секции:',
            font='Calibri 18'
        )
        combobox_size_of_sections_pv = Combobox(
            lb_frame_pv,
            font='Calibri 18',
            values=[str(x) for x in range(2, 101)]
        )
        combobox_size_of_sections_pv.set(3)
        self.combobox_size_of_sections_pv = combobox_size_of_sections_pv

        generate_lic_pass = tk.Button(
            lb_frame_pv,
            fg='#000000',
            text=' Новый Пароль ',
            font='Calibri 15',
            command=self.fun_lic_pass
            )

        # Расположение элементов
        lb_frame_pv.pack(fill=tk.X)
        lb_pass_pv.grid(columnspan=4, sticky='n')

        lb_separating_symbol_pv.grid(row=1, column=0, columnspan=2, sticky='w')
        combobox_separating_symbol_pv.grid(row=1, column=3)

        lb_number_of_sections_pv.grid(row=2, column=0, columnspan=2, sticky='w')
        combobox_number_of_sections_pv.grid(row=2, column=3)

        lb_size_of_sections_pv.grid(row=3, column=0, columnspan=2, sticky='w')
        combobox_size_of_sections_pv.grid(row=3, column=3)

        generate_lic_pass.grid(row=1, column=4, rowspan=3)

        # Генерация пароля виде файла
        lb_frame_p_file = tk.LabelFrame(
            window,
            text='Генерация пароля виде файла',
            font='Calibri 20'
            )

        self.lb_pass_pf = lb_pass_pf = tk.Label(
            lb_frame_p_file,
            font='Calibri 18'
            )

        generate_file_pass = tk.Button(
            lb_frame_p_file,
            fg='#000000',
            text=' Сохранить в фаил ',
            font='Calibri 15',
            command=self.fun_file_pass
            )

        lb_frame_p_file.pack(fill=tk.X)
        lb_pass_pf.pack(side=tk.LEFT)
        generate_file_pass.pack(side=tk.RIGHT)

        # Запуск окна
        window.mainloop()

    # функция вывода нового простого пароля
    def fun_one_pass(self):
        # Формирования с паролем
        pas = generPas(1, '-', 1, int(self.combobox_op.get()))
        pas.createPass()
        self.lb_pass_op['text'] = pas.passwords[0]

    # Копирует пароль в буфер обмен
    def copy_password_clipboard(self, event):
        pyperclip.copy(self.lb_pass_op['text'])

    # функция вывода нового пароля вида лицензии
    def fun_lic_pass(self):
        # Формирования с паролем
        pas = generPas(1,
                       self.combobox_separating_symbol_pv.get(),
                       int(self.combobox_number_of_sections_pv.get()),
                       int(self.combobox_size_of_sections_pv.get())
                       )
        pas.createPass()
        self.lb_pass_pv['text'] = pas.passwords[0]

    # Копирует пароль в буфер обмен
    def copy_password_lic_clipboard(self, event):
        pyperclip.copy(self.lb_pass_pv['text'])

    # функция вывода нового пароля вида лицензии
    def fun_file_pass(self):
        # Формирования с паролем
        pas = generPas(10, '-', 3, 4)
        pas.createPass()
        pas.SaveToFile()
