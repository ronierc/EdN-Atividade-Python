"""
Atividade 4 da Escola da Nuvem - Exercício 4:
4 - Criar um código que serve para analisar números digitados pelo usuário, 
    classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

def analisar_numeros():
    pares = 0
    impares = 0

    print("Digite números (ou 'sair' para encerrar):")

    while True:
        valor = input("Número: ")

        if valor.lower() == "sair":
            break

        try:
            numero = int(valor)

            if numero % 2 == 0:
                print(f"{numero} é PAR")
                pares += 1
            else:
                print(f"{numero} é ÍMPAR")
                impares += 1

        except ValueError:
            print("Entrada inválida! Digite um número inteiro ou 'sair'.")

    print("\n--- Resultado Final ---")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

analisar_numeros()
