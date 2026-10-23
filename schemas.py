from pydantic import BaseModel


class PokemonBase(BaseModel):
  name: str
  type: str
  level: int


class PokemonCreate(PokemonBase):
  pass


class PokemonResponse(PokemonBase):
  id: int

  class Config:
    from_attributes = True

 
