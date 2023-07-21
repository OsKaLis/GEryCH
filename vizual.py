import tkinter as tk
from tkinter.ttk import Combobox, Notebook, Checkbutton, Style
from tkinter.messagebox import showwarning
import pyperclip

from generpas import GenerPas


class VizualPas():
    def __init__(self) -> None:
        # Создаю окно
        window = tk.Tk()
        window.title('GEryCH')
        window.geometry('610x580')
        window.iconbitmap('images/1682135435611.ico')

        # Генерация простого пароля (######## ->)
        lb_frame_op = tk.LabelFrame(
            window,
            text='Генерация простого пароля',
            font='Calibri 20'
            )

        self.create_cell(lb_frame_op)

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

        # чекбоксы выбора из чего генерации
        style = Style()
        style.configure('TCheckbutton', font='Calibri 15')

        check_09_op = tk.BooleanVar()
        self.checkbutton_09_op = checkbutton_09_op = Checkbutton(
            lb_frame_op,
            text="0 .. 9",
            variable=check_09_op,
            style="TCheckbutton"
        )
        check_09_op.set(True)
        self.check_09_op = check_09_op

        check_aw_op = tk.BooleanVar()
        checkbutton_aw_op = Checkbutton(
            lb_frame_op,
            text="a .. w",
            variable=check_aw_op,
            style="TCheckbutton"
        )
        check_aw_op.set(True)
        self.check_aw_op = check_aw_op

        check_AW_op = tk.BooleanVar()
        checkbutton_AW_op = Checkbutton(
            lb_frame_op,
            text="A .. W",
            variable=check_AW_op,
            style="TCheckbutton"
        )
        check_AW_op.set(True)
        self.check_AW_op = check_AW_op

        check_symbol_op = tk.BooleanVar()
        checkbutton_symbol_op = Checkbutton(
            lb_frame_op,
            text="№! .. /%",
            variable=check_symbol_op,
            style="TCheckbutton"
        )
        self.check_symbol_op = check_symbol_op

        generate_one_pass = tk.Button(
            lb_frame_op,
            fg='#000000',
            text='   Новый Пароль   ',
            font='Calibri 15',
            command=self.fun_one_pass
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

        self.create_cell(lb_frame_pv)

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

        lb_number_of_sections_pv.grid(row=2, column=0, columnspan=2,
                                      sticky='w')
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
        self.create_cell(frame_op_v_file)

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

        check_09_op_v_pf = tk.BooleanVar()
        checkbutton_09_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="0 .. 9",
            variable=check_09_op_v_pf,
            style="TCheckbutton"
            )
        check_09_op_v_pf.set(True)
        self.check_09_op_v_pf = check_09_op_v_pf

        check_aw_op_v_pf = tk.BooleanVar()
        checkbutton_aw_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="a .. w",
            variable=check_aw_op_v_pf,
            style="TCheckbutton"
        )
        check_aw_op_v_pf.set(True)
        self.check_aw_op_v_pf = check_aw_op_v_pf

        check_AW_op_v_pf = tk.BooleanVar()
        checkbutton_AW_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="A .. W",
            variable=check_AW_op_v_pf,
            style="TCheckbutton"
        )
        check_AW_op_v_pf.set(True)
        self.check_AW_op_v_pf = check_AW_op_v_pf

        check_symbol_op_v_pf = tk.BooleanVar()
        checkbutton_symbol_op_v_pf = Checkbutton(
            frame_op_v_file,
            text="№! .. /%",
            variable=check_symbol_op_v_pf,
            style="TCheckbutton"
        )
        check_symbol_op_v_pf.set(False)
        self.check_symbol_op_v_pf = check_symbol_op_v_pf

        # кнопка сохранения в фаил простого пароля
        generate_file_pass_op_v_pf = tk.Button(
            frame_op_v_file,
            fg='#000000',
            text='Сохранить в фаил',
            font='Calibri 15',
            command=self.fun_file_pass_op
        )

        # Создание списка файлов в виде лицензии
        self.create_cell(frame_pv_v_file, 4)

        self.lb_pass_pv_pf = lb_pass_pv_pf = tk.Label(
            frame_pv_v_file,
            text='<Name File type of license>',
            font='Calibri 18',
            fg='#1E90FF'
            )

        # киличество паролей в файле
        lb_len_pass_pv_v_pf = tk.Label(
            frame_pv_v_file,
            text='Количество паролей в файле:',
            font='Calibri 18'
        )
        combobox_len_pass_pv_v_pf = Combobox(
            frame_pv_v_file,
            font='Calibri 18',
            values=[str(x) for x in range(10, 1001)],
            width=5
        )
        combobox_len_pass_pv_v_pf.set(10)
        self.combobox_len_pass_pv_v_pf = combobox_len_pass_pv_v_pf

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
            command=self.fun_file_pass_pv_v_file
            )
        self.generate_file_pass_pv_pf = generate_file_pass_pv_pf

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
        lb_len_pass_pv_v_pf.grid(row=1, column=0, sticky='w', columnspan=2)
        combobox_len_pass_pv_v_pf.grid(row=1, column=2, sticky='e')
        lb_separating_symbol_pv_v_file.grid(row=2, column=0, columnspan=2,
                                            sticky='w')
        combobox_separating_symbol_pv_v_file.grid(row=2, column=2, sticky='e')
        lb_number_of_sections_pv_v_file.grid(row=3, column=0, columnspan=2,
                                             sticky='w')
        combobox_number_of_sections_pv_v_file.grid(row=3, column=2, sticky='e')
        lb_size_of_sections_pv_v_file.grid(row=4, column=0, columnspan=2,
                                           sticky='w')
        combobox_size_of_sections_pv_v_file.grid(row=4, column=2, sticky='e')
        generate_file_pass_pv_pf.grid(row=1, column=3, rowspan=4)

        # Запуск окна
        window.mainloop()

    def create_cell(self, obj: object, area_size=3):
        """
        Создаю ячейки для рисования потом наних обектов.
        """
        for column in range(area_size):
            obj.columnconfigure(index=column, weight=1)
        for row in range(area_size):
            obj.rowconfigure(index=row, weight=1)

    # Формирую символь для генерации
    def formation_ofa_symbolic_list(
            self,
            password_object,
            number_symbols=True,
            lowercase_letters=True,
            uppercase_letters=True,
            symbols=False
    ):
        number_checkboxes: int = 0
        if number_symbols:
            password_object.list_of_character_types['number_symbols'][0] = True
            number_checkboxes += 1
        else:
            password_object.list_of_character_types['number_symbols'][0] = False

        if lowercase_letters:
            password_object.list_of_character_types['lowercase_letters'][0] = True
            number_checkboxes += 1
        else:
            password_object.list_of_character_types['lowercase_letters'][0] = False

        if uppercase_letters:
            password_object.list_of_character_types['uppercase_letters'][0] = True
            number_checkboxes += 1
        else:
            password_object.list_of_character_types['uppercase_letters'][0] = False

        if symbols:
            password_object.list_of_character_types['symbols'][0] = True
            number_checkboxes += 1
        else:
            password_object.list_of_character_types['symbols'][0] = False

        if number_checkboxes > 0:
            return password_object
        else:
            return None

    def create_simple_password(self, size_password, number_passwords=1):
        """
        Создание пороля вида [########],
        Можно создавать как один так и несколько.
        """
        def type_check(parameters, text):
            try:
                parameters = int(parameters)
            except ValueError:
                showwarning(title="Предупреждение", message=text)
                return False
            else:
                return True

        def checkin_gnegativity(parameters, text):
            try:
                if parameters < 1:
                    raise ValueError(text)
            except Exception as error:
                showwarning(title="Предупреждение", message=error)
                return False
            else:
                return True

        def checkin_none(parameters):
            text = 'Не выбраны не одной чек бокс ?'
            try:
                if parameters is None:
                    raise ValueError(text)
            except Exception as error:
                showwarning(title="Предупреждение", message=error)
                return False
            else:
                return True

        text = 'Не коректно введено количество символов в пароле?'
        if type_check(size_password, text):
            if type_check(number_passwords, text):
                text = 'Отрицательное число в размерности рароля ?'
                size_password = int(size_password)
                number_passwords = int(number_passwords)
                if checkin_gnegativity(size_password, text):
                    if checkin_gnegativity(number_passwords, text):
                        pas = GenerPas(
                            number_passwords,
                            '-',
                            1,
                            size_password
                        )
                        if number_passwords > 1:
                            pas = self.formation_ofa_symbolic_list(
                                pas,
                                self.check_09_op_v_pf.get(),
                                self.check_aw_op_v_pf.get(),
                                self.check_AW_op_v_pf.get(),
                                self.check_symbol_op_v_pf.get()
                            )
                        else:
                            pas = self.formation_ofa_symbolic_list(
                                pas,
                                self.check_09_op.get(),
                                self.check_aw_op.get(),
                                self.check_AW_op.get(),
                                self.check_symbol_op.get()
                            )
                        if checkin_none(pas):
                            pas.createPass()
                            if number_passwords > 1:
                                pas.SaveToFile()
                                self.lb_pass_op_pf['text'] = pas.last_file_name
                            else:
                                self.lb_pass_op['text'] = pas.passwords[0]

    def fun_one_pass(self) -> None:
        """
        функция создаёт один простой парол.
        """
        self.create_simple_password(self.combobox_op.get())

    def copy_password_clipboard(self, event):
        """
        Копирует простой пароль в буфер обмен.
        """
        pyperclip.copy(self.lb_pass_op['text'])

    # функция вывода нового пароля вида лицензии
    def fun_lic_pass(self):
        pas = GenerPas(1,
                       self.combobox_separating_symbol_pv.get(),
                       int(self.combobox_number_of_sections_pv.get()),
                       int(self.combobox_size_of_sections_pv.get())
                       )
        pas.createPass()
        self.lb_pass_pv['text'] = pas.passwords[0]

    # Копирует пароль в буфер обмен
    def copy_password_lic_clipboard(self, event):
        pyperclip.copy(self.lb_pass_pv['text'])

    def fun_file_pass_op(self) -> None:
        """
        функция сохранения количество паролий в фаил.
        """
        self.create_simple_password(
            self.combobox_len_symbol_op_v_pf.get(),
            self.combobox_len_pass_op_v_pf.get()
        )

    # функция сохранения пароли в фаил
    def fun_file_pass_pv_v_file(self) -> None:
        pas = GenerPas(int(self.combobox_len_pass_pv_v_pf.get()),
                       self.combobox_separating_symbol_pv_v_file.get(),
                       int(self.combobox_number_of_sections_pv_v_file.get()),
                       int(self.combobox_size_of_sections_pv_v_file.get()))
        pas.createPass()
        pas.SaveToFile()
        self.lb_pass_pv_pf['text'] = pas.last_file_name
