class Jogador:
    
    #lista de jogadores
    _lista_jogadores = []
    
    #construtor
    def __init__(self, p_nome, p_pontuacao):
        self.nome = p_nome
        self.pontuacao = p_pontuacao

        type(self)._lista_jogadores.append(self)

    #metodo de classe para buscar todos os jogadores do arquivo

    #metodo para encontar um jogador pelo nome
    @classmethod
    def get_jogadores(cls, p_nome_arquivo):

        try:
            with open(p_nome_arquivo, 'rt') as file:
                lista_jogadores = file.read()
        except IOError:
            print('Não foi possível abrir o arquivo!')
        
        lista_jogadores= lista_jogadores.split('\n')

        for i in lista_jogadores:
            nome, pontuacao = i.split('=')
            novo_jogador = Jogador(nome, pontuacao)

    @classmethod
    def get_jogador(cls, nome):
        for obj in cls._lista_jogadores:
            if obj.nome == nome:
                return obj