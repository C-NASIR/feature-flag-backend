import pytest
from src.schemas.variation import (
    VariationCreate, VariationUpdate
)
from src.services.variation_service import (
    get_variations, get_variation, update_variation,
    create_variation, delete_variation
)


@pytest.fixture
def variation_data(flag_id):
    return VariationCreate(
        key='key 1', value='value 1', flag_id=flag_id)


def test_create_variation(db_session, variation_data):
    variation = create_variation(db_session, variation_data)
    assert variation.key == 'key 1'
    assert variation.value == 'value 1'


def test_get_variation(db_session, variation_data):
    created = create_variation(db_session, variation_data)
    variation = get_variation(db_session, created.id)

    assert variation.id == created.id
    assert variation.key == created.key


def test_get_variations(db_session, variation_data):
    create_variation(db_session, variation_data)
    create_variation(db_session, variation_data)

    assert len(get_variations(db_session)) == 2


def test_update_variation(db_session, variation_data):
    created = create_variation(db_session, variation_data)
    updated_data = VariationUpdate(value='updated value')
    updated = update_variation(db_session, created.id, updated_data)

    assert created.id == updated.id
    assert created.key == updated.key
    assert updated.value == 'updated value'


def test_delete_variation(db_session, variation_data):
    created = create_variation(db_session, variation_data)
    deleted = delete_variation(db_session, created.id)
    assert deleted['ok'] == True
    assert len(get_variations(db_session)) == 0
