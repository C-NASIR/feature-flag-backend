# tests/schemas/test_env.py

import pytest
from uuid import uuid4
from datetime import datetime, timezone
from src.schemas.environment import EnvCreate, EnvUpdate, EnvInDB


def test_env_create_schema():
    data = {"name": "Production", }
    schema = EnvCreate(**data)
    assert schema.name == data["name"]


def test_env_update_schema():
    data = {"name": "New Name"}
    schema = EnvUpdate(**data)
    assert schema.name == "New Name"


def test_env_response_schema():
    data = {
        "id": uuid4(),
        "name": "production",
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }

    schema = EnvInDB(**data)

    assert schema.id == data["id"]
    assert schema.name == "production"
    assert isinstance(schema.created_at, datetime)
