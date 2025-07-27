from src.models import Rule


def test_rule_model_field():
    assert hasattr(Rule, 'id')
    assert hasattr(Rule, 'variation')
    assert hasattr(Rule, 'priority')
    assert hasattr(Rule, 'flag_id')
    assert hasattr(Rule, 'created_at')
    assert hasattr(Rule, 'updated_at')
    assert hasattr(Rule, 'flag')
    assert hasattr(Rule, 'conditions')
    assert hasattr(Rule, 'segments')
