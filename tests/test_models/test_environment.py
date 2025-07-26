from src.models.environment import Environment


def test_environment_model_fields():
    assert hasattr(Environment, "id")
    assert hasattr(Environment, 'name')
    assert hasattr(Environment, 'created_at')
    assert hasattr(Environment, 'updated_at')
