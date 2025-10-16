# 👗 Digital Wardrobe

**Digital Wardrobe** — это веб-приложение на Django, которое помогает пользователям создавать свой цифровой гардероб: загружать вещи, составлять образы и управлять коллекцией одежды онлайн.

---

## 🌐 Демо

🖥️ Сайт доступен по адресу:  
👉 **[https://digitalwardrobe.asia](https://digitalwardrobe.asia)**

---

## 🚀 Функциональность

- 👤 Регистрация и авторизация пользователей  
- 👕 Добавление вещей в личный гардероб  
- 🧩 Создание и редактирование образов (Outfits)  
- 🖼️ Загрузка изображений с автоматическим удалением фона  
- 💬 Простое и понятное управление вещами  
- 🔐 Личный кабинет пользователя  
- ⚙️ Django Admin панель для управления данными  

---

## 🧠 Технологии

- **Backend:** Django 4.2, Django REST Framework  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Database:** SQLite3  
- **Deployment:** Render + custom domain (digitalwardrobe.asia)  
- **Tools:** Gunicorn, Python-dotenv, rembg (удаление фона)  

---

## ⚙️ Установка и запуск локально

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/nzhnvibec0der/digital_wardrobe.git
   cd digital_wardrobe
Создай и активируй виртуальное окружение:

bash
Копировать код
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
Установи зависимости:

bash
Копировать код
pip install -r requirements.txt
Применяй миграции и запусти сервер:

bash
Копировать код
python manage.py migrate
python manage.py runserver
Открой в браузере:

cpp
Копировать код
http://127.0.0.1:8000/
📦 API (Django REST Framework)
Endpoint	Метод	Описание
/api/items/	GET	Получить список всех вещей
/api/items/<id>/	GET	Получить детали вещи
/api/outfits/	GET	Получить список образов
/api/outfits/<id>/	GET	Детали конкретного образа

🧰 Django Admin
Доступна панель администратора для управления пользователями, вещами и образами:
👉 /admin/

🛠️ Структура проекта
bash
Копировать код
digital_wardrobe/
├── wardrobe/           # Основное приложение гардероба
├── users/              # Приложение для пользователей
├── templates/          # HTML шаблоны
├── static/             # CSS, JS, изображения
├── media/              # Загружаемые пользователями файлы
├── manage.py
└── requirements.txt
🏆 Автор
👤 Nurzhan Saruar
GitHub: @nzhnvibec0der

📅 Аттестация
✅ Развёрнут на хостинге Render
✅ Работает по домену digitalwardrobe.asia
✅ Соответствует всем требованиям итогового задания по Django
✅ Доступен онлайн до 01.01.2026

💬 “Digital Wardrobe — это не просто гардероб. Это стиль в цифровом мире.”
