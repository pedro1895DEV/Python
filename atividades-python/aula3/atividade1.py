num1 = int(input("Digite o primeiro número: "));
operador = input("Digite o operador: ");
num2 = int(input("Digite o segundo número: "));

def soma(num1,num2):
    soma =  num1 + num2;
    return soma;
def subtração(num1,num2):
    subtração = num1 -num2;
    return subtração;
def multiplicação(num1,num2):
    multiplicação = num1 * num2;
    return multiplicação;
def divisão(num1,num2):
    divisão = num1 / num2;
    return divisão;

def calculadora(num1, operador, num2):
    if(operador == "+"):
        resultado = soma(num1,num2);
    if(operador == "-"):
        resultado = subtração(num1,num2);
    if(operador == "*"):
        resultado = multiplicação(num1,num2);
    if(operador == "/"):
        resultado = divisão(num1,num2);
    return resultado;

valor = calculadora(num1, operador, num2);
print(valor)