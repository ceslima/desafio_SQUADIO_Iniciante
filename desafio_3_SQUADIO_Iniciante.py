def cadastro_itens_rpg():
    """
    Cadastra e exibe uma lista de 3 itens de um personagem de RPG usando POO e tratamento de exceções.
    """
    personagem = PersonagemRPG()

    try:
        for i in range(3):
            item = input(f"Digite o nome do {i + 1}º item: ")
            personagem.adicionar_item(item)

        personagem.exibir_itens()

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executa o programa
cadastro_itens_rpg()
