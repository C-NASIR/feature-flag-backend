from src.models.segment import Segment


def test_segment_model_fields():
    assert hasattr(Segment, "id")
    assert hasattr(Segment, 'key')
    assert hasattr(Segment, 'description')
    assert hasattr(Segment, 'created_at')
    assert hasattr(Segment, 'updated_at')
