[![Build Status](https://travis-ci.org/berpress/python-project-lvl3.svg?branch=master)](https://travis-ci.org/berpress/python-project-lvl3)

[![Test Coverage](https://api.codeclimate.com/v1/badges/af2c5b1f166e9bf74575/test_coverage)](https://codeclimate.com/github/berpress/python-project-lvl3/test_coverage)

[![Maintainability](https://api.codeclimate.com/v1/badges/af2c5b1f166e9bf74575/maintainability)](https://codeclimate.com/github/berpress/python-project-lvl3/maintainability)


### Загрузчик страниц

1. Установка 
``` sh
python3 -m pip install --user --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple litovsky-page-loader

```
2. Использование
Утилита принимает на вход один обязательный параметр - url страницы для скачивания. В результате скачивается страница и сохраняются локальные ресурсы, если они есть.
Пример
``` sh
    loader https://hexlet.io/courses
```
Для сохранения страницы в определенную папку необходимо указать парметр --output. Если параметр --output не указан, то будет создана временная папка.

Для управления логами предусмотрен параметр --logging_level. Необходимо указать значение от 0 до 50, согласно этой таблице 

|  Level | number  |
|---|---|
|CRITICAL   | 50  |
|  ERROR | 40  |
| WARNING  | 30  |
|  DEBUG  | 10  |
|  NOTSET  | 0 |

По умолчанию установлено значение 20 (INFO)

Пример 
``` sh
    loader https://hexlet.io/courses
```
Ре
