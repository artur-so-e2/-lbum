from desenvolviento import listar_album, listar_figuras, comprar_album, comprar_pacotes, abrir_pacotes

albuns = []

figuras = []

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
        listar_album()

    elif escolha == '2':
        listar_figuras()

    elif escolha == '3':
        comprar_album()

    elif escolha == '4':
        comprar_pacotes()

    elif escolha == '5':
        abrir_pacotes()

    elif escolha == '6':
        break

    else:
        print('Erro, opção inválida.')
        continue