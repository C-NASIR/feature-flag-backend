from src.models import Condition


def test_condition_model_fields():
    assert hasattr(Condition, 'id')
    assert hasattr(Condition, 'attribute')
    assert hasattr(Condition, 'operator')
    assert hasattr(Condition, 'value')
    assert hasattr(Condition, 'rule_id')
    assert hasattr(Condition, 'created_at')
    assert hasattr(Condition, 'updated_at')
    assert hasattr(Condition, 'rule')
