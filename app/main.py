from app.pokeapi import buscar_personagem


def main() -> None:
    print("Hello, treinador!")
    personagem = buscar_personagem("pikachu")
    print(f"Nome: {personagem['nome']}")
    print(f"Altura: {personagem['altura']}")


if __name__ == "__main__":
    main()
