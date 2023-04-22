valores = input("Digite os valores separados por espaço: ")
quantidade = [int(num) for num in valores.split()]
maior = [int(num) for num in valores.split()]

def numeros(*valores):
    print('Valores analisados:', len(quantidade));
    print('Maior valor digitado:', max(maior))

numeros(valores)