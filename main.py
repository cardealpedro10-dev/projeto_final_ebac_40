from database import engine, get_db
import models
from fastapi import Depends, FastAPI, HTTPException, status
import models, schemas
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Pokémons - Projeto Final EBAC",
    description="API RESTful para gerenciar registros de pokémons usando FastAPI e SQLAlchemy.",
    version="1.0.0",
)


@app.post(
    "/pokemons/",
    response_model=schemas.PokemonResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_pokemon(
    pokemon: schemas.PokemonCreate, db: Session = Depends(get_db)
):
  db_pokemon = (
      db.query(models.PokemonModel)
      .filter(models.PokemonModel.name == pokemon.name)
      .first()
  )
  if db_pokemon:
    raise HTTPException(
        status_code=400, detail="Pokémon já cadastrado com esse nome."
    )
  new_pokemon = models.PokemonModel(
      name=pokemon.name, type=pokemon.type, level=pokemon.level
  )
  db.add(new_pokemon)
  db.commit()
  db.refresh(new_pokemon)
  return new_pokemon


@app.get("/pokemons/", response_model=list[schemas.PokemonResponse])
def list_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  return db.query(models.PokemonModel).offset(skip).limit(limit).all()


@app.get("/pokemons/{pokemon_id}", response_model=schemas.PokemonResponse)
def get_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
  pokemon = (
      db.query(models.PokemonModel)
      .filter(models.PokemonModel.id == pokemon_id)
      .first()
  )
  if not pokemon:
    raise HTTPException(status_code=404, detail="Pokémon não encontrado.")
  return pokemon


@app.put("/pokemons/{pokemon_id}", response_model=schemas.PokemonResponse)
def update_pokemon(
    pokemon_id: int,
    updated_data: schemas.PokemonCreate,
    db: Session = Depends(get_db),
):
  pokemon = (
      db.query(models.PokemonModel)
      .filter(models.PokemonModel.id == pokemon_id)
      .first()
  )
  if not pokemon:
    raise HTTPException(status_code=404, detail="Pokémon não encontrado.")

  pokemon.name = updated_data.name
  pokemon.type = updated_data.type
  pokemon.level = updated_data.level
  db.commit()
  db.refresh(pokemon)
  return pokemon


@app.delete("/pokemons/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
  pokemon = (
      db.query(models.PokemonModel)
      .filter(models.PokemonModel.id == pokemon_id)
      .first()
  )
  if not pokemon:
    raise HTTPException(status_code=404, detail="Pokémon não encontrado.")
  db.delete(pokemon)
  db.commit()
  return None

 
