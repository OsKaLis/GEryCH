<div id="header" align="center">
  <h1>Проект GEryCH</h1>
</div>

## Используемые технологии:
![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Python 3.12](https://img.shields.io/badge/QT-6.7.1-brightgreen.svg?style=flat&logo=qt&logoColor=white)

## Функционал генератора:
+ Сгенерировать пароль согласно настройкам
+ Сгененировать пароль вида  ####-####-#### или согласно настройкам
+ Может сгененрировать множство простых паролей в фаил согласно настройкам 
+ Может сгененрировать множство паролей вида key в фаил согласно настройкам 

## Как развернуть проект на локальной машине:

### 1. Клонируем проект:
```
git clone git@github.com:OsKaLis/GEryCH.git
```

### 2. Переходим в директорию проекта:
```
cd GEryCH/
```

### 3. Необходимо проверить установленную версию Python:
```
python3 -V
```
- Если у вас версия 3.12.*, то можно переходить к шагу 4.
- Если версия не 3.12.*, то необходимо её установить.

### 4. Устанвка `poetry`:
```
pip install poetry
```
- Версия `Poetry 1.8.3`
- [Не большое руководство по `poetry`](https://habr.com/ru/articles/740376/)

### 5. Проверка что `poetry` установлен:
```
poetry -V
```

### 6. Устанавливаем установка зависимости для окружения:
```
poetry install
```

### 7. Запуск приложение:
```
python qt-gerych.py
```


## Скриншот приложения:
![Интерфейс программы GEryCH](https://github.com/OsKaLis/GEryCH/blob/8a9c36c2ccee63d744fd8acadb5bfd511656c791/images/GEryCH.png)


## Планы по доработке:
+ Собрать 2 версии одну для Linux вторую Wimdows исполняемые файлы


## Автор: Юшко Ю.Ю.
