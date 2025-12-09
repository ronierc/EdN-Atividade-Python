"""
Atividade 3 da Escola da Nuvem - Exercício 3:
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

def converter_temperatura(temp, un_origem, un_coversao):
    un_origem = un_origem.upper()
    un_coversao = un_coversao.upper()

    # Primeiro, converter tudo para Celsius
    if un_origem == "C":
        temp_c = temp
    elif un_origem == "F":
        temp_c = (temp - 32) * 5/9
    elif un_origem == "K":
        temp_c = temp - 273.15
    else:
        return "Unidade de origem inválida!"

    # Agora converter de Celsius para a desejada
    if un_coversao == "C":
        return temp_c
    elif un_coversao == "F":
        return (temp_c * 9/5) + 32
    elif un_coversao == "K":
        return temp_c + 273.15
    else:
        return "Unidade de destino inválida!"

try:
    temp = float(input("Digite a temperatura: "))
    un_origem = input("Unidade de origem (C, F, K): ")
    un_coversao = input("Unidade de destino (C, F, K): ")

    resultado = converter_temperatura(temp, un_origem, un_coversao)

    print(f"Resultado: {resultado:.2f} {un_coversao.upper()}")

except ValueError:
    print("Erro: Digite apenas números para a temperatura!")

