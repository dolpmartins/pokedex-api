class PersonagemNaoEncontrado(Exception):
    def __init__(self, nome: str) -> None:
        self.nome = nome
        super().__init__(f"Personagem '{nome}' não encontrado na PokéAPI")
