from src.schemas.variation import (
    VariationCreate, VariationUpdate
)
from src.services.variation_service import (
    get_variations, get_variation, update_variation,
    create_variation, delete_variation
)


data = [
    {'key': 'key a', 'value': 'value a',
        'description': 'nothing here a'},
    {'key': 'key b', 'value': 'value b',
        'description': 'nothing here b'}
]


def test_create_variation(db_session, flag_id):
    var_data = VariationCreate(**data[0])
    variation = create_variation(db_session, flag_id, var_data)
    assert variation.key == data[0]['key']
    assert variation.value == data[0]['value']


def test_get_variation(db_session, flag_id):
    var_data = VariationCreate(**data[0])
    created = create_variation(db_session, flag_id, var_data)
    variation = get_variation(db_session, created.id)

    assert variation.id == created.id
    assert variation.key == created.key


def test_get_variations(db_session, flag_id):
    var_data1 = VariationCreate(**data[0])
    var_data2 = VariationCreate(**data[1])
    create_variation(db_session, flag_id, var_data1)
    create_variation(db_session, flag_id, var_data2)

    assert len(get_variations(db_session)) == 2


def test_update_variation(db_session, flag_id):
    var_data = VariationCreate(**data[0])
    created = create_variation(db_session, flag_id, var_data)
    updated_data = VariationUpdate(value='updated value')
    updated = update_variation(db_session, created.id, updated_data)

    assert created.id == updated.id
    assert created.key == updated.key
    assert updated.value == 'updated value'


def test_delete_variation(db_session, flag_id):
    var_data = VariationCreate(**data[0])
    created = create_variation(db_session, flag_id, var_data)
    deleted = delete_variation(db_session, created.id)
    assert deleted['ok'] == True
    assert len(get_variations(db_session)) == 0
