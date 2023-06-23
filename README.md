# Online Notary

Онлайн нотариус, создание и редактирование страниц

## Запуск проекта с использованием Docker

1. Установите Docker на вашу систему: [Docker Installation Guide](https://docs.docker.com/get-docker/).
2. Установить Docker Compose: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/).

3. Склонируйте репозиторий проекта:
   ```bash
   git clone https://github.com/ваш_проект.git


Перейдите в директорию проекта:

bash
Copy code
cd ваш_проект
Создайте файл .env и заполните его необходимыми переменными окружения:

bash
Copy code
cp .env.example .env
Замените .env.example на примере настройки переменных окружения вашего проекта.

Соберите и запустите контейнеры Docker:

bash
Copy code
docker-compose up -d --build
Примените миграции и создайте суперпользователя:

bash
Copy code
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
Ваш проект будет доступен по адресу: http://localhost:8000.

Дополнительные команды и настройки
Запуск команды внутри контейнера Docker:

bash
Copy code
docker-compose exec web <команда>
Остановка и удаление контейнеров Docker:

bash
Copy code
docker-compose down
Логи контейнера Docker:

bash
Copy code
docker-compose logs -f
Более подробные настройки Docker и Django можно найти в файле docker-compose.yml и в документации Django.