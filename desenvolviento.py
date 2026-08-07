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
    for album in albuns:
        if album['obtido'] == False:
            print(f"NOME: {album['nome']}    PREÇO: R${album['preco']}    ID: {album['id']}    OBTIDO: Não")

        elif album['obtido'] == True:
            print(f"NOME: {album['nome']}    PREÇO: R${album['preco']}    ID: {album['id']}    OBTIDO: Sim")

def comprar_pacotes(pacotes):
    print

def abrir_pacotes(pacotes):
    print