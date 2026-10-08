from http import HTTPStatus

import requests

from app.exceptions import PersonagemNaoEncontrado
from app.models import Personagem, montar_personagem

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def buscar_personagem(nome: str) -> Personagem:
    resposta = requests.get(f"{BASE_URL}/{nome.lower()}", timeout=10)
    if resposta.status_code == HTTPStatus.NOT_FOUND:
        raise PersonagemNaoEncontrado(nome)
    resposta.raise_for_status()
    return montar_personagem(resposta.json())
