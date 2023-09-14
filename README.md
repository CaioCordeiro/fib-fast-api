# README - Projeto API Fibonacci

Este é um projeto de exemplo que implementa uma API REST em Python usando o framework FastAPI junto do Uvicorn. A API possui duas rotas:

1. Rota de Saúde (/api/health):
   - Responde a uma requisição GET com a mensagem "Estou saudável", indicando que o servidor está funcionando corretamente.

2. Rota de Fibonacci (/api/fibonacci):
   - Recebe uma requisição POST com um número de elementos e retorna uma lista contendo os elementos da sequência de Fibonacci até o número especificado.
   - Exemplo de entrada: `{"elementos": 7}`
   - Saída correspondente: `[0, 1, 1, 2, 3, 5, 8]`

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.10 ou posterior
- Docker
- Um ambiente de desenvolvimento ou servidor com acesso à internet para clonar o repositório e executar a aplicação.

## Instruções de Uso

### Rodar Localmente

1. Entre no repositorio

    ```bash
    cd fib-fast-api
    ```

2. Instale as dependencias

    ```bash
    pip install -r requirements.txt
    ```

3. Rode o servidor

    ```bash
    uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
    ```

A API estará disponível em `http://localhost:8000`.

### Docker

1. Contrua a imagem

    ```bash
    docker build -t fastapi-app .
    ```

2. Inicie o container

    ```bash
    docker run -p 8000:8000 fastapi-app
    ```

A API estará disponível em `http://localhost:8000`.

### Testando as Rotas

Agora que a aplicação está em execução, você pode testar as rotas usando ferramentas como curl ou Postman.

1. GET `/api/health`

    ```bash
    curl -X GET http://localhost:8000/api/health
    "Estou saudável"
    ```

2. POST `/api/fibonacci`

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"elementos": 4}' http://localhost:8000/api/fibonacci
    [ 0, 1, 1, 2]

## Testes

Essa aplicação possui testes unitários, voce pode executar-los para garantir que o codigo funciona como esperado.

1. Entrar no projeto

    ```bash
    cd fib-fast-api
    ```

2. Executar os testes

    ```bash
    python -m unittest discover tests/
    ```
