"""
Atividade 4 da Escola da Nuvem - Exercício 3:
3 - Criar um código que serve para verificar se uma senha digitada pelo 
    usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""

def verifica_senha(senha):
    if len(senha) < 8:
        return "Senha inválida: deve ter pelo menos 8 caracteres."

    if not any(char.isdigit() for char in senha):
        return "Senha inválida: deve conter pelo menos um número."

    return "Senha válida!"


# Programa principal
senha_usuario = input("Digite uma senha: ")
resultado = verifica_senha(senha_usuario)

print(resultado)
