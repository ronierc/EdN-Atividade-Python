"""
Atividade 2 da Escola da Nuvem - Exercício 1:
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

TAXA_DOLAR = 5.2
TAXA_EURO = 6.15

def converte_real(vlr):
    print(f"""
        Valor em reais: R$ {vlr:.2f}
        Valor em dólar({TAXA_DOLAR:.2f}): R$ {vlr*TAXA_DOLAR:.2f}
        Valor em euro({TAXA_EURO:.2f}): R$ {vlr*TAXA_EURO:.2f}
    """)

converte_real(152.25)
