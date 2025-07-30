from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.flag import FlagCreate, FlagUpdate, FlagInDB


def test_flag_create_schema():

    # environment_id: flag can not be created with out this and it comes from the route

    data = {
        "key": "feature-x",
        "name": "Feature X",
        "description": "Enables Feature X",
        "default_variation": "on",
        "enabled": True
    }

    schema = FlagCreate(**data)

    assert schema.key == data["key"]
    assert schema.name == data["name"]
    assert schema.description == data["description"]
    assert schema.default_variation == data["default_variation"]
    assert schema.enabled is True


def test_flag_update_schema():
    data = {
        "name": "New Name",
        "description": "Updated desc",
    }

    schema = FlagUpdate(**data)

    assert schema.name == "New Name"
    assert schema.description == "Updated desc"


def test_flag_response_schema():
    data = {
        "id": uuid4(),
        "key": "feature-y",
        "name": "Feature Y",
        "environment_id": uuid4(),
        "description": "Flag for Y",
        "default_variation": "on",
        "enabled": True,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }

    schema = FlagInDB(**data)

    assert schema.id == data["id"]
    assert schema.key == "feature-y"
    assert schema.environment_id == data["environment_id"]
    assert schema.enabled is True
    assert isinstance(schema.created_at, datetime)
