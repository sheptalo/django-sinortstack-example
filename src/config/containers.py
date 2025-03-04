from dependency_injector import containers, providers

from application.controllers.users import RegisterUserController
from infrastructure.repositories.user_repository import (
    DjangoUserRepository,
    SQLiteUserRepository,
)
from use_cases.user import RegisterUserUseCase


class DjangoRepositoryContainer(containers.DeclarativeContainer):
    user = providers.Factory(DjangoUserRepository)


class SQLiteRepositoryContainer(containers.DeclarativeContainer):
    user = providers.Factory(SQLiteUserRepository)


class UseCaseContainer(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    register = providers.Factory(RegisterUserUseCase, repo=repositories.user)


class ControllerContainer(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    use_cases = providers.DependenciesContainer()
    register_user = providers.Factory(
        RegisterUserController,
        use_case=use_cases.register,
    )


class ApplicationContainer(containers.DeclarativeContainer):
    repositories = providers.Container(DjangoRepositoryContainer)
    use_cases = providers.Container(UseCaseContainer, repositories=repositories)
    controllers = providers.Container(
        ControllerContainer, repositories=repositories, use_cases=use_cases
    )
