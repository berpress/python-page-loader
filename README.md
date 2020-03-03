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
| INFO  | 20  |
|  DEBUG  | 10  |
|  NOTSET  | 0 |

По умолчанию установлено значение 20 (INFO)

Например, запустим утилиту с выводом логов (INFO)
``` sh
    loader --output=/var/tmp https://hexlet.io/courses --l=20
```
Результат
``` sh
    2020-03-03 21:35:38,897 - root - INFO - Get file name hexlet-io-courses from https://hexlet.io/courses
2020-03-03 21:35:39,003 - root - INFO - Get download link https://hexlet.io/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js
2020-03-03 21:35:39,249 - root - INFO - Get file name cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min from /cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js
2020-03-03 21:35:39,249 - root - INFO - Create /var/tmp/hexlet-io-courses_files folder
2020-03-03 21:35:39,250 - root - INFO - Write data to /var/tmp/hexlet-io-courses_files/cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min.js file
2020-03-03 21:35:39,250 - root - INFO - Change link to /var/tmp/hexlet-io-courses_files/cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min.js
2020-03-03 21:35:39,294 - root - INFO - Create /var/tmp folder
2020-03-03 21:35:39,294 - root - INFO - Write data to /var/tmp/hexlet-io-courses.html file
2020-03-03 21:35:39,294 - root - INFO - Finish write data to hexlet-io-courses file in /var/tmp folder

```
Если уровень логгирования будет выше 20 (DEBUG и INFO), то будет отображаться прогресс закрузки.

[![asciicast](https://asciinema.org/a/XYE7IARob3mkXYvxawLk7u1QA.svg)](https://asciinema.org/a/XYE7IARob3mkXYvxawLk7u1QA)

