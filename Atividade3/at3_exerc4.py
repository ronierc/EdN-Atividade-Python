"""
Atividade 3 da Escola da Nuvem - Exercício 4:
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) 
    que não são divisíveis por 400.
"""

def bissexto(ano: int) -> bool:
    """
    Verifica se um ano é bissexto.
    Regras:
    - Divisível por 4;
    - Anos centenários (divisíveis por 100) só são bissextos se também forem divisíveis por 400.
    """
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


try:
    ano = int(input("Digite um ano: "))

    if bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")

except ValueError:
    print("Erro: Digite um número inteiro válido!")

