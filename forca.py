#imports
import menu as m
import game as gm

def buscar_palavras_arquivo(p_nome_arquivo = 'forca_python') -> list:
    
    """
    Parametros
    localização do arquivo
    ---------------------------------------------
    Retorno
    lista de palavras
    ---------------------------------------------
    """
    
    lista_palavras = ""
    try:
        with open('forca_python', 'rt') as file:
            lista_palavras = file.read()
    except IOError:
        print('Não foi possível abrir o arquivo!')
        exit(0)
    
    lista_palavras= lista_palavras.split('\n')

    return lista_palavras

def forca():
    palavras = buscar_palavras_arquivo('forca_python')

    while True:
        acao = m.menu()

        if acao == "1":
            gm.ver_placar()
            input()
        elif acao == "2":
            gm.jogar(palavras)
            input()
        else:
            break
        
        m.menu()

if __name__ == '__main__':
    forca()
    exit(0)






