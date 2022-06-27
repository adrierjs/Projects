def criarArquivo(nome_arquivo):
    nome_arquivo = nome_arquivo + '.txt'
    arquivo = open(nome_arquivo, 'w')
    texto = input('Digite o texto: ')
    arquivo.writelines(texto)
    arquivo.close()


def escreverArquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.writelines('\n')
    arquivo.writelines(texto)
    arquivo.close()


def lerArquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()


def menu():
    usuario = int(input('\nSeja bem-vindo!'
                        '\n Escola a operação a ser realizada:'
                        '\n 1 - Criar arquivo txt'
                        '\n 2 - Editar arquivo txt'
                        '\n 3 - Ler arquivo'
                        '\n 0 - Sair\nEntrada: '))
    return usuario


usuario = -1
while usuario !=0:
    usuario = menu()
    if usuario == 1:
        nome_arquivo = input('Digite o nome do seu arquivo a ser criado: ')
        criarArquivo(nome_arquivo)
    elif usuario == 2:
        texto = input('Digite as proximas linhas: ')
        escreverArquivo(texto)
    elif usuario == 3:
        lerArquivo(input('Digite o nome do arquivo: '))




