from src.models import Flag


def test_flag_model_fields():
    assert hasattr(Flag, 'id')
    assert hasattr(Flag, 'key')
    assert hasattr(Flag, 'name')
    assert hasattr(Flag, 'description')
    assert hasattr(Flag, 'environment_id')
    assert hasattr(Flag, 'default_variation')
    assert hasattr(Flag, 'enabled')
    assert hasattr(Flag, 'created_at')
    assert hasattr(Flag, 'updated_at')
    assert hasattr(Flag, 'variations')
    assert hasattr(Flag, 'rules')
