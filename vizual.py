import tkinter as tk
from tkinter.ttk import Combobox, Notebook, Checkbutton, Style

from generpas import generPas

import pyperclip


class VizualPas():
    def __init__(self) -> None:
        # Создаю окно
        window = tk.Tk()
        window.title('GEryCH')
        window.geometry('600x540')
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
            width=5,
            values=[str(x) for x in range(8, 101)]
            )
        combobox_op.set(8)
        self.combobox_op = combobox_op

        generate_one_pass = tk.Button(
            lb_frame_op,
            fg='#000000',
            text='   Новый Пароль   ',
            font='Calibri 15',
            command=self.fun_one_pass
            )

        # чекбоксы выбора из чего генерации
        style = Style()
        style.configure('TCheckbutton', font='Calibri 15')

        check_09_op = tk.BooleanVar()
        checkbutton_09_op = Checkbutton(
            lb_frame_op,
            text="0 .. 9",
            variable=check_09_op,
            style="TCheckbutton"
        )

        check_aw_op = tk.BooleanVar()
        checkbutton_aw_op = Checkbutton(
            lb_frame_op,
            text="a .. w",
            variable=check_aw_op,
            style="TCheckbutton"
        )

        check_AW_op = tk.BooleanVar()
        checkbutton_AW_op = Checkbutton(
            lb_frame_op,
            text="A .. W",
            variable=check_AW_op,
            style="TCheckbutton"
        )

        check_symbol_op = tk.BooleanVar()
        checkbutton_symbol_op = Checkbutton(
            lb_frame_op,
            text="№! .. /%",
            variable=check_symbol_op,
            style="TCheckbutton"
        )

        # Расположение элементов
        lb_frame_op.pack(fill=tk.X)
        lb_pass_op.grid(row=0, column=0, columnspan=4)
        lb_len_symbol_op.grid(row=1, column=0, columnspan=2, sticky='w')
        combobox_op.grid(row=1, column=2, sticky='e')
        generate_one_pass.grid(row=1, column=3)
        checkbutton_09_op.grid(row=2, column=0)
        checkbutton_aw_op.grid(row=2, column=1)
        checkbutton_AW_op.grid(row=2, column=2)
        checkbutton_symbol_op.grid(row=2, column=3)


        # Генерация пароля вида (####-####-####)
        lb_frame_pv = tk.LabelFrame(
            window,
            text='Генерация пароля вида Лицензии',
            font='Calibri 20'
            )

        for c in range(3): lb_frame_pv.columnconfigure(index=c, weight=1)
        for r in range(3): lb_frame_pv.rowconfigure(index=r, weight=1)

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
            width=5,
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
            width=5,
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
            width=5,
            values=[str(x) for x in range(2, 101)]
        )
        combobox_size_of_sections_pv.set(3)
        self.combobox_size_of_sections_pv = combobox_size_of_sections_pv

        generate_lic_pass = tk.Button(
            lb_frame_pv,
            fg='#000000',
            text='   Новый Пароль   ',
            font='Calibri 15',
            command=self.fun_lic_pass
            )

        # Расположение элементов
        lb_frame_pv.pack(fill=tk.X)
        lb_pass_pv.grid(row=0, column=0, columnspan=5)

        lb_separating_symbol_pv.grid(row=1, column=0, columnspan=2, sticky='w')
        combobox_separating_symbol_pv.grid(row=1, column=2, sticky='e')

        lb_number_of_sections_pv.grid(row=2, column=0, columnspan=2, sticky='w')
        combobox_number_of_sections_pv.grid(row=2, column=2, sticky='e')

        lb_size_of_sections_pv.grid(row=3, column=0, columnspan=2, sticky='w')
        combobox_size_of_sections_pv.grid(row=3, column=2, sticky='e')

        generate_lic_pass.grid(row=1, column=4, rowspan=3)

        # Генерация пароля виде файла
        lb_frame_p_file = tk.LabelFrame(
            window,
            text='Генерация пароля виде файла',
            font='Calibri 20'
            )

        # Создание вкладок
        tab_v_file = Notebook(lb_frame_p_file)
        tab_v_file.pack(expand=True, fill=tk.BOTH)

        # создаем пару фреймвов
        frame_op_v_file = tk.Frame(tab_v_file)
        frame_pv_v_file = tk.Frame(tab_v_file)

        # добавляем фреймы в качестве вкладок
        tab_v_file.add(frame_op_v_file, text="Простые пароли")
        tab_v_file.add(frame_pv_v_file, text="Пароли ввиде лицензии")

        # Создание списка файлов в виде простых паролей
        for c in range(3): frame_op_v_file.columnconfigure(index=c, weight=1)
        for r in range(3): frame_op_v_file.rowconfigure(index=r, weight=1)

        # Имя файла куда сохранилась
        self.lb_pass_op_pf = lb_pass_op_pf = tk.Label(
            frame_op_v_file,
            text='<Name File simple password>',
            font='Calibri 18',
            fg='#1E90FF'
        )

        # киличество паролей в файле
        lb_len_pass_op_v_pf = tk.Label(
            frame_op_v_file,
            text='Количество паролей в файле:',
            font='Calibri 18'
        )

        combobox_len_pass_op_v_pf = Combobox(
            frame_op_v_file,
            font='Calibri 18',
            values=[str(x) for x in range(10, 1001)],
            width=5
        )
        combobox_len_pass_op_v_pf.set(10)
        self.combobox_len_pass_op_v_pf = combobox_len_pass_op_v_pf

        # в вод количество синволов в пароле
        lb_len_symbol_op_v_pf = tk.Label(
            frame_op_v_file,
            text='Количество синволов в пароле:',
            font='Calibri 18'
        )
        combobox_len_symbol_op_v_pf = Combobox(
            frame_op_v_file,
            font='Calibri 18',
            values=[str(x) for x in range(8, 101)],
            width=5
        )
        combobox_len_symbol_op_v_pf.set(8)
        self.combobox_len_symbol_op_v_pf = combobox_len_symbol_op_v_pf

        # чекбоксы выбора из чего генерации
        style = Style()
        style.configure('TCheckbutton', font='Calibri 15')

        check_09 = tk.BooleanVar()
        checkbutton_09_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="0 .. 9",
            variable=check_09,
            style="TCheckbutton"
            )


        check_aw = tk.BooleanVar()
        checkbutton_aw_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="a .. w",
            variable=check_aw,
            style="TCheckbutton"
        )

        check_AW = tk.BooleanVar()
        checkbutton_AW_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="A .. W",
            variable=check_AW,
            style="TCheckbutton"
        )

        check_symbol = tk.BooleanVar()
        checkbutton_symbol_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="№! .. /%",
            variable=check_symbol,
            style="TCheckbutton"
        )


        # кнопка сохранения в фаил простого пароля
        generate_file_pass_op_v_pf = tk.Button(
            frame_op_v_file,
            fg='#000000',
            text='Сохранить в фаил',
            font='Calibri 15',
            command=self.fun_file_pass
        )


        # Создание списка файлов в виде лицензии
        for c in range(3): frame_pv_v_file.columnconfigure(index=c, weight=1)
        for r in range(3): frame_pv_v_file.rowconfigure(index=r, weight=1)

        self.lb_pass_pv_pf = lb_pass_pv_pf = tk.Label(
            frame_pv_v_file,
            text='<Name File type of license>',
            font='Calibri 18',
            fg='#1E90FF'
            )

        lb_separating_symbol_pv_v_file = tk.Label(
            frame_pv_v_file,
            text='Выбрать разделяющий символ:',
            font='Calibri 18'
        )
        combobox_separating_symbol_pv_v_file = Combobox(
            frame_pv_v_file,
            font='Calibri 18',
            width=5,
            values=['-', '#', '_', '%', '$']
        )
        combobox_separating_symbol_pv_v_file.set('-')
        self.combobox_separating_symbol_pv_v_file = combobox_separating_symbol_pv_v_file

        lb_number_of_sections_pv_v_file = tk.Label(
            frame_pv_v_file,
            text='Выбрать количество секций:',
            font='Calibri 18'
        )
        combobox_number_of_sections_pv_v_file = Combobox(
            frame_pv_v_file,
            font='Calibri 18',
            width=5,
            values=[str(x) for x in range(2, 101)]
        )
        combobox_number_of_sections_pv_v_file.set(3)
        self.combobox_number_of_sections_pv_v_file = combobox_number_of_sections_pv_v_file

        lb_size_of_sections_pv_v_file = tk.Label(
            frame_pv_v_file,
            text='Выбрать размер секции:',
            font='Calibri 18'
        )
        combobox_size_of_sections_pv_v_file = Combobox(
            frame_pv_v_file,
            font='Calibri 18',
            width=5,
            values=[str(x) for x in range(2, 101)]
        )
        combobox_size_of_sections_pv_v_file.set(3)
        self.combobox_size_of_sections_pv_v_file = combobox_size_of_sections_pv_v_file

        # кнопка сохранения в фаил пароля вида лицензии
        generate_file_pass_pv_pf = tk.Button(
            frame_pv_v_file,
            fg='#000000',
            text='Сохранить в фаил',
            font='Calibri 15',
            command=self.fun_file_pass
            )

        # Расположение элементов
        lb_frame_p_file.pack(fill=tk.X)

        # простые пароли
        lb_pass_op_pf.grid(row=0, column=0, columnspan=4)
        lb_len_pass_op_v_pf.grid(row=1, column=0, sticky='w', columnspan=2)
        combobox_len_pass_op_v_pf.grid(row=1, column=2, sticky='e')
        lb_len_symbol_op_v_pf.grid(row=2, column=0, sticky='w', columnspan=2)
        combobox_len_symbol_op_v_pf.grid(row=2, column=2, sticky='e')
        checkbutton_09_op_v_pf.grid(row=3, column=0)
        checkbutton_aw_op_v_pf.grid(row=3, column=1)
        checkbutton_AW_op_v_pf.grid(row=3, column=2)
        checkbutton_symbol_op_v_pf.grid(row=3, column=3)
        generate_file_pass_op_v_pf.grid(row=1, column=3, rowspan=2)

        # пароли вида лицензии
        lb_pass_pv_pf.grid(row=0, column=0, columnspan=4)
        lb_separating_symbol_pv_v_file.grid(row=1, column=0, columnspan=2, sticky='w')
        combobox_separating_symbol_pv_v_file.grid(row=1, column=2, sticky='e')
        lb_number_of_sections_pv_v_file.grid(row=2, column=0, columnspan=2, sticky='w')
        combobox_number_of_sections_pv_v_file.grid(row=2, column=2, sticky='e')
        lb_size_of_sections_pv_v_file.grid(row=3, column=0, columnspan=2, sticky='w')
        combobox_size_of_sections_pv_v_file.grid(row=3, column=2, sticky='e')
        generate_file_pass_pv_pf.grid(row=1, column=3, rowspan=3)


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

    # функция сохранения пароли в ваил
    def fun_file_pass(self) -> None:
        # Формирования с паролем
        pas = generPas(
            int(self.combobox_len_pass_op_v_pf.get()),
            '-',
            1,
            int(self.combobox_len_symbol_op_v_pf.get())
        )
        pas.createPass()
        pas.SaveToFile()
        self.lb_pass_op_pf['text'] = pas.last_file_name
