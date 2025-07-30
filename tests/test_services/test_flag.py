import pytest
from sqlalchemy.orm import Session
from src.schemas.environment import EnvCreate
from src.services.environment_service import create_env
from src.models.flag import Flag
from src.schemas.flag import FlagCreate, FlagUpdate
from src.services import flag_service


@pytest.fixture
def env_id(db_session: Session):
    data = {'key': 'dev', 'name': 'dev'}
    return create_env(db_session, EnvCreate(**data)).id


@pytest.fixture
def flag_data():
    return FlagCreate(
        key="feature-z",
        name="Feature Z",
        description="Enables Feature Z",
        default_variation="on",
        enabled=True
    )


def test_create_flag(db_session: Session, flag_data: FlagCreate, env_id):
    flag = flag_service.create_flag(db_session, env_id, flag_data)

    assert isinstance(flag, Flag)
    assert flag.key == "feature-z"
    assert flag.enabled is True
    assert flag.description == "Enables Feature Z"


def test_get_flag(db_session: Session, flag_data: FlagCreate, env_id):
    created_flag = flag_service.create_flag(db_session, env_id, flag_data)
    fetched_flag = flag_service.get_flag(db_session, created_flag.id)

    assert fetched_flag is not None
    assert fetched_flag.id == created_flag.id


def test_update_flag(db_session: Session, flag_data: FlagCreate, env_id):
    created_flag = flag_service.create_flag(db_session, env_id, flag_data)

    update_data = FlagUpdate(
        name="Updated Feature Z",
        enabled=False
    )

    updated_flag = flag_service.update_flag(
        db_session, created_flag.id, update_data)

    assert updated_flag.name == "Updated Feature Z"
    assert updated_flag.enabled is False


def test_delete_flag(db_session: Session, flag_data: FlagCreate, env_id):
    created_flag = flag_service.create_flag(db_session, env_id, flag_data)
    deleted_result = flag_service.delete_flag(db_session, created_flag.id)
    assert deleted_result['ok'] == True
