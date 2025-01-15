```markdown
# Проект TestBasket создан для выполнения тестового задания Компании ООО "Баксэт". 

TestBasket — это проект на DRF с использованием PostgreSQL, контейнеризированный с помощью Docker.

## Как запустить проект

Следуйте этим шагам для запуска проекта:
```
### 1. Убедитесь, что у вас установлены:
```
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)
```
### 2. Клонируйте репозиторий
```bash
git clone https://github.com/curabby/TestBakset.git
cd TestBakset
```

### 3. Создайте файл `.env`
Создайте файл `.env` в корневой директории проекта со следующим содержанием:
```env
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
SECRET_KEY=your_django_secret_key
DEBUG=True
```
Замените `your_postgres_user`, `your_postgres_password`, `your_postgres_db` и `your_django_secret_key` на ваши собственные значения.

### 4. Соберите и запустите контейнеры
Выполните следующую команду для сборки и запуска контейнеров:
```bash
docker-compose up --build
```

### 5. Откройте приложение в браузере
Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

---

## 📚 Описание API эндпоинтов

### 1. **Создание VPS**
- **URL:** `http://localhost:8000/api/v1/create/`
- **Метод:** `POST`
- **Описание:** Создает новый VPS.
- **Пример тела запроса (JSON):**
  ```json
  {
      "cpu": 2,
      "ram": 4,
      "hdd": 50,
      "status": "started"
  }
  ```
- **Ответ (успешный):**
  ```json
  {
      "uid": "194b375a-ce5f-40f2-ad12-0fe3b444a928",
      "cpu": 2,
      "ram": 4,
      "hdd": 50,
      "status": "started"
  }
  ```

---

### 2. **Получение списка VPS**
- **URL:** `http://localhost:8000/api/v1/getvps/`
- **Метод:** `GET`
- **Описание:** Возвращает список всех VPS.
- **Параметры для фильтрации:**
  status (started, blocked, stopped, restarted)
  cpu
  ram
  hdd
  
- **Пример ответа:**
  ```json
  [
      {
          "uid": "194b375a-ce5f-40f2-ad12-0fe3b444a928",
          "cpu": 2,
          "ram": 4,
          "hdd": 50,
          "status": "started"
      },
      {
          "uid": "a6504d53-37b0-4648-8686-351e055c744f",
          "cpu": 4,
          "ram": 8,
          "hdd": 100,
          "status": "stopped"
      }
  ]
  ```

---

### 3. **Получение конкретного VPS**
- **URL:** `http://localhost:8000/api/v1/getvps/<uid>/`
- **Метод:** `GET`
- **Описание:** Возвращает данные о конкретном VPS по его уникальному идентификатору (UID).
- **Пример запроса:**
  ```
  http://localhost:8000/api/v1/getvps/194b375a-ce5f-40f2-ad12-0fe3b444a928/
  ```
- **Пример ответа:**
  ```json
  {
      "uid": "194b375a-ce5f-40f2-ad12-0fe3b444a928",
      "cpu": 2,
      "ram": 4,
      "hdd": 50,
      "status": "started"
  }
  ```

---

### 4. **Обновление статуса VPS**
- **URL:** `http://localhost:8000/api/v1/status-update/<uid>/`
- **Метод:** `PATCH`
- **Описание:** Обновляет статус VPS (например, `started` -> `stopped`).
- **Пример тела запроса (JSON):**
  ```json
  {
      "status": "stopped"
  }
  ```
- **Пример запроса:**
  ```
  http://localhost:8000/api/v1/status-update/194b375a-ce5f-40f2-ad12-0fe3b444a928/
  ```
- **Пример ответа:**
  ```json
  {
    "message": "Status updated successfully",
    "status": "restarted"
}
  ```
---

## 📂 Структура проекта
- **Core/** — основное приложение Django с моделями и API.
- **Dockerfile** — файл для создания образа Docker.
- **docker-compose.yml** — файл для управления контейнерами.
- **requirements.txt** — зависимости Python.

## 🛠️ Полезные команды
- Остановка контейнеров:
  ```bash
  docker-compose down
  ```
- Просмотр логов:
  ```bash
  docker-compose logs -f
  ```
