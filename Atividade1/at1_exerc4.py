"""
    Atividade 1 da Escola da Nuvem - Exercício 4:
    4- Calculadora de Preço Total
    * Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

    * Nome do produto: "Cadeira Infantil"
    * Preço unitário: R$ 12.40
    * Quantidade: 3
    O programa deve calcular o preço total e exibir todas as informações, e o resultado final.
"""

def compra(produto, preco, qtde):
    print(f"""
        Produto: {produto}
        Preço: R$ {preco:.2f}
        Quantidade: {qtde}
        Total da Compra: R$ {(preco * qtde):.2f}""") 

compra("Cadeira Infantil", 12.40, 3)
