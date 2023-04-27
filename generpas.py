from random import choice
import time


# Клас генерации
class GenerPas():
    def __init__(self, kolPass: int, razSinvol, kolSekciy, dlinaSekcii):
        self.kolPass: int = kolPass
        self.razSinvol = razSinvol
        self.kolSekciy = kolSekciy
        self.dlinaSekcii = dlinaSekcii
        self.passwords = []
        self.last_file_name = 'default_name_file'

        # Символи для генерации
        self.number_symbols = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        self.lowercase_letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p',  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        self.uppercase_letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        self.symbols = [
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
            '+', '[', ']', '{', '}', ':', ':', '|', '<', '>', '?'
        ]

        self.list_of_character_types = {
            'number_symbols': [True, self.number_symbols],
            'lowercase_letters': [True, self.lowercase_letters],
            'uppercase_letters': [True, self.uppercase_letters],
            'symbols': [False, self.symbols]
        }

    # Создаю масим символов для генерации
    def CreatebBaseSymbols(self):
        rez = []
        for name in self.list_of_character_types:
            if self.list_of_character_types[name][0]:
                rez += self.list_of_character_types[name][1]
        return rez

    # Создание заданое количество паролей
    def createPass(self):
        skleu = ""
        genPass = ""
        for i in range(0, self.kolPass):
            for j in range(0, self.kolSekciy):
                for q in range(0, self.dlinaSekcii):
                    if q < self.dlinaSekcii:
                        genPass += choice(self.CreatebBaseSymbols())
                if j + 1 < self.kolSekciy:
                    skleu += genPass + self.razSinvol
                else:
                    skleu += genPass
                genPass = ""
            self.passwords.insert(i, skleu)
            skleu = ""

    # Показ пароля из созданых
    def ridPass(self, nom):
        return self.passwords[nom]

    # вывести все созданые пароли
    def FulCreatePass(self):
        for i in range(0, self.kolPass):
            print(f'Pass № {i+1} : {self.passwords[i]}')

    # Сохранить в фаил созданые пароли (*.txt)
    def SaveToFile(self):
        Namefile = time.strftime("%Y_%m_%d_%H.%M.%S", time.localtime())
        self.last_file_name = Namefile + "_pass.txt"
        PTF = open(self.last_file_name, "w")
        for i in range(0, self.kolPass):
            PTF.write("Pass №" + str(i+1) + " : " + self.passwords[i] + '\n')
        PTF.close()
