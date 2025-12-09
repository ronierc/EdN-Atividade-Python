"""
Atividade 2 da Escola da Nuvem - Exercício 4:
Calculadora de Consumo de Combustível

Este programa calcula o consumo médio de combustível de um veículo.
Dados utilizados:
- Distância percorrida: 300 km
- Combustível gasto: 25 litros
"""

def consumo(distancia, combustivel):
    consumo_medio = distancia / combustivel

    print(f"""
        Distância percorrida: {distancia} km
        Combustível gasto: {combustivel} litros
        ---------------------------------------------------
        Consumo Médio: {consumo_medio:.2f} km por litro.
""")

consumo(300, 25)
