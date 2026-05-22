"""
Sistema Persi Stock - Gerenciamento de Estoque
Versão: 1.0
Autor: Alexandre Persi
Descrição: Sistema para cadastrar, remover e visualizar produtos no estoque.
"""

print(" Persi stock ")
print(" Bem vindo ao Persi Stock! ")

produtos = []


while True:
    print("\n--- Menu ---")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Visualizar estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu adicionar um produto.")
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Preço: R$ "))
        produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
        produtos.append(produto)
        print(f"Produto '{nome}' adicionado com sucesso!")

    elif opcao == "2":
        print("Você escolheu remover um produto.")
        nome = input("Digite o nome do produto a ser removido: ")
        for produto in produtos:
            if produto["nome"] == nome:
                produtos.remove(produto)
                print(f"Produto '{nome}' removido com sucesso!")
                break
        else:
            print(f"Produto '{nome}' não encontrado.")

    elif opcao == "3":
        print("DEBUG: Entrei na opcao3")
        if len(produtos) == 0:
            print("O estoque esta vazio.")
        else:
            print("\n--- Produtos cadastrados ---")
            for i, item in enumerate(produtos):
                print(f"{i+1}. {item['nome']} - {item['quantidade']} - und - R$ {item['preco']:.2f}")

    elif opcao == "4":
        print("saindo...")
        break

    else:
        print("Opção invalida! escolha 1, 2, 3 ou 4.")
