from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Resposta reduzida da PokéAPI, só com os campos que a aplicação usa
DADOS_PIKACHU = {
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "types": [{"slot": 1, "type": {"name": "electric"}}],
}


@pytest.fixture
def pokeapi_falsa(monkeypatch):
    # Substitui requests.get para os testes não dependerem da internet
    def get_falso(url, timeout):
        if url.endswith("/pikachu"):
            return Mock(status_code=200, json=Mock(return_value=DADOS_PIKACHU))
        return Mock(status_code=404)

    monkeypatch.setattr("app.pokeapi.requests.get", get_falso)


def test_buscar_pikachu_retorna_200(pokeapi_falsa):
    resposta = client.get("/personagens/pikachu")

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "pikachu"


def test_buscar_personagem_inexistente_retorna_404(pokeapi_falsa):
    resposta = client.get("/personagens/personagem-inexistente")

    assert resposta.status_code == 404
