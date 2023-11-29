# Programação Estruturada: Prova 03

## Instruções

### Execução manual

Para executar o seu programa: Altere o código no arquivo main com a sua solução e execute no terminal o comando a seguir:

```sh
python main.py
```

### Teste com pytest

Para testar o seu programa com pytest: Altere o código no arquivo main com a sua solução e execute no terminal o comando a seguir:

```sh
pytest
```

## Questão 01

A partir do dicionário de nomes e idades de cidades a seguir, crie uma função que retorne uma lista de cidades maiores que 100 anos.

### Exemplo:

Entrada:

```py
idades_paraiba = {
    "João Pessoa": 432,
    "Campina Grande": 325,
    "Santa Rita": 68,
    "Patos": 289,
    "Bayeux": 54,
    "Sousa": 178,
    "Cajazeiras": 201,
    "Cabedelo": 45,
    "Guarabira": 122,
    "Areia": 177,
}
```

Saída:

resultado_esperado = ['Cabedelo', 'Santa Rita', 'Guarabira', 'Sousa', 'Areia', 'João Pessoa', 'Campina Grande', 'Patos', 'Cajazeiras']

## Questão 02

Crie um programa que leia duas listas (lista1 e lista2), retorne a soma do número maiores que 0 e uma lista dos elementos maiores que 0 em ordem crescente.

### Exemplos

Entrada:

- lista1 = [3, -5, 12, 0, -8, 7]
- lista2 = [-2, 10, -1, 6, -4, 9]

Saída:

- resultado_esperado - 37, [3, 6, 7, 9, 10, 12]

Entrada:

- lista1 = [2, 4, 6, 8, 10]

- lista2 = [-1, -3, -5, -7, -9]

Saída

- resultado_esperado = 30, [2, 4, 6, 8, 10]

## Questão 03:

Você deverá ler valores numéricos até o usuário digitar 0. Crie uma função ler_valores() para retornar os valores deverão ser passados para uma função processa_lista(lista) que irá retornar 2 listas, uma lista para valores pares e uma lista para ímpares.

### Exemplos

- Entrada: [2, 4, 6, 8, 10, 12, 14, 0]

- Saída Esperada:

  - Lista de Pares: [12, 14, 6, 8, 10]
  - Lista de Ímpares: []

- Entrada: [1, 3, 5, 7, 9, 11, 0]
- Saída Esperada:

  - Lista de Pares: []
  - Lista de Ímpares: [11, 9, 7, 5, 3]

- Entrada: [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0]
- Saída Esperada:
  - Lista de Pares: [12, 4, 6, 8, 10]
  - Lista de Ímpares: [11, 3, 5, 7, 9]

## Questão 04

Joaquina é uma fotógrafa muito peculiar. Ela só aceita tirar fotos de pessoas se as pessoas estiverem em grupos de exatamente 04 pessoas. Tudo isso porque Joaquina tem uma mania esquisita de ordenação. Para ela, a pessoa mais baixa deve ficar sempre do lado direito, a segunda mais baixa do lado esquerdo, no meio, logo após a mais baixa, fica a terceira mais baixa e em seguida a mais alta.

Você deverá ler valores numéricos referente à altura em uma função ler_04_alturas() que deve retornar a lista de alturas. Em seguida, os valores deverão ser passados para uma função organizar_alturas(lista) que irá a lista de altuas conforme a organização de Joaquina. Ao final, crie uma função para formatar as alturas da lista de Joaquina, onde cada valor fique com duas casas decimais após a vírgula e retorne esta lista formatada.

### Exemplos

- Entrada

  A entrada consiste de 04 números reais maiores que zero correspondendo às alturas de 04 pessoas. Cada número é dado em uma linha diferente. A entrada pode não estar ordenada.
  [40, 30, 20, 10]

- Saída

  Consiste de 04 números reais, separados por um final de linha, ordenados de acordo com a mania de Ambrosina. Os números devem ser formatados com 02 casas decimais.

  [10.00, 30.00, 40.00, 20.00]
