# pokedex-api

Este projeto será uma API de personagens dos jogos da franquia Pokémon, permitindo consultar informações sobre os Pokémon e outros personagens que aparecem nos jogos.

> Status: em desenvolvimento. Por enquanto, a aplicação busca os dados do Pikachu na [PokéAPI](https://pokeapi.co) e imprime nome, altura, peso e tipos.

## Estrutura

```
pokedex-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── pokeapi.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar

1. Crie e ative o ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:

   ```bash
   python -m app.main
   ```

   Saída esperada:

   ```
   Hello, treinador!
   Nome: pikachu
   Altura: 4
   Peso: 60
   Tipos: electric
   ```
