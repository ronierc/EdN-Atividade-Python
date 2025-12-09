"""
Atividade 2 da Escola da Nuvem - Exercício 2:
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

def compra(produto, preco, desc):
    calc_desconto = preco * (desc / 100)

    print(f"""
        Produto: {produto}
        Preço: R$ {preco:.2f}
        Valor do desconto R$: {calc_desconto:.2f}
        Total da Compra: R$ {preco - calc_desconto:.2f}""")

compra("Camiseta", 50, 20)
