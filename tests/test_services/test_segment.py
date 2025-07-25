from src.models.segment import Segment
from src.schemas.segment import SegmentCreate, SegmentUpdate
from src.services.segment_service import (
    get_segments, get_segment, create_segment,
    update_segment, delete_segment
)


def test_create_segment(db_session):
    segment_in = SegmentCreate(key='Segment X', description='Service test')
    segment = create_segment(db_session, segment_in)
    assert isinstance(segment, Segment)
    assert segment.key == 'Segment X'


def test_get_segment(db_session):
    segment_in = SegmentCreate(key='Segment Y')
    segment = create_segment(db_session, segment_in)
    fetched = get_segment(db_session, segment.id)
    assert fetched.id == segment.id


def test_get_segments(db_session):
    create_segment(db_session, SegmentCreate(key="Segment A"))
    create_segment(db_session, SegmentCreate(key="Segment B"))
    segments = get_segments(db_session)
    assert len(segments) == 2


def test_update_segment(db_session):
    created = create_segment(db_session, SegmentCreate(
        key='Segment Z', description='desc'))
    updated = update_segment(db_session, created.id,
                             SegmentUpdate(key='Updated Z'))
    assert updated.key == 'Updated Z'
    assert updated.description == 'desc'


def test_delete_segment(db_session):
    created = create_segment(db_session, SegmentCreate(key='To delete'))
    deleted_result = delete_segment(db_session, created.id)
    assert deleted_result['ok'] == True
    assert len(get_segments(db_session)) == 0
