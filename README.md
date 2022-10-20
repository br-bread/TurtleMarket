![project workflow](https://github.com/br-bread/homework/actions/workflows/python-package.yml/badge.svg)
# Homework
Репозиторий для сдачи домашек по яндексу
___
## Инструкция по запуску

- ### Установить virtualenv
```
pip install virtualenv
```
- ### Создать venv
#### Windows
```
python -m venv venv
```
#### Linux
```
python3 -m venv venv
```
- ### Активировать venv
#### Windows
(Для Windows сначала нужно разрешить выполнение PowerShell скриптов)
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
```
venv\Scripts\activate.ps1
```
#### Linux
```
source venv/bin/activate
```
- ### Установить requirements.txt
```
pip install -r requirements.txt
```
- ### Запустить проект
#### Windows
```
python manage.py runserver
```
#### Linux
```
python3 manage.py runserver
```
Для просмотра страницы перейти на http://127.0.0.1:8000 

Для хранения параметров DEBUG и SECRET_KEY используются переменные окружения. 
При необходимости можно создать и установить значения, или поменять значение в settings.py