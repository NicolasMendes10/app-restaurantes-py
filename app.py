import os


restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False}
                ,{'nome':'Pizza','categoria':'Pizza','ativo':True}
                ,{'nome':'Cantina','categoria':'Italiana','ativo':False}]

def exibir_nome_programa():
    print('''
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
    ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
    ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
    ''')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/desativar restaurante')
    print('4. Sair \n')


def finalizar_app():
    exibir_subtitulos('Encerrando o programa\n')


def opcao_invalida():
    print('Opção inválida! \n')
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal.')
    main()


def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)    
    print(linha)
    print()


def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante     
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes
    '''

    exibir_subtitulos('## Cadastro de novos restaurantes ##')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante} :')

    dados_do_restaurante = {'nome':nome_restaurante,
                            'categoria':categoria,
                            'ativo':False}
    
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso.')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulos('## Alternando estado do restaurante ##')

    nome_restaurante = input('Digite o nome do restaurante que será alterado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado.')


    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulos('## Listar restaurantes ##')

    print(f'{'Nome do restaurante '.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'DEBUG: Você escolheu a opção {opcao_escolhida}')


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()