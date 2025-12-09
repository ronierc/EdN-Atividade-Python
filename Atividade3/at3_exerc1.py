"""
Atividade 3 da Escola da Nuvem - Exercício 1:
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

-Criança (0-12 anos),
-Adolescente (13-17 anos),
-Adulto (18-59 anos) ou
-Idoso (60 anos ou mais).
"""

def classificar(idade):
    try:
        idade = int(idade)

        if idade <= 12:
            print("Criança")
        elif idade <= 17:
            print("Adolescente")
        elif idade <= 59:
            print("Adulto")
        else:
            print("Idoso")     
    except ValueError:  
        print("Digite uma idade válida")

idade = input("Digite sua idade:")

classificar(idade)
