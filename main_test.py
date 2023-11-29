# Testes parametrizados corrigidos
import pytest
import mock
import builtins
import main

from solution import q1, q2, q3, q4


@pytest.mark.parametrize("idades_cidades, resultado_esperado", [
    (
        {
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
        },
        ["Cajazeiras", "João Pessoa", "Patos", "Sousa", "Areia", "Guarabira"]
    ),
    (
        {
            "Recife": 150,
            "Caruaru": 110,
            "Olinda": 89,
            "Petrolina": 205,
            "Garanhuns": 98,
            "Jaboatão dos Guararapes": 75,
            "Serra Talhada": 122,
        },
        ["Petrolina", "Recife", "Serra Talhada", "Caruaru"]
    ),
])
def test_q1(idades_cidades, resultado_esperado):
    resultado = q1(idades_cidades)
    assert resultado == resultado_esperado

@pytest.mark.parametrize("lista1, lista2, soma_esperada, resultado_esperado", [
    ([3, -5, 12, 0, -8, 7], [-2, 10, -1, 6, -4, 9], 37, [3, 6, 7, 9, 10, 12]),
    ([2, 4, 6, 8, 10], [-1, -3, -5, -7, -9], 30, [2, 4, 6, 8, 10]),
    ([-1, -2, -3], [-4, -5, -6], 0, []),
])
def test_q2(lista1, lista2, soma_esperada, resultado_esperado):
    soma, resultado = q2(lista1, lista2)
    assert soma == soma_esperada
    assert resultado == resultado_esperado

@pytest.mark.parametrize("entrada, esperado_pares, esperado_impares", [
    ([2, 4, 6, 8, 10, 12, 14, 0], [12, 14, 6, 8, 10], []),
    ([1, 3, 5, 7, 9, 11, 0], [], [11, 3, 5, 7, 9]),
    ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 0], [22, 14, 16, 18, 20], []),
    ([2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0], [12, 4, 6, 8, 10], [11, 3, 5, 7, 9])
])
def test_q3(entrada, esperado_pares, esperado_impares):
    resultado_pares, resultado_impares = q3(entrada)
    assert resultado_pares == esperado_pares
    assert resultado_impares == esperado_impares

@pytest.mark.parametrize("entrada, esperado", [
    ([1.75, 1.80, 1.70, 1.65, 0], ['1.65', '1.75', '1.80', '1.70']),
    ([1.60, 1.62, 1.58, 1.65, 0], ['1.58', '1.62', '1.65', '1.60']),
    ([1.70, 1.68, 1.75, 1.60, 0], ['1.60', '1.70', '1.75', '1.68']),
    ([1.80, 1.75, 1.90, 1.88, 0], ['1.75', '1.88', '1.90', '1.80']),
    ([1.65, 1.60, 1.58, 1.70, 0], ['1.58', '1.65', '1.70', '1.60']),
    # Adicione mais casos conforme necessário
])
def test_q4(entrada, esperado):
    resultado = q4(entrada)
    assert resultado == esperado


