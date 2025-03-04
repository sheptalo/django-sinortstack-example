# Пример django clean-DI используя архитектуру sinorstack

## start

```bash
cd src
python manage.py runserver
```

Для того чтобы использовать вместо DJANGO ORM, SQL запросы нужно поменять в `src/config/containers.py` следующее:

```python
# Вариант для DJANGO ORM
class ApplicationContainer(containers.DeclarativeContainer):
    repositories = providers.Container(DjangoRepositoryContainer)
    ...

# Вариант для SQL
class ApplicationContainer(containers.DeclarativeContainer):
    repositories = providers.Container(SQLiteRepositoryContainer)
    ...
```
