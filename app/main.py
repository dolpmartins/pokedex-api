from app.pokeapi import buscar_personagem


def main() -> None:
    print("Hello, treinador!")
    personagem = buscar_personagem("pikachu")
    print(f"Nome: {personagem.nome}")
    print(f"Altura: {personagem.altura}")
    print(f"Peso: {personagem.peso}")
    print(f"Tipos: {', '.join(personagem.tipos)}")


if __name__ == "__main__":
    main()
