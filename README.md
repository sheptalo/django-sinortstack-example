# clean-DI with Django as Adapter

# Start project

```bash
python .\src\entrypoint.py
```

## Start with Django Adapter

```bash
python .\src\adapters\django\manage.py runserver
```

# DI

Change repository in 1 line

```python
# src/application/containers.py

# DJANGO ORM
class ApplicationContainer(containers.DeclarativeContainer):
    repositories = providers.Container(DjangoRepositoryContainer)
    ...


# SQLite
class ApplicationContainer(containers.DeclarativeContainer):
    repositories = providers.Container(SQLiteRepositoryContainer)
    ...
```

# TODO 

- [ ] pytest tests
