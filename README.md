# Bem vindos ao repositório do projeto fastapi-musics-app!

Neste projeto criei uma API de Biblioteca de Músicas usando FastAPI e TDD!
O objetivo deste projeto foi colocar em prática meus conhecimentos com o framework FastAPI, compreendendo as diferenças e semelhanças com o Flask, criar APIs rápidas e eficientes e praticar a implementação de uma aplicação completa com camadas bem definidas.

A aplicação permite realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em uma coleção de músicas.

# Detalhes

<details>

  <summary><strong> 🛠 Funcionalidades </strong></summary>
  <br />

- **Criar uma música:** Adicionar uma nova música à biblioteca.
- **Listar todas as músicas:** Obter uma lista de todas as músicas na biblioteca.
- **Selecionar música aleatória:** Selecionar uma música da biblioteca aleatoriamente.
- **Obter uma música específica:** Buscar uma música pelo seu ID.
- **Atualizar uma música:** Atualizar as informações de uma música existente.
- **Deletar uma música:** Remover uma música da biblioteca.

</details>
<br />
<details>

  <summary><strong> 👨‍💻 Tecnologias Utilizadas </strong></summary>
  <br />

- **FastAPI:** Framework principal para a criação da API.
- **Uvicorn:** Servidor ASGI para rodar a aplicação FastAPI.
- **Pydantic:** Para validação de dados e criação de modelos.

</details>
</br>

# Orientações

<details>

  <summary><strong> 🛼 Como executar o projeto </strong></summary>
  <br />

### Pré-requisitos

- Python 3.8 ou superior
- Virtualenv (opcional, mas recomendado)

### Passos para Configuração

1. Clone o repositório com o comando: `git@github.com:linahsu/fastapi-musics-app.git`

</br>

2. Entre na pasta do repositório que você acabou de clonar:
    - `cd fastapi-musics-app`

</br>

3. Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

</br>

4. Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

</br>

5. Utilize o MongoDB com Docker com o comando:

```bash
docker run --name mongodb_v6 -d -p 27017:27017 mongo:6.0
```

</br>

6. Popule o banco de dados com o arquivo seed **musics.mongodb**</br>
**(opcional caso queira visualizar a aplicação já populada com algumas músicas)**

</br>

7. Execute a aplicação com:

```bash
 uvicorn app.main:app --reload
```

</details>
</br>
<details>

<summary><strong>🎛 Linter</strong></summary>
  <br />

Para garantir a qualidade do código, foi utilizado nesse projeto o linter `Flake8`, sendo alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de que o ambiente virtual foi criado e está ativo dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no código, tais problemas serão mostrados no terminal. Se não houver problema no código, nada será impresso no terminal.

</details>
</br>
<details>
  <summary><strong>🛠 Testes</strong></summary>
  <br />

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

<strong>Executar os testes</strong>

```bash
python3 -m pytest
```

Caso você queira que os testes gerem uma saída mais verbosa completa, o comando é:

```bash
python3 -m pytest -s -vv
```

O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

```bash
python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
```

</details>