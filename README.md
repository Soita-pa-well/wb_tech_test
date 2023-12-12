# wb_tech_test
Тестовый проект WB-Tech: Реализованы сущности комнады и ее участников и главная страница в виде html шаблона для наглядности заполнения БД по адресу /
### как запустить проект:
Перейти в директорию test_project и Запустить docker-compose
```bash
docker-compose up -d
```
Выполнить миграции 
```bash
docker-compose exec wb_test python manage.py migrate
```
Собрать статику
```bash
docker-compose exec wb_test python manage.py collectstatic
```
Копировать статику в контейнер gateway
```bash
docker-compose exec wb_test cp -r /app/static/. /static/static/
```


