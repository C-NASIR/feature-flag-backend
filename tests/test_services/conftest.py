import pytest
from sqlalchemy.orm import Session
from src.schemas.environment import EnvCreate
from src.services.environment_service import create_env
from src.schemas.flag import FlagCreate
from src.schemas.rule import RuleCreate
from src.services import flag_service, rule_service


@pytest.fixture
def env_id(db_session: Session):
    data = {'key': 'dev', 'name': 'dev'}
    return create_env(db_session, EnvCreate(**data)).id


@pytest.fixture
def flag_id(db_session: Session, env_id):
    flag_data = FlagCreate(
        key="feature-z",
        name="Feature Z",
        description="Enables Feature Z",
        default_variation="on",
        enabled=True
    )
    return flag_service.create_flag(db_session, env_id, flag_data).id


@pytest.fixture
def flag_id(db_session: Session, env_id):
    flag_data = FlagCreate(
        key="feature-z",
        name="Feature Z",
        description="Enables Feature Z",
        default_variation="on",
        enabled=True
    )
    return flag_service.create_flag(db_session, env_id, flag_data).id


@pytest.fixture
def rule_id(db_session, flag_id):
    data = {'variation': 'on', 'priority': 3, 'conditions': []}
    rule_data = RuleCreate(**data)
    return rule_service.create_rule(db_session, flag_id, rule_data).id
