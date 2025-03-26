def aventura_do_explorador(passos):
    """
    Simula a jornada de um explorador em uma floresta misteriosa.

    Args:
      passos: Um número inteiro representando a quantidade de passos.
    """
    if passos == 0:
        print("Nenhum passo dado na floresta.")
    elif passos == 1:
        print("Explorador: 1 passo")
    elif passos > 1:
        for i in range(1, passos + 1):
            if i == 1:
                print("Explorador: 1 passo")
            else:
                print(f"Explorador: {i} passos")

try:
    # Solicita a entrada do usuário e tenta converter para inteiro
    passos = int(input(""))
    # Inicia a aventura
    aventura_do_explorador(passos)

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
