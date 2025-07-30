# Projeto: Consulta de Países via API

Este projeto contém um script Python para consultar informações sobre países utilizando a API pública [REST Countries](https://restcountries.com/). É possível obter a contagem de países, listar todos os países, consultar capitais e populações.

## Funcionalidades

- Contar o número de países independentes.
- Listar todos os países independentes em ordem alfabética.
- Consultar a capital de um país.
- Consultar a população de um país.

## Requisitos

- Python 3.7+
- [requests](https://pypi.org/project/requests/)

## Instalação

1. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Instale a dependência:
   ```bash
   pip install -r requeriments
   ```

## Como usar

Execute o script com o comando desejado:

```bash
python api-paises.py <acao> <nome do pais>
```

### Ações disponíveis

- `contagem` — Mostra o número de países independentes.
- `paises` — Lista todos os países independentes.
- `capitais <nome do pais>` — Mostra a capital do país informado.
- `populacao <nome do pais>` — Mostra a população do país informado.

### Exemplos

- Contar países:
  ```bash
  python api-paises.py contagem
  ```
- Listar países:
  ```bash
  python api-paises.py paises
  ```
- Consultar capital:
  ```bash
  python api-paises.py capitais Brazil
  ```
- Consultar população:
  ```bash
  python api-paises.py populacao Brazil
  ```

## Observações

- O script depende da disponibilidade da API REST Countries.
- Os nomes dos países devem ser informados em inglês, conforme reconhecidos pela API.

## Licença

MIT 