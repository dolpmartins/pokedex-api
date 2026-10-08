from fastapi import FastAPI

from app.models import Personagem
from app.pokeapi import buscar_personagem

app = FastAPI(title="Pokédex API")


@app.get("/personagens/{nome}")
def obter_personagem(nome: str) -> Personagem:
    return buscar_personagem(nome)
