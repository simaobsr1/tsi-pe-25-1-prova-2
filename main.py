def q1(cidades):
    resultado = []

    for nome in cidades:
        if cidades[nome] > 100:
            resultado.append(nome)
    return resultado


def q2(lista1, lista2):

    numeros = []
    for n in lista1 + lista2:
        if n > 0:
            numeros.append(n)
    soma = sum(numeros)
    numeros.sort()
    return (soma, numeros)


def q3():
    
    valores = []
    while True:
        n = int(input("Digite um número (0 para sair): "))
        if n == 0:
            break
        valores.append(n)
    return valores

def processa_lista(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


def q4ler_altura():
    alturas = []
    for i in range(3):
        altura = float(input("Digite a altura: "))
        alturas.append(altura)
    return alturas

def organizar_alturas(lista):
    lista_ordenada = sorted(lista)
    return [lista_ordenada[1], lista_ordenada[2], lista_ordenada[0]]

def formatar_alturas(lista):
    lista_formatada = []
    for altura in lista:
        lista_formatada.append("{:.2f}".format(altura))
    return lista_formatada


def main():
    # Teste as questões que você desenvolveu manualmente:
    # Q 1
    idades = {
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
    print("Q1:", q1(idades))

    #  2
    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    print("Q2:", q2(lista1, lista2))

    #  3
    valores = q3()
    pares, impares = processa_lista(valores)
    print("Q3 - Pares:", pares)
    print("Q3 - Ímpares:", impares)

    # Q 4
    alturas = q4ler_altura()
    organizadas = organizar_alturas(alturas)
    formatadas = formatar_alturas(organizadas)
    print("Q4:", formatadas)



if __name__ == "__main__":
    main()


