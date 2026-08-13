from desenvolviento import listar_album, listar_figuras, comprar_album, comprar_pacotes, abrir_pacotes

albuns = [{'nome': 'Abcdário', 'preco': 25, 'id': '67', 'obtido': False},]

figuras = [{'nome': 'A', 'id': '1', 'id_album': '67', 'obtido': False},
           {'nome': 'B', 'id': '2', 'id_album': '67', 'obtido': False},
           {'nome': 'C', 'id': '3', 'id_album': '67', 'obtido': False},
           {'nome': 'D', 'id': '4', 'id_album': '67', 'obtido': False},
           {'nome': 'E', 'id': '5', 'id_album': '67', 'obtido': False},
           {'nome': 'F', 'id': '6', 'id_album': '67', 'obtido': False},
           {'nome': 'G', 'id': '7', 'id_album': '67', 'obtido': False},
           {'nome': 'H', 'id': '8', 'id_album': '67', 'obtido': False},]

pacotes = []

while(True):
    print('='*15, 'MENU', '='*15)
    print('1 - Listar álbuns')
    print('2 - Listar figuras')
    print('3 - Comprar álbuns')
    print('4 - Comprar pacotes')
    print('5 - Abrir pacotes')
    print('6 - Sair')

    escolha = input('Digite a opção que deseja fazer: ')

    if escolha == '1':
        listar_album(albuns)

    elif escolha == '2':
        listar_figuras(figuras)

    elif escolha == '3':
        comprar_album(albuns)

    elif escolha == '4':
        comprar_pacotes(pacotes)

    elif escolha == '5':
        abrir_pacotes(pacotes)

    elif escolha == '6':
        break

    else:
        print('Erro, opção inválida.')
        continue