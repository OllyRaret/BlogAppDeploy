# Блог-сервер на Django + PostgreSQL

## Технологии
- Python 3.9+
- Django
- PostgreSQL
- Docker + Docker Compose
- GitHub Actions

## Запуск проекта
1. Убедитесь, что установлены Docker и Docker Compose
2. Клонируйте репозиторий
3. Настройте окружение (файл .env):
```
# Настройки Django
SECRET_KEY=django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Настройки PostgreSQL
POSTGRES_NAME=db_name
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
4. Запустите сервисы:
```bash
docker-compose up -d
```
5. Приложение доступно на `http://localhost:8080`

## API Endpoints

### GET /posts
Возвращает список всех постов:
```bash
curl http://localhost:8080/posts
```
Пример ответа:
```json
[
  {"id": 1, "title": "Hello world", "content": "My first post!"}
]
```

### POST /posts
Добавляет новый пост:
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"title":"New post","content":"Post content"}' \
  http://localhost:8080/posts
```
Пример ответа:
```json
{"id": 2, "title": "New post", "content": "Post content"}
```

## Проверка работоспособности
1. Проверьте статус контейнеров:
```bash
docker-compose ps
```
2. Выполните тестовые запросы (см. раздел API)
3. Проверьте логи:
```bash
tail -f logs/django/*.log logs/postgres/*.log
```

## Настройка автоматического деплоя
1. Добавьте секреты в GitHub:
   - `SSH_PRIVATE_KEY` - приватный SSH-ключ для доступа к серверу
   - `SERVER_HOST` - IP/домен сервера
   - `SERVER_USER` - пользователь для подключения
   - `DOCKER_HUB_USERNAME` - имя пользователя Docker Hub
   - `DOCKER_HUB_TOKEN` - токен для подключения в Docker Hub

2. При push в ветку `master` будет:
   - Собран Docker образ
   - Развернуто приложение на целевом сервере через SSH

## Требования к серверу для деплоя
- Установленные Docker и Docker Compose
- Доступ по SSH
- Права пользователя на работу с Docker
