# pokedex-api

Este projeto será uma API de personagens dos jogos da franquia Pokémon, permitindo consultar informações sobre os Pokémon e outros personagens que aparecem nos jogos.

> Status: estrutura inicial. Por enquanto, a aplicação apenas imprime uma mensagem de boas-vindas.

## Estrutura

```
pokedex-api/
├── app/
│   ├── __init__.py
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

2. Instale as dependências (ainda vazias):

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
   ```
