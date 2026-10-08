import requests
from fastapi import FastAPI, HTTPException

from app.exceptions import PersonagemNaoEncontrado
from app.models import Personagem
from app.pokeapi import buscar_personagem

app = FastAPI(title="Pokédex API")


@app.get("/personagens/{nome}")
def obter_personagem(nome: str) -> Personagem:
    try:
        return buscar_personagem(nome)
    except PersonagemNaoEncontrado:
        raise HTTPException(
            status_code=404,
            detail=f"Ops! O personagem '{nome}' não foi encontrado na Pokédex.",
        )
    except (requests.ConnectionError, requests.Timeout):
        raise HTTPException(
            status_code=503,
            detail="Não foi possível falar com a PokéAPI agora. Tente novamente em instantes.",
        )
