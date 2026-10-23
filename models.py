from database import Base
from sqlalchemy import Column, Integer, String


class PokemonModel(Base):
  __tablename__ = "pokemons"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True, nullable=False)
  type = Column(String, nullable=False)
  level = Column(Integer, nullable=False)