import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def buscar_personagem(nome: str) -> dict:
    resposta = requests.get(f"{BASE_URL}/{nome.lower()}", timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()
    return {
        "nome": dados["name"],
        "altura": dados["height"],
    }
