from math import prod


def mdc(a, b):
    return a if not b else mdc(b, a % b)


k = int(input("Quantidade de equações: "))

# lendo os A´s
listaA = list()

for i in range(k):

    a = int(input('a{}: '.format(i+1)))
    listaA.append(a)


# lendo os B´s
listaB = list()
for i in range(k):
    b = int(input('b{}: '.format(i+1)))
    listaB.append(b)

# lendo os N´s
listaN = list()
for i in range(k):
    n = int(input('n{}: '.format(i+1)))
    listaN.append(n)

# Verificando se o sistema possui solução
for i in range(k):
    x = listaA[i]
    y = listaN[i]
    temSolucao = True
    # Sistema sem solução
    if mdc(x, y) != 1:
        print("TCR não aplicável")
        temSolucao = False
        break

# Ver mdc entre os N´s
for i in range(k):
    for j in range(i+1, k):
        if mdc(listaN[i], listaN[j]) != 1:
            print("TCR não aplicável")
            temSolucao = False
            break


if temSolucao == True:
    bis = list()
    x = 1
    # Encontrando solução numérica para cada congruência linear //  bi´s
    for i in range(k):
        while True:
            y = (listaA[i]*x) % listaN[i]
            if (y == listaB[i]):
                bis.append(x)
                break
            x = x + 1

    # Encontrando coeficientes auxiliares // ni´s
    nis = list()
    for i in range(k):
        ca = int(prod(listaN) / listaN[i])
        nis.append(ca)

    # Simplificando as equações
    siProv = list()

    for i in range(k):
        si = nis[i] % listaN[i]
        siProv.append(si)

    # Congruências lineares auxiliares // si´s
    sis = list()
    for i in range(k):
        x = 1
        while True:
            y = (siProv[i]*x) % listaN[i] == 1
            if (y == 1):
                sis.append(x)
                break
            x = x + 1

    # Calculando o resultado
    result = list()
    for i in range(k):

        r = bis[i]*nis[i]*sis[i]
        result.append(r)

    resultadoFinal = sum(result) % prod(listaN)
    print("x = {} (mod {})".format(resultadoFinal, prod(listaN)))
    print(sum(result))
