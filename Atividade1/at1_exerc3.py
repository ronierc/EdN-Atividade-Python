"""
    Atividade 1 da Escola da Nuvem - Exercício 3:
    3- Calculadora de Volume
    * Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:
    * Comprimento: 12 cm
    * Largura: 14 cm
    * Altura: 20 cm
    O programa deve calcular o volume e exibir o resultado em cm³.
"""

def volume(comprimento, largura, altura):
    return comprimento * largura * altura

result = volume(12, 14, 20)

print(f"O volume da caixa é {result} cm³")
