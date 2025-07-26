from src.models.environment import Environment
from src.schemas.environment import EnvCreate, EnvInDB, EnvUpdate
from src.services.environment_service import (
    get_envs, get_env, update_env,
    create_env, delete_env
)


def test_create_env(db_session):
    env = create_env(db_session, EnvCreate(name='A'))
    assert isinstance(env, Environment)
    assert env.name == 'A'


def test_get_env(db_session):
    env = create_env(db_session, EnvCreate(name='B'))
    fetched = get_env(db_session, env.id)
    assert fetched.id == env.id


def test_get_envs(db_session):
    create_env(db_session, EnvCreate(name='A'))
    create_env(db_session, EnvCreate(name='B'))
    envs = get_envs(db_session)
    assert len(envs) == 2


def test_update_env(db_session):
    created = create_env(db_session, EnvCreate(name='A'))
    updated = update_env(db_session, created.id, EnvUpdate(name='updated'))
    assert updated.name == 'updated'
    assert created.id == updated.id


def test_delete_env(db_session):
    created = create_env(db_session, EnvCreate(name='to be deleted'))
    deleted_result = delete_env(db_session, created.id)
    assert deleted_result['ok'] == True
    assert len(get_envs(db_session)) == 0
