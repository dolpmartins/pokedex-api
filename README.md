# pokedex-api

Este projeto será uma API de personagens dos jogos da franquia Pokémon, permitindo consultar informações sobre os Pokémon e outros personagens que aparecem nos jogos.

> Status: em desenvolvimento. Por enquanto, a API tem o endpoint `GET /personagens/{nome}`, que busca o personagem na [PokéAPI](https://pokeapi.co) e devolve nome, altura, peso e tipos em JSON.

## Estrutura

```
pokedex-api/
├── app/
│   ├── __init__.py
│   ├── exceptions.py
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

3. Inicie o servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Consulte um personagem em http://127.0.0.1:8000/personagens/pikachu:

   ```bash
   curl http://127.0.0.1:8000/personagens/pikachu
   ```

   Resposta esperada:

   ```json
   {"nome": "pikachu", "altura": 4, "peso": 60, "tipos": ["electric"]}
   ```

   A documentação interativa da API fica em http://127.0.0.1:8000/docs.

   Possíveis erros:

   - **404**: o personagem não existe na PokéAPI.
   - **503**: não foi possível conectar à PokéAPI (fora do ar ou sem resposta).
