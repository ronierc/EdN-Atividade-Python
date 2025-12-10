"""
Atividade 4 da Escola da Nuvem - Exercício 1:
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

def calculadora(vlr1, vlr2, op):
    vlr1 = float(vlr1)
    vlr2 = float(vlr2)

    try:
        if op == '+':
            calc = vlr1 + vlr2
            print(f"{vlr1} {op} {vlr2} = {calc}")
        elif op == '-':
            calc = vlr1 - vlr2
            print(f"{vlr1} {op} {vlr2} = {calc}")
        elif op == '/':
            calc = vlr1 / vlr2
            print(f"{vlr1} {op} {vlr2} = {calc}")
        else:
            calc = vlr1 * vlr2
            print(f"{vlr1} {op} {vlr2} = {calc}")
    except ValueError:  
        print("Digite uma conta válida")

vlr1 = input("Digite o 1 valor:")
vlr2 = input("Digite o 2 valor:")
operacao = input("Digite a operação (+,-,*,/):")

calculadora(vlr1, vlr2, operacao)
