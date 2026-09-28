# Pesquisa de Satisfação - TudoWeb

Projeto desenvolvido em Python para a empresa fictícia **TudoWeb**, com o objetivo de realizar uma pesquisa de opinião sobre o atendimento ao cliente.

## Objetivo

Criar um programa que:

- Cadastre 50 entrevistados;
- Solicite nome e idade;
- Solicite a opinião sobre o atendimento;
- Utilize as opções:
  - `1` - EXCELENTE
  - `2` - BOM
  - `3` - RUIM
- Utilize estrutura de repetição `for`;
- Utilize estruturas de decisão `if`, `elif` e `else`;
- Conte as respostas EXCELENTE e RUIM;
- Exiba o resultado ao final da pesquisa.

## Tecnologias

- Python 3
- Visual Studio Code ou outro editor de código
- Git e GitHub

## Como executar

No terminal, entre na pasta do projeto e execute:

```bash
python pesquisa_satisfacao.py
```

O programa solicitará os dados dos 50 entrevistados.

## Validação com 10 entrevistados

Foi criado o arquivo `teste_10_entrevistados.py` para validar a lógica com 10 registros.

Execute:

```bash
python teste_10_entrevistados.py
```

Resultado esperado:

- EXCELENTE: 4
- RUIM: 3
- TESTE APROVADO!

## Estruturas utilizadas

### Estrutura de repetição

```python
for i in range(1, NUM_ENTREVISTADOS + 1):
```

Responsável por repetir a pesquisa para os 50 entrevistados.

### Estrutura de decisão

```python
if opiniao == 1:
    quantidade_excelente += 1
elif opiniao == 2:
    classificacao = "BOM"
else:
    quantidade_ruim += 1
```

Responsável por identificar a opinião escolhida e atualizar os contadores.

## Evidências

A pasta `prints` contém imagens demonstrando:

1. Código-fonte;
2. Execução do teste com 10 entrevistados;
3. Resultado final do teste.

## Competências desenvolvidas

- Implementação de algoritmos de programação;
- Utilização da linguagem Python;
- Estrutura de repetição;
- Estruturas de decisão;
- Raciocínio lógico;
- Teste e validação de programas;
- Organização de projeto para GitHub.
