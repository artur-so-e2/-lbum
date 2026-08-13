import random

def listar_album(albuns):
    for album in albuns:
        if album['obtido'] == False:
            print(f"NOME: {album['nome']}    PREÇO: R${album['preco']}    ID: {album['id']}    OBTIDO: Não")

        elif album['obtido'] == True:
            print(f"NOME: {album['nome']}    PREÇO: R${album['preco']}    ID: {album['id']}    OBTIDO: Sim")

def listar_figuras(figuras):
    for figura in figuras:
        if figura['obtido'] == False:
            print(f"NOME: {figura['nome']}    ID: {figura['id']}    ID DO ÁLBUM: {figura['id_album']}    OBTIDO: Não")

        elif figura['obtido'] == True:
            print(f"NOME: {figura['nome']}    ID: {figura['id']}    ID DO ÁLBUM: {figura['id_album']}    OBTIDO: Sim")

def comprar_album(albuns):
    while(True):
        resultado = None
        listar_album(albuns)

        opcao = input("Digite qual o id do álbum você deseja comprar: ")

        for album in albuns:
            if opcao == album['id']:
                album['obtido'] = True
                resultado = album
                print("Compra efetuada com sucesso!")
        if not resultado:
            print("Erro, tente novamente.")
            continue
        else:
            opcao2 = input("Digite se quer continuar comprando álbuns (S/N): ").upper()
            if opcao2 != 'S':
                break

def comprar_pacotes(figuras, pacotes):
    for figura in figuras:
        if figura['obtido'] == False:
            print(f"NOME: {figura['nome']}    ID: {figura['id']}    ID DO ÁLBUM: {figura['id_album']}    OBTIDO: Não")

        elif figura['obtido'] == True:
            print(f"NOME: {figura['nome']}    ID: {figura['id']}    ID DO ÁLBUM: {figura['id_album']}    OBTIDO: Sim")

def abrir_pacotes(pacotes):
    print