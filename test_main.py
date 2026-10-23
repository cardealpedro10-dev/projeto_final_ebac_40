from database import Base, engine, get_db
from fastapi.testclient import TestClient
from main import app
import models
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_test
)


def override_get_db():
  try:
    db = TestingSessionLocal()
    yield db
  finally:
    db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
  Base.metadata.create_all(bind=engine_test)
  yield
  Base.metadata.drop_all(bind=engine_test)


def test_create_pokemon():
  response = client.post(
      "/pokemons/", json={"name": "Pikachu", "type": "Elétrico", "level": 10}
  )
  assert response.status_code == 201
  data = response.json()
  assert data["name"] == "Pikachu"
  assert "id" in data


def test_list_pokemons():
  client.post(
      "/pokemons/", json={"name": "Charmander", "type": "Fogo", "level": 5}
  )
  response = client.get("/pokemons/")
  assert response.status_code == 200
  assert len(response.json()) == 1

 
