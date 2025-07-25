# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.db.session import get_db
from src.db.base import Base
from src.main import app
import os

# Load test database URL from environment variable or set it directly
TEST_DATABASE_URL = os.getenv("DATABASE_URL_TEST")

# Create the PostgreSQL test engine
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Create and drop all tables before/after tests


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Fixture for DB session


@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


# Truncate all tables after each test to clean state
@pytest.fixture(autouse=True)
def clean_tables():
    yield  # Run the test
    with engine.connect() as conn:
        conn.execute(text("""
            DO $$ DECLARE
                r RECORD;
            BEGIN
                -- Disable referential integrity temporarily
                EXECUTE 'TRUNCATE ' || 
                    string_agg(format('%I.%I', schemaname, tablename), ', ') || 
                    ' RESTART IDENTITY CASCADE'
                FROM pg_tables
                WHERE schemaname = 'public';
            END $$;
        """))
        conn.commit()


# Fixture for FastAPI test client with DB dependency override
@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
