![project workflow](https://github.com/br-bread/homework/actions/workflows/python-package.yml/badge.svg)
# Homework
Репозиторий для сдачи домашек по яндексу
___
## Инструкция по запуску

### Linux

- Установить virtualenv (pip install virtualenv)
- Создать venv (python3 -m venv venv)
- Активировать venv (source venv/bin/activate)
- Установить requirements.txt (pip install -r requirements.txt)
- python3 manage.py runserver

### Windows

- Установить virtualenv (pip install virtualenv)
- Создать venv (python -m venv venv)
- Разрешить выполнение PowerShell скриптов (Set-ExecutionPolicy Unrestricted -Scope Process)
- Активировать venv (venv\Scripts\activate.ps1)
- Установить requirements.txt (pip install -r requirements.txt)
- python manage.py runserver

Для просмотра страницы перейти на http://127.0.0.1:8000 

Для хранения параметров DEBUG и SECRET_KEY используются переменные окружения. 
При необходимости можно создать и установить значения, или поменять значение в settings.py
