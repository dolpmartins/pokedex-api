from dataclasses import dataclass


@dataclass
class Personagem:
    nome: str
    altura: int  # em decímetros, como vem da PokéAPI
    peso: int  # em hectogramas, como vem da PokéAPI
    tipos: list[str]


def montar_personagem(dados_json: dict) -> Personagem:
    # A PokéAPI ordena os tipos pelo campo "slot" (1 = tipo principal)
    tipos_ordenados = sorted(dados_json["types"], key=lambda t: t["slot"])
    return Personagem(
        nome=dados_json["name"],
        altura=dados_json["height"],
        peso=dados_json["weight"],
        tipos=[t["type"]["name"] for t in tipos_ordenados],
    )
