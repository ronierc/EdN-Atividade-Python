"""
Atividade 2 da Escola da Nuvem - Exercício 3:
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5

O programa deve calcular a média e exibir todas as notas e o resultado final, 
    arredondando para duas casas decimais.
"""

def media(n1, n2, n3):
    media_final = (n1 + n2 + n3) / 3

    print(f"""
        A média das notas:
          ----------------
          Nota 1: {n1}
          Nota 2: {n2}
          Nota 3: {n3}
          ----------------
          É: { media_final:.2f}
""")

media(7.5, 8, 6.5)
