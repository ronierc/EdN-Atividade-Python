"""
Atividade 3 da Escola da Nuvem - Exercício 2:
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

def imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)

        calc = peso/ (altura * altura)

        if calc <= 18.5:
            print("Abaixo do peso")
        elif calc <= 25:
            print("Peso normal")
        elif calc <= 30:
            print("Sobrepeso")
        else:
            print("Obeso")
    except ValueError:
        print("Digite um peso válido")

peso = input("Digite seu peso:")
altura = input("Digite sua altura:")

imc(peso, altura)
