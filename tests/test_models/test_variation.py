from src.models import Variation


def test_variation_model_fields():
    assert hasattr(Variation, 'id')
    assert hasattr(Variation, 'flag_id')
    assert hasattr(Variation, 'value')
    assert hasattr(Variation, 'created_at')
    assert hasattr(Variation, 'updated_at')
