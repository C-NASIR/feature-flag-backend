import pytest
from sqlalchemy.orm import Session
from src.schemas.environment import EnvCreate
from src.services.environment_service import create_env
from src.schemas.flag import FlagCreate
from src.services import flag_service


@pytest.fixture
def env_id(db_session: Session):
    return create_env(db_session, EnvCreate(name='A')).id


@pytest.fixture
def flag_id(db_session: Session, env_id):
    flag_data = FlagCreate(
        key="feature-z",
        name="Feature Z",
        environment_id=env_id,
        description="Enables Feature Z",
        default_variation="on",
        enabled=True
    )

    return flag_service.create_flag(db_session, flag_data).id
