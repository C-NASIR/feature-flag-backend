from src.schemas.flag import FlagCreate
from src.services.flag_service import create_flag, get_flags


def test_create_flag(db_session):
    flag_data = FlagCreate(key='beta_key', name='beta_feature',
                           description='beta feature', enabled=True)
    new_flag = create_flag(db_session, flag_data)

    assert new_flag.name == 'beta_feature'
    assert new_flag.enabled is True


def test_get_all_flags(db_session):
    flags = get_flags(db_session)
    assert isinstance(flags, list)
