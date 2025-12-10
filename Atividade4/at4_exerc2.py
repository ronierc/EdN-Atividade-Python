"""
Atividade 4 da Escola da Nuvem - Exercício 2:
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""

def calcular_media_turma():
    try:
        qtd_alunos = int(input("Quantos alunos deseja registrar? "))

        if qtd_alunos <= 0:
            print("A quantidade de alunos deve ser maior que zero.")
            return

        notas = []

        for i in range(1, qtd_alunos + 1):
            nota = float(input(f"Digite a nota do aluno {i}: "))
            notas.append(nota)

        media_turma = sum(notas) / qtd_alunos

        print("\n--- Resultado ---")
        print(f"Notas cadastradas: {notas}")
        print(f"Média da turma: {media_turma:.2f}")

    except ValueError:
        print("Erro: Digite apenas números válidos!")


# Chamada do programa
calcular_media_turma()
