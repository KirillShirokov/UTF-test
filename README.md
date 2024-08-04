
##  Установка и настройка проекта
### Подготовка сервера к установке проекта
- Склонируйте проект из репозитория
- Создайте файл .env в директории */infra* проекта и укажите в нем переменные указанные в .env.example
- Настройте виртуальное окружение
- Установите пакеты из файла requirements.txt
- Выполните миграции
```
git clone https://github.com/<your_profile>/<your_project>/
python3 -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

## Технологии:

**Python**
**Django**

## Разработчик
Кирилл Широков